import pandas as pd
INF = int(1e9)
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

def createGraphData(station_file):
    graph = [[INF] * (len(station_file) + 2) for _ in range(len(station_file) + 2)]
    route = [[INF] * (len(station_file) + 2) for _ in range(len(station_file) + 2)]

    for i in range(1, len(station_file)+1):
        graph[0][i] = station_file.loc[i-1]['역명'] + station_file.loc[i-1]['호선'][0]
        graph[i][0] = station_file.loc[i-1]['역명'] + station_file.loc[i-1]['호선'][0]
        route[0][i] = station_file.loc[i - 1]['역명'] + station_file.loc[i - 1]['호선'][0]
        route[i][0] = station_file.loc[i - 1]['역명'] + station_file.loc[i - 1]['호선'][0]

    for a in range(1, len(station_file)+2):
        for b in range(1, len(station_file)+2):
            if a == b:
                graph[a][b] = 0
                route[a][b] = ''

    for i in range(len(station_file)):
        station = station_file.loc[i]['역명'] + station_file.loc[i]['호선'][0]
        if station_file.loc[i]['역간거리(km)'] == 0.0:
            next_station = station_file.loc[i + 1]['역명'] + station_file.loc[i + 1]['호선'][0]
            graph[graph[0].index(station)][graph[0].index(next_station)] = station_file.loc[i + 1]['역간거리(km)']*1000
        elif i == len(station_file)-1 or station_file.loc[i]['호선'][0]!=station_file.loc[i+1]['호선'][0]:
            pre_station = station_file.loc[i - 1]['역명'] + station_file.loc[i - 1]['호선'][0]
            graph[graph[0].index(station)][graph[0].index(pre_station)] = station_file.loc[i]['역간거리(km)']*1000
        else:
            next_station = station_file.loc[i+1]['역명'] + station_file.loc[i+1]['호선'][0]
            pre_station = station_file.loc[i-1]['역명'] + station_file.loc[i-1]['호선'][0]
            graph[graph[0].index(station)][graph[0].index(next_station)] = station_file.loc[i+1]['역간거리(km)']*1000
            graph[graph[0].index(station)][graph[0].index(pre_station)] = station_file.loc[i]['역간거리(km)']*1000
    return graph

def addTransferData(transfer_station_file, graph):
    for i in range(len(transfer_station_file)):
        if str(transfer_station_file.loc[i]['호선']) != 9 and str(transfer_station_file.loc[i]['환승노선'][0]).isdigit() \
                and str(transfer_station_file.loc[i]['환승노선'][0]) != 9:
            transfer = str(transfer_station_file.loc[i]['환승역명']) + str(transfer_station_file.loc[i]['호선'])
            transfer_finish = str(transfer_station_file.loc[i]['환승역명']) + str(transfer_station_file.loc[i]['환승노선'][0])

            if transfer in graph[0] and transfer_finish in graph[0]:
                graph[graph[0].index(transfer)][graph[0].index(transfer_finish)] = transfer_station_file.loc[i]['환승거리(m)']*14

    return graph

def Floydwarshall(size, graph):
    for k in range(1, size):
        for a in range(1, size):
            for b in range(1, size):
                graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
    return graph

if __name__ == '__main__':
    station_file = pd.read_excel('C:\\Users\\이지순\\PycharmProjects\\Shortest_distance_project\\SeoulMetro_StationSpacing(202003)_edit.xlsx')
    transfer_station_file = pd.read_excel('C:\\Users\\이지순\\PycharmProjects\\Shortest_distance_project\\transit_station_distance.xlsx')

    station_graph = createGraphData(station_file)
    trasfer_graph = addTransferData(transfer_station_file, station_graph)
    graph = Floydwarshall(len(station_file)+1, trasfer_graph)
    tmp = sys.argv[1]
    tmp = tmp.split('a')

    start = tmp[1] + tmp[0]
    finish = tmp[3] + tmp[2]

    result = start+" > "+finish+'a'+str(graph[graph[0].index(start)][graph[0].index(finish)])+"ma"+"환승역 정보 없음"
    print(result)