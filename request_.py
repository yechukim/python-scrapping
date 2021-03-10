import requests

res = requests.get("http://google.com")
res.raise_for_status()

print("ok", res.status_code)
print(len(res.text))

with open("myGoogle.html","w", encoding="utf8") as f:
  f.write(res.text)