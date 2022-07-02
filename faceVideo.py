import requests
import sys
import argparse
import json
parser = argparse.ArgumentParser()
parser.add_argument("-file_path", "--Input", help = "Show Output")
parser.add_argument("-title", "--input", help = "Show Output")
parser.add_argument("-description", "--input1", help = "Show Output")
parser.add_argument("-json", "--Input1", help = "Show Output")
args = parser.parse_args()
Title=args.input
Description=args.input1
f = open(args.Input1)
data = json.load(f)
jsonData = data["Facebook"]
token= jsonData["Access_token"]
page_Id= jsonData["Page_Id"]
url='https://graph-video.facebook.com/v14.0/'+page_Id+'/videos'
#?access_token='+str(token)
payload = {
    'access_token': token, 
    'title': Title,
    'description': Description
}
path=args.Input+jsonData["File_Name"]
files={'file':open(path,'rb')}
flag=requests.post(url, files=files, data=payload, verify=False).text
print (flag)
#print("Video Uploaded")