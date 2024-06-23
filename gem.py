from urllib.request import urlopen

response = urlopen('http://google.com/')
html = response.read()
print(html)
