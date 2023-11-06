import os
import glob
import pandas as pd

def merge(dataPath, outputPath):

    print("Starting Merge...")
    
    all_files = glob.glob(os.path.join(dataPath, "*.csv"))
    df = pd.concat((pd.read_csv(f) for f in all_files))
    df.to_csv(outputPath, index=False)
    
    print("Merged!")

def dtaToCSV(toConvertPath, outputPath):

    print("Starting Conversion...")
    
    dataOld = pd.read_stata(toConvertPath)
    dataOld.to_csv(outputPath, index=False)

    print("Converted!")

def main():
    #Uncomment the helper functions you require!
    
   #~~~~~~~~~~~~dtaToCSV~~~~~~~~~~~~
    #converts dta files to csv files:

    """
    toConvertPath = '/Users/lspagnoli/Desktop/dataOld' #file path for the dta file to be converted
    outputPath = '/Users/lspagnoli/Desktop/dataNew' #the location of the converted file, including new file name
    
    dtaToCSV(toConvertPath, outputPath)
    """
    
    #~~~~~~~~~~~~merge~~~~~~~~~~~~
    #takes all csv files in a folder and merges them into one new file:

    """
    toConvertPath = '/Users/lspagnoli/Desktop/data' #file path for the folder containing data to be merged
    outputPath = "/Users/lspagnoli/Desktop/NEWMerged.csv" #the location of the new merged file, including new file name
    
    merge(toConvertPath, outputPath)
    """

     print("Complete :3")


main()
