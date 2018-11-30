# coding: utf-8

from py2neo import Node, Relationship, Graph
from pandas import DataFrame
import json
import codecs

# graph = Graph(
#             host="127.0.0.1",  # neo4j 搭载服务器的ip地址，ifconfig可获取到
#             http_port=7474,  # neo4j 服务器监听的端口号
#             user="neo4j",  # 数据库user name，如果没有更改过，应该是neo4j
#             password="123")
# graph = Graph(
#             host="154.8.214.203",  # neo4j 搭载服务器的ip地址，ifconfig可获取到
#             http_port=7474,  # neo4j 服务器监听的端口号
#             user="neo4j",  # 数据库user name，如果没有更改过，应该是neo4j
#             password="m4eeee")

with codecs.open('json39_tq2.json', 'r',encoding='utf-8') as f:
    contents = f.read()
    l = json.loads(contents)
    # print(type(l))
    # print(l[0])
    # print('++++++++++++++++++++++')
    print(len(l))
    print(l[1995])
    #
    # for b in l:
    #     #补充疾病节点的简介
    #     query1 = "match(p:%s) where p.名称='%s' set p.简介='%s'" % (
    #         '疾病', b['疾病名称'], b['简介'].replace("'", "\\'"))
    #     graph.run(query1)
    #     for jb in b['并发症']:
    #         query2 = "match(p:%s),(q:%s) where p.名称='%s'and q.名称='%s' merge (p)-[rel:%s]->(q)" % (
    #             '疾病', '疾病', b['疾病名称'], jb, '并发症')
    #         graph.run(query2)