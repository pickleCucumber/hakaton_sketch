import sys

h=45
priority={'Высокий':0.74, 'Средний':1, 'Низкий':1.25}

class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)

    def construct_graph(self, nodes, init_graph):
        '''
        Этот метод обеспечивает симметричность графика. Другими словами, если существует путь от узла A к B со значением V, должен быть путь от узла B к узлу A со значением V.
        '''
        graph = {}
        for node in nodes:
            graph[node] = {}

        graph.update(init_graph)

        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value

        return graph

    def get_nodes(self):
        "Возвращает узлы графа"
        return self.nodes

    def get_outgoing_edges(self, node):
        "Возвращает соседей узла"
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections

    def value(self, node1, node2):
        "Возвращает значение ребра между двумя узлами"
        return self.graph[node1][node2]


def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())

    # посещении каждого узла и обновлять его по мере продвижения по графику
    shortest_path = {}

    # dict, чтобы сохранить кратчайший известный путь к найденному узлу
    previous_nodes = {}

    # max_value для инициализации значения "бесконечности" непосещенных узлов
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # инициализируем значение начального узла 0
    shortest_path[start_node] = 0

    # алгоритм выполняется до тех пор, пока мы не посетим все узлы
    while unvisited_nodes:
        # узел с наименьшей оценкой
        current_min_node = None
        for node in unvisited_nodes:  # Iterate over the nodes
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        #соседей текущего узла и обновляет их расстояния
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if (tentative_value<(shortest_path[neighbor]))&(tentative_value<h): #|shortest_path[neighbor]==9223372036854775807):
                print('1', tentative_value)
                shortest_path[neighbor] = tentative_value
                # также апдейтим лучший путь к текщей ноде
                previous_nodes[neighbor] = current_min_node
                print('2', tentative_value)

        # после посещения его соседей мы отмечаем узел как "посещенный"
        unvisited_nodes.remove(current_min_node)

    return previous_nodes, shortest_path


def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node

    while node != start_node:
        path.append(node)
        node = previous_nodes[node]

    # добавить начальный узел вручную
    path.append(start_node)

    print("Найден следующий лучший маршрут  {}.".format(shortest_path[target_node]))
    print(" -> ".join(reversed(path)))

sort_list=[]

nodes = ['ул. им. 40-летия Победы, д. 20/1', 'ул. им. Атарбекова, д. 24','ул. им. Героя Аверкиева А.А., д. 8',
'ул. им. Героя Аверкиева А.А., д. 8/1 к. мая, кв. 268','ул. им. Тургенева, д. 106','ул. Красных Партизан, д. 117','ул. Северная, д. 389',
'ул. Уральская, д. 166/3','ул. Северная, д. 524','ул. им. Кирилла Россинского, д. 61/1', 'ул. Коммунаров, д. 258',
'ул. им. Дзержинского, д. 100','ул. Северная, д. 326','ул. им. 40-летия Победы, д. 34',
'ул. Красная, д. 176','ул. Уральская, д. 79/1','ул. Северная, д. 326','ул. Красная, д. 149', 'ул. Целиноградская, д. 6/1',
'ул. им. Дзержинского, д. 100','ул. Российская, д. 418',"ул. им. Володи Головатого, д. 313",'ул. Красная, д. 145']
sort_list=nodes
'''''''''
staff_point=[]  #i-ого сотрудника
sort_list=nodes#отсортированные по важности и условиям задачи
nodes=staff_point.append(sort_list)   #точки сотрудников




'''''''''''
init_graph = {}#получаем хуй за щеку с апи
for node in nodes:
    init_graph[node] = {}

init_graph["ул. им. 40-летия Победы, д. 20/1"]["ул. им. Атарбекова, д. 24"] = 0.5#*priority.values #путь* коэффициент важности  (мб + время выполнения)
init_graph["ул. им. 40-летия Победы, д. 20/1"]["ул. им. Героя Аверкиева А.А., д. 8"] = 1.5#*priority.values
init_graph['ул. им. Героя Аверкиева А.А., д. 8']["ул. им. Атарбекова, д. 24"] = 1#*priority.values
init_graph['ул. им. Героя Аверкиева А.А., д. 8']["ул. Северная, д. 326"] = 3#*priority.values
init_graph["ул. им. Атарбекова, д. 24"]["ул. Северная, д. 326"] = 5#*priority.values
init_graph["ул. Северная, д. 326"]["ул. Российская, д. 418"] = 4#*priority.values
init_graph["ул. Северная, д. 326"]["ул. Уральская, д. 79/1"] = 1#*priority.values
init_graph["ул. Красная, д. 176"]["ул. Северная, д. 326"] = 2#*priority.values
init_graph["ул. Красная, д. 176"]["ул. Красная, д. 145"] = 2#*priority.values

graph = Graph(nodes, init_graph)

previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node="ул. им. 40-летия Победы, д. 20/1")

print_result(previous_nodes, shortest_path, start_node="ул. им. 40-летия Победы, д. 20/1", target_node="ул. Красная, д. 145")
#о мб добавить веса в путь
