

# 재귀
def facto(n):
    if n <=1:
        return 1
    return n* facto(n-1)

print(facto(5))

#------------------------------
print('----------')

from collections import Counter

data = Counter("Hello world")
print(data)
print(data['o'])
# (출력)
# Counter({'l': 3, 'o': 2, 'H': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
# 2

data2 = Counter(['1', '2', '2', '3', '3', '3'])
print(data2)


#------------------------------
print('----------')
# DFS

graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

print(graph)