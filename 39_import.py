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

with codecs.open('json39_tq.json', 'r',encoding='utf-8') as f:
    contents = f.read()
    # content = ''.join()
    # print(contents[0:2])
    # c=''
    # for line in contents:
    #     # line = line.strip()
    #     c+=line

    # print(type(c))
    # print(c[0:10])
    l = json.loads(contents)
    # print(type(l))
    # print(l[0])
    # print('++++++++++++++++++++++')
    print(len(l))
    print(l[1995])
    #
    # for b in l:
    #     #创建疾病节点
    #     node_jb = Node('疾病', 名称=b['疾病名称'],治疗费用=b['治疗费用'],患病比例=b['患病比例'],易感人群=b['易感人群'],
    #                    是否属于医保=b['是否属于医保'],传染方式=b['传染方式'],治疗周期=b['治疗周期'],治愈率=b['治愈率'])
    #     graph.merge(node_jb)
    #     #创建治疗方式节点并建立关系
    #     for a in b['治疗方式']:
    #         node_zlfs = Node('治疗方式', 名称=a)
    #         graph.merge(node_zlfs)
    #         query1 = "match(p:%s),(q:%s) where p.名称='%s'and q.名称='%s' merge (p)-[rel:%s]->(q)" % (
    #             '疾病', '治疗方式', b['疾病名称'], a, '治疗方式')
    #         graph.run(query1)
    #
    #     # 创建症状节点并建立关系
    #     for z in b['症状']:
    #         node_zz = Node('症状', 名称=z)
    #         graph.merge(node_zz)
    #         query2 = "match(p:%s),(q:%s) where p.名称='%s'and q.名称='%s' merge (p)-[rel:%s]->(q)" % (
    #             '疾病', '症状', b['疾病名称'], z, '症状')
    #         graph.run(query2)
    #
    #     # 创建科室节点并建立关系
    #     for k in b['科室']:
    #         node_ks = Node('科室', 名称=k)
    #         graph.merge(node_ks)
    #         query3 = "match(p:%s),(q:%s) where p.名称='%s'and q.名称='%s' merge (p)-[rel:%s]->(q)" % (
    #             '疾病', '科室', b['疾病名称'], k, '科室')
    #         graph.run(query3)
    #
    #     # 创建药品节点并建立关系
    #     for y in b['药品']:
    #         node_yp = Node('药品', 名称=y)
    #         graph.merge(node_yp)
    #         query4 = "match(p:%s),(q:%s) where p.名称='%s'and q.名称='%s' merge (p)-[rel:%s]->(q)" % (
    #             '疾病', '药品', b['疾病名称'], y, '药品')
    #         graph.run(query4)

        #
        # node_zz = Node('症状', name=b['疾病名称'],con=b.get('症状','no').replace('\n', '').replace("'", "\\'"))
        # graph.merge(node_zz)
        # node_by = Node('病因', name=b['疾病名称'], con=b.get('病因','no').replace('\n', '').replace("'", "\\'"))
        # graph.merge(node_by)
        # node_jy = Node('就医', name=b['疾病名称'], con=b.get('就医','no').replace('\n', '').replace("'", "\\'"))
        # graph.merge(node_jy)
        # node_zl = Node('治疗', name=b['疾病名称'], con=b.get('治疗','no').replace('\n', '').replace("'", "\\'"))
        # graph.merge(node_zl)
        # sql_gs = "match(p:%s) where p.name='%s' set p.des='%s'" % ('疾病',b['疾病名称'], b.get('概述','no').replace('\n', '').replace("'", "\\'"))
        # graph.run(sql_gs)
        # node_yf = Node('预防', name=b['疾病名称'], con=b.get('预防','no').replace('\n', '').replace("'", "\\'"))
        # graph.merge(node_yf)
        # node_rc = Node('日常', name=b['疾病名称'], con=b.get('日常','no').replace('\n', '').replace("'", "\\'"))
        # graph.merge(node_rc)
        # query1 = "match(p:%s),(q:%s) where p.name='%s'and q.name='%s' merge (p)-[rel:%s]->(q)" % (
        #     '疾病', '症状', b['疾病名称'], b['疾病名称'], '症状')
        # graph.run(query1)
        # query2 = "match(p:%s),(q:%s) where p.name='%s'and q.name='%s' merge (p)-[rel:%s]->(q)" % (
        # '疾病', '病因', b['疾病名称'], b['疾病名称'], '病因')
        # graph.run(query2)
        # query3 = "match(p:%s),(q:%s) where p.name='%s'and q.name='%s' merge (p)-[rel:%s]->(q)" % (
        # '疾病', '就医', b['疾病名称'], b['疾病名称'], '就医')
        # graph.run(query3)
        # query4 = "match(p:%s),(q:%s) where p.name='%s'and q.name='%s' merge (p)-[rel:%s]->(q)" % (
        # '疾病', '治疗', b['疾病名称'], b['疾病名称'], '治疗')
        # graph.run(query4)
        # query5 = "match(p:%s),(q:%s) where p.name='%s'and q.name='%s' merge (p)-[rel:%s]->(q)" % (
        # '疾病', '预防', b['疾病名称'], b['疾病名称'], '预防')
        # graph.run(query5)
        # query6 = "match(p:%s),(q:%s) where p.name='%s'and q.name='%s' merge (p)-[rel:%s]->(q)" % (
        # '疾病', '日常', b['疾病名称'], b['疾病名称'], '日常')
        # graph.run(query6)
    # for b in l:
    # # 创建并发症关系
    #     for jb in b['并发症']:
    #         query5 = "match(p:%s),(q:%s) where p.名称='%s'and q.名称='%s' merge (p)-[rel:%s]->(q)" % (
    #             '疾病', '疾病', b['疾病名称'], jb, '并发症')
    #         graph.run(query5)


