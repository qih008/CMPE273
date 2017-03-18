from github import Github
import base64
import os
import yaml 
import json

g = Github()

# user = g.get_user("sithu")
#repo = g.get_repo("sithu/assignment1-config-example"). # work!!
url_temp = "https://github.com/sithu/assignment1-config-example"
repo = g.get_repo(url_temp.split("https://github.com/")[1])


#content = repo.get_file_contents("/dev-config.yml").content
content = repo.get_file_contents("/dev-config.yml").content
decode_str = base64.b64decode(content)   # output for yaml
temp = "dev-config.yml"
file_extension = os.path.splitext(temp)[1] 
if file_extension == ".yml":
    print decode_str
elif file_extension == ".json":
    str_json = json.dumps(yaml.load(decode_str), sort_keys=True, indent=2) # output for json
    print str_json