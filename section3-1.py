import sys
import io
import urllib.request as req
from urllib.parse import urlparse

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://www.encar.com"

mem = req.urlopen(url)

#print(mem)

print(mem.geturl())
print(mem.getcode())
#print(mem.info())
print(urlparse("https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EB%8F%99%EB%AC%BC#imgId=post5259850_1726833499&vType=rollout"))
