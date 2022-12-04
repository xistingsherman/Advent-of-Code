
import http.client

f = open("D:\Documents\Advent of Code\Day 4\input.txt", "r")

lines = f.readlines()


count = 0
for line in lines:
    line = line.strip()
    left,right = line.split(',')
    l1,l2 = left.split('-')
    r1,r2 = right.split('-')
    l1 = int(l1)
    l2 = int(l2)
    r1 = int(r1)
    r2 = int(r2)

    if (l1 >= r1) and (l2 <= r2):
        count += 1

    elif (r1 >= l1) and (r2 <= l2):
        count += 1

print(count)
f.close()



conn = http.client.HTTPSConnection("adventofcode.com")

payload = str(count)

headers = {
  'Cookie': 'session=sessionIDgoesHere'

}

conn.request("POST", "/2022/day/2/input", payload, headers)

res = conn.getresponse()

data = res.read()

print(data.decode("utf-8"))
