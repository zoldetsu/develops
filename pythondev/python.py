
import json

name_json = 'json.json'
with open(name_json, 'r') as file_js:
    file_js = json.load(file_js) 
print(file_js)
file_js["model"] = [2, {"xex": 26}]

print(json.dumps(file_js,indent=2))

with open(name_json,'w') as file_json:
    json.dump(file_js, file_json, indent=4)


print(file_js["model"][0])