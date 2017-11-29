import pprint
import heapq
from queue import Queue
pp = pprint.PrettyPrinter(indent=4)
a = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

matrix = []
alist = a.split("\n")
for line in alist:
    matrix.append(line.split(" "))
g = {}
print(matrix)
for row_num,row in enumerate(matrix):
    print("row is {}".format(row))
    for item_num,item in enumerate(row):
        adj_list = []
        node = "{}_{}_{}".format(row_num,item_num,item)
        #if row_num + 1 < len(matrix) and item_num -1 >= 0 :
        #    left = "{}_{}_{}".format(row_num+1,item_num-1,matrix[row_num+1][item_num-1])
        #    adj_list.append(left)
        if row_num + 1 < len(matrix):
            middle = "{}_{}_{}".format(row_num+1,item_num,matrix[row_num+1][item_num])
            adj_list.append(middle)
        if row_num + 1 < len(matrix): 
            right = "{}_{}_{}".format(row_num+1,item_num+1,matrix[row_num+1][item_num+1])
            adj_list.append(right)
        g[node] = adj_list
        print("node is {} and adj_list is {}".format(node,adj_list))
#pp.pprint(g)
dist = {}
prev = {}
for node in g : 
    dist[node] = -1 
    prev[node] = None
dist["0_0_75"] = 75
q = []
q.append("0_0_75")
count = 0 
while len(q) > 0:
    item = q.pop(0)
    count = count + 1 
    print("item removed is {} len of queue is {} q is {}  ".format(item,len(q),q))
    item_val = int(item.split("_")[-1])
    for node in g[item]:
        if node not in q: 
            q.append(node)
        adj_node_val = int(node.split("_")[-1])
        print("dist[item] is {} adj_node_val is {}".format(dist[item],adj_node_val))
        if dist[item] + adj_node_val > dist[node]:
            dist[node] = dist[item] + adj_node_val
            print("setting dist[node] as {}".format(dist[node]))
       
pp.pprint(dist)
print(max(dist.values()))
