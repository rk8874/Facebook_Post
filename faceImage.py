import facebook
import os
import sys
import io
from PIL import Image
import sys
import argparse
import json
#below the code use for taken user input from the command line.
parser = argparse.ArgumentParser()
parser.add_argument("-file_path", "--Input", help = "Show Output")
parser.add_argument("-description", "--input", help = "Show Output")
parser.add_argument("-json", "--Input1", help = "Show Output")
args = parser.parse_args()
f = open(args.Input1)
data = json.load(f)
jsonData = data["Facebook"]
token= jsonData["Access_token"]
page_Id= jsonData["Page_Id"]
file=args.Input+jsonData["File_Name"]
def main():
    graph = facebook.GraphAPI(access_token=token, version='3.1')
    response=graph.put_photo(image=open(file, 'rb'),caption=args.input, profile_id=page_Id)
    print (f"Image_Id: {response['id']}")
    print("Image uploaded!!")
if __name__ == "__main__":
    main()
