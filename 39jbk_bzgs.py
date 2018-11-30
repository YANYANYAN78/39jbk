# coding: utf-8

# from py2neo import Node, Relationship, Graph
# from pandas import DataFrame
import json
import codecs

with codecs.open('json39_tq.json', 'r',encoding='utf-8') as f:
    contents = f.read()
    l1 = json.loads(contents)

with codecs.open('json39_tq2.json', 'r',encoding='utf-8') as f:
    contents = f.read()
    l2 = json.loads(contents)


for i in l1:
    for j in l2:
        if i['疾病名称']==j['疾病名称']:
            i['简介']=j['简介']
            i['并发症']=j['并发症']

js39 = json.dumps(l1,ensure_ascii=False)

with open('json39_bzgs.json', 'wb') as ff:
    ff.write(js39.encode('utf-8'))


with open('json39_bzgs.json', 'r',encoding='utf-8') as f:
    content = f.read()
    ll = json.loads(content)
    print(len(ll))
    print(ll[0]) 