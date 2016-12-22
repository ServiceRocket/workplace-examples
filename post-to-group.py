import json
import os
import requests
import sys

"""
Simple script to post content to a Workplace group by impersonating a person.

    $ ACCESS_TOKEN=... COMMUNITY_ID=... python post-to-group.py <user_id> <group_id> "Hello world!"

"""

GRAPH_URL_PREFIX = 'https://graph.facebook.com/'

access_token = os.environ['ACCESS_TOKEN']
community_id = os.environ['COMMUNITY_ID']
impersonate_user_id = sys.argv[1]
group_to_post_to_id = sys.argv[2]
message_to_post = sys.argv[3]

def buildHeader(access_token):
  return {'Authorization': 'Bearer ' + access_token}

def postToGroup(access_token):
  headers = buildHeader(access_token)
  result = requests.get(GRAPH_URL_PREFIX + impersonate_user_id + '?fields=impersonate_token', headers=headers)
  data = json.loads(result.text, result.encoding)
  impersonate_token = data["impersonate_token"]
  headers = buildHeader(impersonate_token)

  data = {
    "message": message_to_post,
    "type": "status"
  }

  result = requests.post(GRAPH_URL_PREFIX + group_to_post_to_id + '/feed', headers=headers, data=data)
  return json.loads(result.text, result.encoding)

result = postToGroup(access_token)
print(result)
