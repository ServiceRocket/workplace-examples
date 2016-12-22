import json
import os
import requests
import sys

"""
Simple script to post content and attachment to a Workplace group, similar to `post-to-group.py`.

    $ ACCESS_TOKEN=... COMMUNITY_ID=... python post-to-group.py <user_id> <group_id> <file_path> "Hello world!"

"""

GRAPH_URL_PREFIX = 'https://graph.facebook.com/'

access_token = os.environ['ACCESS_TOKEN']
community_id = os.environ['COMMUNITY_ID']
impersonate_user_id = sys.argv[1]
group_to_post_to_id = sys.argv[2]
file_to_post = sys.argv[3]
message_to_post = sys.argv[4]

def buildHeader(access_token):
  return {'Authorization': 'Bearer ' + access_token}

def postToGroupWithFile(access_token):
  headers = buildHeader(access_token)
  result = requests.get(GRAPH_URL_PREFIX + impersonate_user_id + '?fields=impersonate_token', headers=headers)
  data = json.loads(result.text, result.encoding)
  impersonate_token = data["impersonate_token"]
  headers = buildHeader(impersonate_token)

  files = {'file': open(file_to_post, 'rb')}
  data = {
    "name": message_to_post
  }
  result = requests.post(GRAPH_URL_PREFIX + group_to_post_to_id + '/photos', headers=headers, files=files, data=data)
  return json.loads(result.text, result.encoding)

result = postToGroupWithFile(access_token)
print(result)
