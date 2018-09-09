#!/usr/bin/env python
# coding: utf-8
# 国家统计局省市县乡4级行政区划爬虫

import requests
from bs4 import BeautifulSoup as bs

 

def get_rslt(abc):
    base_url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/'
    url = base_url + abc
    kv = {'user-agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    soup = bs(r.text,'lxml')
    rslt = []
    for i in soup.find_all(['a']):
        rslt.append([i['href'],i['href'][:2],i.contents[0]])
    return rslt[:-1]

province_html = []
province_dic = {}
a = get_rslt('index.html')
for i in a:
    province_html.append(i[0])
    province_dic[i[1]] = i[2]

city_html = []
city_dic = {}
for i in province_html:
#for i in ['34.html']:
    x = i.split('.')[0]
    a = get_rslt(i)
    b = []
    c = []
    for j in a:
        b.append(j[0])
        c.append(j[2])
    d = [b[i] for i in range(len(b)) if i%2]
    e = [c[i] for i in range(len(c)) if i%2]
    f = [c[i] for i in range((len(c))) if (i+1)%2]
    g = {}
    for j in range(len(e)):
        g[f[j][:4]] = e[j]
    city_dic[x] = g
    for i in d:
        city_html.append(i)

county_html = [] 
county_dic = {} 
for i in city_html:
    x = i[3:7]
    a = get_rslt(i)
    b = [] 
    c = []
    for j in a:
        b.append(j[0])
        c.append(j[2])
    d = [b[i] for i in range(len(b)) if i%2]
    e = [c[i] for i in range(len(c)) if i%2]
    f = [c[i] for i in range((len(c))) if (i+1)%2]
    g = {}
    for j in range(len(e)):
        g[f[j][:6]] = e[j]
    county_dic[x] = g
    for i in d:
        county_html.append(i)

town_dic = {}

def abc(htmllist):
    dic = {}
    for i in htmllist:
        j = i[3:5]+'/'+i
        x = i[3:9]
        print(x,j)
        a = get_rslt(j)
        c = []
        for j in a:
            c.append(j[2])
        e = [c[i] for i in range(len(c)) if i%2]
        f = [c[i] for i in range((len(c))) if not i%2]
        g = {}
        for j in range(len(e)):
            g[f[j][:9]] = e[j]
        dic[x] = g
    return dic 

county_html1 = county_html[:500]
county_html2 = county_html[500:1000]
county_html3 = county_html[1000:1500]
county_html4 = county_html[1500:2000]
county_html5 = county_html[2000:2500]
county_html6 = county_html[2500:]

town1 = abc(county_html1)
town2 = abc(county_html2)
town3 = abc(county_html3)
town4 = abc(county_html4)
town5 = abc(county_html5)
town6 = abc(county_html6)
