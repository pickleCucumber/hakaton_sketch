'''все точки=[ ]
пока не х>=45
для каждого сотрудника ближайшая точка
пометить как пройденная везде'''
import heapq


priority={'Высокий':0.74, 'Средний':1, 'Низкий':1.25}

h=45
def dijkstra(graph, start) :
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    queue = [(0, start)]
    h = 45

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        # Обрабатываем только вершину с наименьшим расстоянием
        if current_distance > distances[current_vertex]:
            continue
        print(graph[current_vertex])
        for neighbor, weight in graph[current_vertex]:#.items():
            distance = current_distance + weight#заменить priority.values()

            # Рассматриваем этот новый путь только в том случае, если он лучше любого пути, который мы нашли до сих пор
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
        #nodes = nodes.remove(neighbor) удаляем нахуй пройденную точку из начального списка нод
        h=h-distance#-time_on_point
    return distances

 # тут надо доделать тип словарь для каждой начальной локации и присобачить как-нить чтобы время
'''graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'C': 2},
    'C': {'A': 3, 'B': 2}
}'''

nodes = ['ул. Российская, д. 418',"ул. им. Володи Головатого, д. 313",'ул. Красная, д. 145', 'ул. им. 40-летия Победы, д. 20/1', 'ул. им. Атарбекова, д. 24','ул. им. Героя Аверкиева А.А., д. 8',
'ул. им. Героя Аверкиева А.А., д. 8/1 к. мая, кв. 268','ул. им. Тургенева, д. 106','ул. Красных Партизан, д. 117','ул. Северная, д. 389']
'''''ул. Уральская, д. 166/3','ул. Северная, д. 524','ул. им. Кирилла Россинского, д. 61/1', 'ул. Коммунаров, д. 258',
'ул. им. Дзержинского, д. 100','ул. Северная, д. 326','ул. им. 40-летия Победы, д. 34',
'ул. Красная, д. 176','ул. Уральская, д. 79/1','ул. Северная, д. 326','ул. Красная, д. 149', 'ул. Целиноградская, д. 6/1',
'ул. им. Дзержинского, д. 100','ул. Российская, д. 418',"ул. им. Володи Головатого, д. 313",'ул. Красная, д. 145']'''
location=['ул. Российская, д. 418',"ул. им. Володи Головатого, д. 313",'ул. Красная, д. 145']
distances=[1, 5, 2.5, 4, 2, 1.5, 3, 2, 5, 3]


loc=dict(zip(nodes, distances))
graph = {}
for i in range(len(location)):
    print(location[i])
    print(loc)
    graph[location[i]].appent(loc)



print(graph)
#graph= {zip(location): loc}
while (len(nodes)!=0) or h<1: #крч для каждого сотрудника считаем ближайшую точку динамически и апдейтим начальную точку
    for i in graph.keys():
        print(dijkstra(graph, i))
#print(graph.keys())
#print(dijkstra(graph, i))
