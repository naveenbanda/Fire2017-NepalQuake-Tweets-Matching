import json
import csv

jsonfile=open("Nepal-twitter-code-mixed-47k.jsons",'r')
csv_out=open("TestDataset.csv","w+")
csvwriter=csv.writer(csv_out)

fields=["id","text"]
csvwriter.writerow(fields)

for item in jsonfile:
	tweet=json.loads(item)

	csvwriter.writerow([tweet.get("id"),tweet.get("text").encode("unicode_escape")])

csv_out.close()
jsonfile.close()




