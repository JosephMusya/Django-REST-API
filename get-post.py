import requests

LOGIN_TOKEN = 'be590b7a4c26e54091d6d83ee6b85e157b058000'
AUTH = {
        'Authorization': 'Token {}'.format(LOGIN_TOKEN)
    }

url = 'http://localhost:8000/event/3'
response = requests.get(url).json()

PARAMS = {
    'location':'Dedan Kimathi Uni',
    'topic': response['topic'],
    'date':  response['date'],
}
try:
    new_response = requests.put(url,headers=AUTH,json=PARAMS)
    print(new_response.json()['location'])
    while True:
        data = requests.get(url).json()
        print(data)
except Exception as e:
    print("ERROR",e)
