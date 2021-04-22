
from argparse import ArgumentParser
import pandas as pd
import points
import pickle

class NearestSegment(object):
    def __init__(self,i_low,i_high):

        self.i_low = i_low
        self.i_high = i_high

        # print(self.i_low, self.i_high)
        # return

        self.addrs = pd.read_csv("csv/volusia-address.csv",low_memory=False)
        self.addrs.geom = self.addrs.geom.apply(points.wkb_decode)
        print("volusia.address table loaded.")

        self.aadt = pd.read_csv("csv/volusia-aadt-segments.csv",low_memory=False)
        self.aadt.geom = self.aadt.geom.apply(points.wkb_decode)
        # print(self.aadt)
        print("volusia.aadt_segments table loaded.")

        line = self.aadt.geom.iloc[0]
        pt = self.addrs.geom.iloc[0]
        
        # d = points.point_line_distance_2d(pt,line.coords[0],line.coords[1])
        # d = points.point_shape_distance_2d(pt,line)
        # print(d)

        # self.nearest_segment(pt)
        # ans = self.all_nearest_segments()

        self.all_nearest_segments()
        

        # with open("pkl/ans.pkl","rb") as f:
        #     line = pickle.load(f)
        
        # print(line)

        return


    def all_nearest_segments(self):
        ans = []
        for i in range(self.i_low,self.i_high):
            try:
                seg_id = self.nearest_segment(self.addrs.geom.iloc[i])
            except:
                seg_id = None
            ans.append(seg_id)


            n = i-self.i_low
            goal = self.i_high - self.i_low
            print("Progress %.2f%% %d/%d" % ( (n/goal)*100, n, goal), end="\r")

        with open("pkl/ans.pkl%d-%d" % (self.i_low,self.i_high),'wb') as f:
            pickle.dump(ans,f)
        return


    def nearest_segment(self,point):
        # Finds the seg_id of the nearest aadt segment to a point
        #
        # @param point : shapely point
        #   (x,y) coordinate
        # 
        # @return segment id
        distances = [points.point_shape_distance_2d(point,line) for line in self.aadt.geom]
        d = min(distances)
        seg_id = self.aadt.seg_id.iloc[distances.index(d)]
        return seg_id

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser("Find nearest seg_id")
    parser.add_argument("--ilow",dest="ilow",type=int)
    parser.add_argument("--ihigh",dest="ihigh",type=int)
    args = parser.parse_args()


    NearestSegment(i_low = args.ilow, i_high = args.ihigh)
    print("DONE")