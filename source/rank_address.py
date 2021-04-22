import pandas as pd
import pickle
import numpy as np

class RankAddress(object):
    def __init__(self):
        self.init_addrs()
        self.init_aadt()
        
        # Link table between gis_address and aadt
        addr_aadt = self.addrs[['pid',"seg_id"]]
        addr_aadt.to_csv("csv/volusia-addr_addt.csv",header=None,index=False)
        
        # Updated aadt now with rank
        self.aadt.to_csv("csv/volusia-aadt-segments2.csv",header=None,index=False)
        
        return

    def init_aadt(self):
        self.aadt = pd.read_csv("csv/volusia-aadt-segments.csv",low_memory=False)
        self.aadt = self.aadt.assign(rank=self.aadt.aadt.apply(self.classify_aadt))
        return

    def classify_aadt(self,aadt):
        # classifies each aadt as low=1, med=2, high=3 traffic
        # 
        # @param aadt : float 
        #   AADT value
        #
        # @return : int
        #   low=1, med=2, high=3, no data=NaN
        med = 11777
        high = 25305
        if aadt >= 0 and aadt < med: return 1
        elif aadt >= med and aadt < high: return 2
        elif aadt >= high: return 3
        return np.NaN

    





    def init_addrs(self):
        self.addrs = pd.read_csv("csv/volusia-address.csv",low_memory=False)
        self.init_ans()
        return





    def init_ans(self):
        # Load Address Nearest Segment data and attach it to adress table as seg_id
        pickles = ["pkl\\ans.pkl0-50000","pkl\\ans.pkl50000-100000","pkl\\ans.pkl100000-150000",
                "pkl\\ans.pkl150000-200000","pkl\\ans.pkl200000-250000","pkl\\ans.pkl250000-251938"]
        ans = []
        for fn in pickles:
            with open(fn,"rb") as f:
                ans.append(pickle.load(f))
        ans = [item for sublist in ans for item in sublist]
        self.addrs = self.addrs.assign(seg_id=ans)
        return 

if __name__ == "__main__":
    RankAddress()