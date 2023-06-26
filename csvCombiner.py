import os
import glob
import pandas as pd

def merge():

    path = "/Users/lspagnoli/Desktop/data"

    all_files = glob.glob(os.path.join(path, "*.csv"))
    df = pd.concat((pd.read_csv(f) for f in all_files))

    df.to_csv("/Users/lspagnoli/Desktop/NEWMerged.csv", index=False)

    print("Merged!")

def toCSV():

    #dataNew = pd.read_stata('/Users/lspagnoli/Desktop/dataNew.dta')
    dataOld = pd.read_stata('/Users/lspagnoli/Desktop/dataOld')

    #dataNew.to_csv('/Users/lspagnoli/Desktop/data/new.csv', index=False)
    dataOld.to_csv('/Users/lspagnoli/Desktop/dataNew', index=False)

    print("Converted!")

def main():

    #print("Starting Conversion...")
    #toCSV()
    print("Starting Merge...")
    merge()
    print("Complete!!!")


main()