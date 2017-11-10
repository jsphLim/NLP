import requests
 import json
 import re
 from bosonnlp import BosonNLP
 url = 'http://music.163.com/api/song/lyric?' + 'id=' + str(115162) + '&lv=1&kv=1&tv=-1'
 lyric = requests.get(url)
 jsonObject = lyric.text
 j = json.loads(jsonObject)
 lrc = j['lrc']['lyric']
 pat = re.compile(r'\[.*\]')
 lrc = re.sub(pat, "", lrc)
 lrc = lrc.strip()
 lrc = lrc.split()
 nlp = BosonNLP('xxxxxxxxxxxxxxxxx') #输入你的NLP密钥
 for i in lrc:
     print(nlp.sentiment(i))
