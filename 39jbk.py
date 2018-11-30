# coding: utf-8
from py2neo import Node, Relationship, Graph
from pandas import DataFrame
import json
# import codecs


L=[]

with open('../医疗/39jbk.json', 'r',encoding='utf-8') as f:
    contents = f.read()
    l = json.loads(contents)
    # print(len(l))
    # print(l[0])

for i in l:
    d={}
    d['药品']=list(i.get('常用药品',''))#list
    d['治愈率']=''.join(i.get('治愈率','')).replace('。','')#str
    d['患病比例'] = None#float
    d['简介']=i.get('sick_introduce','')#str
    d['疾病名称'] = i.get('sick_name', '')#str
    d['科室'] = list(i.get('挂号的科室', ''))#list
    d['治疗周期'] = ''.join(i.get('治疗周期', '')).replace('。', '')#str
    d['并发症'] = list(i.get('并发症', ''))#list
    d['治疗方式'] = ''.join(i.get('治疗方法', '')).split('、')#list
    d['症状'] = list(i.get('典型症状', ''))  # list
    crx = list(i.get('传染性',''))
    cbtj= list(i.get('传播途径',''))
    if crx==["无传染性"] and cbtj==[]:
        d['传染方式']=''.join(crx)#str
    elif crx==[] and cbtj==[]:
        d['传染方式']=''#str
    elif cbtj !=[]:
        d['传染方式'] =cbtj
    else:
        d['传染方式'] = ''  # str
    sfyb =list(i.get('是否属于医保',''))
    if sfyb==[]:
        d['是否属于医保']='-'
    elif sfyb==["医保疾病"]:
        d['是否属于医保']='是'
    d['治疗费用'] = ''.join(i.get('治疗费用', '暂无')).replace('。', '')  # str
    d['易感人群'] = ''.join(i.get('多发人群', '暂无')).replace('。', '')  # str
    L.append(d)
#
js39 = json.dumps(L,ensure_ascii=False)

with open('json39_tq.json', 'wb') as ff:
    ff.write(js39.encode('utf-8'))


with open('json39_tq.json', 'r',encoding='utf-8') as f:
    content = f.read()
    ll = json.loads(content)
    print(len(ll))
    print(ll[0])