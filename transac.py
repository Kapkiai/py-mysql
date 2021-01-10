#!/usr/bin/python3
# import json
# import dateutil.parser as dparser
# import re
# from datetime import datetime

# # with open('871919_-_RIVERSIDE_HOSTELS_SERVICES-2-page-1-table-1.json', 'r') as fd:
# #     data = json.load(fd)

# # j = data[9]['2']
# # # h = dparser.parse("14-12-2020 11:16:07 14-12-2020 11:16:07", fuzzy=True)
# # print(j)
# # match = re.search(r'\d{2}-\d{2}-\d{4} \d{2}:\d{2}:\d{2}', j)
# # print(match)
# # date = datetime.strptime(match.group(), '%d-%m-%Y %H:%M:%S')
# # print(date)

# v = "OKS4YB8H5Y 24-12-2020 09:00:59 24-12-2020 09:00:59 Pay Bill from 254790596961 -"

# r = re.search(r'^[A-Z0-9]*',v)
# # if r:
# print("dd", r)


# print(n)
# from docx import Document

# document = Document('871919 - RIVERSIDE HOSTELS SERVICES-2-converted.docx')
# tables = document.tables
# # print(type(tables[0].rows.cell))
# h = []


# r = {row.cells[0].paragraphs[0].text: val for (row, val) in zip(tables[0].columns, zip([row.cells[0].paragraphs[0].text for row in tables[0].rows]))}
# print(r)

import json
# g = ['name', 'age', 'class']
# t = ['Mathew', 'Vin']
# i = [20, 28]
# p = [9, 3]


# n = {x: list(j) for (x, j) in zip(g, zip(t, i))}
# h = [[row.cells[a].paragraphs[0].text for row in tables[1].columns]
#      for a in range(2)]
# for a in range(2):
# 	t = [row.cells[a].paragraphs[0].text for row in tables[0].columns]
# 	h.append(t)

# print(h, len(tables[0].rows))
# t =for row in tables[0].columns:
# 	print(row.cells[a].paragraphs[0].text)
# dic = {x: y for (x, y) in zip(h[0], zip(*h[1:]))}
# print(dic)
# with open('test.json', 'w') as fd:
# 	json.dump(dic, fd)

# a = [{1: "name", 2: "age"}, {1: "Mathew", 2: 30}]


# d = {}
# for k in a[0].keys():
#     d[k] = tuple(d[k] for d in a)

# print(d)
# tab = []

# for u in tables:
#     h = [[row.cells[a].paragraphs[0].text for row in u.columns]
#          for a in range(len(u.rows))]
#     dic = {x: list(y) for (x, y) in zip(h[0], zip(*h[1:]))}
#     keys = ['Receipt No.', 'Completion Time', 'Details', 'Paid In']
#     tab.append({key: dic[key] for key in dic if key in keys})


# print(tab[0])

# res = dict()
# for dict in tab:
#     for list in dict:
#         if list in res:
#             res[list] += (dict[list])
#         else:
#             res[list] = dict[list]

# print(res)


# v = {k: [d.get(k) for d in tab] for k in set().union(*tab)}
# print(v)
# pen = {}
# for k in tab[0].keys():
#     pen[k] = list(pen[k] for pen in tab)

# with open('test.json', 'w') as fd:
#     json.dump(res, fd)
# print(pen)

with open('test.json', 'r') as file:
	data = json.load(file)

print(len(data))

