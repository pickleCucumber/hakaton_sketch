
import heapq
import pandas as pd
from pprint import pprint

priority={'Высокий':0.74, 'Средний':1, 'Низкий':1.25}

all_point=[]
h=45
def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    queue = [(0, start)]
    a=999999
    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        # Обрабатываем только вершину с наименьшим расстоянием
        try:
            for neighbor, weight in graph[current_vertex].items():
                distance = current_distance + weight
                #print(distance)
                #print(neighbor)

                # Рассматриваем этот новый путь только в том случае, если он лучше любого пути, который мы нашли до сих пор
                if distance < a:
                    best_point = neighbor
                    a = distance
                    heapq.heappush(queue, (distance, neighbor))
        except KeyError:
            break
    return best_point, a


nodes = ['ул. Уральская, д. 79/1','ул. Северная, д. 524','ул. им. Кирилла Россинского, д. 61/1','ул. им. 40-летия Победы, д. 20/1', 'ул. им. Атарбекова, д. 24','ул. им. Героя Аверкиева А.А., д. 8',
'ул. им. Героя Аверкиева А.А., д. 8/1 к. мая, кв. 268','ул. им. Тургенева, д. 106','ул. Красных Партизан, д. 117','ул. Северная, д. 389']
''''ул. Уральская, д. 166/3','ул. Северная, д. 524','ул. им. Кирилла Россинского, д. 61/1', 'ул. Коммунаров, д. 258',
'ул. им. Дзержинского, д. 100','ул. Северная, д. 326','ул. им. 40-летия Победы, д. 34',
'ул. Красная, д. 176','ул. Уральская, д. 79/1','ул. Северная, д. 326','ул. Красная, д. 149', 'ул. Целиноградская, д. 6/1',
'ул. им. Дзержинского, д. 100','ул. Российская, д. 418',"ул. им. Володи Головатого, д. 313",'ул. Красная, д. 145']'''
location=['ул. Российская, д. 418',"ул. им. Володи Головатого, д. 313",'ул. Красная, д. 145']
distances=[1, 5, 2.5, 4, 2, 1.5, 3, 2, 5, 3]

loc=dict(zip(nodes, distances))
graph = {}
for i in range(len(location)):
    graph[location[i]]=loc

df=pd.DataFrame(columns=['best_point'])
df1=pd.DataFrame(columns=['time'])
df1.fillna('0')
# #надо добавить крч если нескольким сотрудникам одинаковая точка проставилась, то надо посчитать до следующей и назначить тому, у кого меньше времени уйдет
ix=0
j=1
k=1
try:
  while len(nodes)>0:
    j=j+1
    

    for i in graph.keys():
      best_point=i
      p=int(df1.loc[df1.index==i].sum().values)
      print(p)
      print(len(nodes))

      if df1.at[i, k]<9:
        best_point, time=dijkstra(graph, best_point)
        df.at[i, j]=best_point
        df1.at[i, k] =df1.loc[i]+time#+time_task #вот как сюда время выполнения таски добавить, пока хз
        #nodes.remove(df.at[i, j]) #= [x for x in nodes if x not in df.loc[:,df.columns == j]]
      else:  #вот тут сбрасывается до начальной ноды, по идеи
        k=k+1
        best_point=i
        best_point, time=dijkstra(graph, best_point)
        df.at[i, j]=best_point
        df1.at[i, k] =df1.loc[i]+time
      nodes.remove(df.at[i, j])
      loc=dict(zip(nodes, distances))
      graph = {}
      for i in range(len(location)):
          graph[location[i]]=loc
except UnboundLocalError:
  pass


    
