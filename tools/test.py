import requests
import json

if __name__ == "__main__":
    payload = {'some': 'askdjfl;aksdfl;j'}
    response = requests.post(
        url="http://localhost:9999/payback",
        data=json.dumps(payload),
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        )
    print(response.text)