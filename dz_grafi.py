#1 Номер
'''N, M = map(int, input().split())

rebra = []

for i in range(M):
    z , v = map(int, input().split())
    rebra.append((z, v))

print(f"Количество вершин: {N}")
print(f"Количество ребер: {M}")
print(f"Список ребер: {rebra}")'''

#2 Номер

'''N = 4
edge_list = [(1, 2), (2, 3), (3, 4), (4, 1), (1, 3)]

matrix = [[0] * N for i in range(N)]

for z, v in edge_list:
    matrix[z - 1][v - 1] = 1

for b in matrix:
    print(b)'''

#3 Номер
'''A = [
    [2, 3, 1],
    [3, 6, 2],
    [0, 4, 8]
]
B = [[0] * len(A) for _ in range(len(A))]

for i in range(len(A)):
    for j in range(len(A[i])):
        B[i][j] = A[j][i]

for line in B:
    print(*line)'''

#5 Номер
'''def read_edge_list():
    N = int(input())
    M = int(input())
    res = []
    for i in range(M):
        x, y = (int(x) for x in input().split())
        res.append((x, y))
    return N, res

def adj_list(N, edge_list):
    res = [[] for i in range(N)]

    for x, y in edge_list:
        res[x].append(y)
        res[y].append(x)

    return res

def dfs(curr_node, adj_list, visited=None):
    if visited is None:
        visited = set()

    print(f"Вошел: {curr_node}")
    visited.add(curr_node)

    for neighbor in adj_list[curr_node]:
        if neighbor not in visited:
            dfs(neighbor, adj_list, visited)

    print(f"Вышел: {curr_node}")

N, edges = read_edge_list()
graph = adj_list(N, edges)

visited = set()
for start_node in range(N):
    if start_node not in visited:
        dfs(start_node, graph, visited)'''
# 6
# 4
# 0 1
# 1 2
# 3 4
# 4 5
#

#6 Номер

'''def pelmen_ford(adj_list, start_node):

    N = max(max(edge[0], edge[1]) for edge in adj_list) + 1
    distance = [float("inf")] * N
    distance[start_node] = 0

    for i in range(N - 1):
        for z, o, v in adj_list:
            if distance[z] != float("inf") and distance[z] + v < distance[o]:
                distance[o] = distance[z] + v
    for z, o, v in adj_list:
        if distance[z] != float("inf") and distance[z] + v < distance[o]:
            print("ПОПАЛСЯ ОТРИЦАТЕЛЬНЫЙ ЦИКЛ")
            return None

    return distance


adj_list = [(0, 1, -1), (0, 2, 4), (1, 2, 3), (1, 3, 2), (1, 4, 2), (3, 2, 5), (3, 1, 1), (4, 3, -3)]

distance = pelmen_ford(adj_list, 0)

if distance:
    print("Кратчайшие расстояния от вершины 0:")
    for i, x in enumerate(distance):
        print(f"До вершины {i}: {x}")'''


#10 Номер Вопросики
'''В каких ситуациях вы предпочтете рекурсивную реализацию DFS итеративной и наоборот? 
Эффективно ли применение списка в качестве стэка в итеративной версии? 
Что насчет очереди в случае BFS?'''
# Рекурсивный проще в написании, но не подходит для больших графов, итеративный пишется сложнее, но работает на больших графах.
# Список эффективен, так как можно за О(1) вытащить элемент.
# Так как мы добавляем элемент по мере прохожденичя графа, то удобно будет добавлять их  очередь

