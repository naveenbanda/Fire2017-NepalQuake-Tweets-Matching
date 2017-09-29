import json
import csv

jsonfile=open("Nepal-training-20K.jsons",'r')
csv_out=open("tweets.csv","w+")
csvwriter=csv.writer(csv_out)

fields=["id","text"]
csvwriter.writerow(fields)

for item in jsonfile:
	tweet=json.loads(item)

	csvwriter.writerow([tweet.get("id"),tweet.get("text").encode("unicode_escape")])

csv_out.close()
jsonfile.close()




