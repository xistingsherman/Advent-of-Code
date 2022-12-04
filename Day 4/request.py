import http.client

conn = http.client.HTTPSConnection("adventofcode.com")

payload = ''

headers = {

  'Cookie': 'session=sessionNumberGoesHere'

}

conn.request("POST", "/2022/day/2/input", payload, headers)

res = conn.getresponse()

data = res.read()

print(data.decode("utf-8"))