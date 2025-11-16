import json
import requests
import numpy

url =  'https://api.datamuse.com/words?ml=duck&sp=b*&max=3'

print(url)

request = requests.get(url)
#print(request.text)

rqst_dict = json.loads(request.text)
#print(rqst_dict)

json.dump(rqst_dict, open("/workspaces/content_video_repo_python/week13/test.json", "w"))

#print(rqst_dict.keys())

scores = []
for d in rqst_dict:
    scores.append(d["score"])
print("scores", scores)
print ("avg score: ", numpy.mean(scores))