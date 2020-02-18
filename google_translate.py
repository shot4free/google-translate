#!/usr/bin/python3

import json
from apiclient.discovery import build

query='This is a test to translate english to polish'
target_language = 'pl'

service = build('translate','v2',developerKey='')

collection = service.translations()

request = collection.list(q=query, target=target_language)

response = request.execute()

response_json = json.dumps(response)

ascii_translation = ((response['translations'][0])['translatedText'])

print(response)
print(ascii_translation)
