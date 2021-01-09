import json
import urllib.request, urllib.parse, urllib.error
import ssl



ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = "http://py4e-data.dr-chuck.net/comments_1080924.json"
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()

info = json.loads(data)
print('User count:', len(info))
count = 0
for item in info["comments"]:
    count+= int(item["count"])
print(count)
