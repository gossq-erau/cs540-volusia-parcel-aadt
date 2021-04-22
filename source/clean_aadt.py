import pandas as pd
import shapefile
import points


class CleanAADT(object):
    def __init__(self):
        self.load_aadt()
        self.main()
        return

    def load_aadt(self):
        # Load the AADT shapefile as a pandas dataframe
        # @return DataFrame :
        #   AADT data as a pandas dataframe.
        sf_path = "data/aadt_volusia.shp"
        sf = shapefile.Reader(sf_path)
        print(sf)
        shapes = [s.points for s in sf.shapes()]
        fields = [f[0].upper() for f in sf.fields[1:]]
        records = sf.records()

        df = pd.DataFrame(columns = fields, data = records)
        self.aadt = df.assign(SHAPE=shapes)
        return

    


    def main(self):
        print(self.aadt.columns)
        
        # Select roads in Volusia county
        county = "Volusia"
        self.aadt = self.aadt[self.aadt.COUNTY == county]
        
        # print(self.aadt.describe())
        self.aadt.SHAPE = self.aadt.SHAPE.apply(points.shape_to_linestring)
        
        print(self.aadt)

        # Save to csv
        self.aadt.to_csv("csv/volusia-aadt.csv",sep="\t",header=False)
        

        # d = points.point_shape_distance_2d([10,10],self.aadt.SHAPE.iloc[0])
        # print(d)
        return

if __name__ == "__main__":
    CleanAADT()
    print("DONE!")