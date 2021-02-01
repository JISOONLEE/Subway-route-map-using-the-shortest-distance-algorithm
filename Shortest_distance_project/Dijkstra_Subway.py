import pandas as pd
import heapq
import copy
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
INF = int(1e9)

def data_station(station_file):
    dic = {}
    for i in range(0, len(station_file)):
        station_name = station_file.loc[i]['역명']+station_file.loc[i]['호선'][0]
        if dic.get(station_name): # 딕셔너리 안에 키 값 있을 경우
            if station_file.loc[i]['역간거리(km)'] == 0.0: # 호선의 시작역일때
                dic[station_name][1].append(
                    [station_file.loc[i + 1]['역명'] + station_file.loc[i + 1]['호선'][0],
                     station_file.loc[i + 1]['역간거리(km)'] * 1000])
            elif i != len(station_file) - 1 and station_file.loc[i]['호선'][0] != station_file.loc[i+1]['호선'][0]: # 호선의 마지막역일때, 맨 마지막역을 뺀 나머지
                dic[station_name][1].append(
                    [station_file.loc[i - 1]['역명'] + station_file.loc[i - 1]['호선'][0],
                     station_file.loc[i]['역간거리(km)'] * 1000])
            elif i == len(station_file) - 1: #마지막역일때
                dic[station_name][1].append(
                    [station_file.loc[i - 1]['역명'] + station_file.loc[i - 1]['호선'][0],
                     station_file.loc[i]['역간거리(km)'] * 1000])
            else:
                dic[station_name][1].append(
                    [station_file.loc[i - 1]['역명'] + station_file.loc[i - 1]['호선'][0],
                     station_file.loc[i]['역간거리(km)'] * 1000])
                dic[station_name][1].append(
                    [station_file.loc[i + 1]['역명'] + station_file.loc[i + 1]['호선'][0],
                     station_file.loc[i + 1]['역간거리(km)'] * 1000])
        else: # 딕셔너리 안에 키 값 없을 경우
            if station_file.loc[i]['역간거리(km)'] == 0.0: # 호선의 시작역일때
                dic[station_name] = [INF, [
                    [station_file.loc[i + 1]['역명'] + station_file.loc[i + 1]['호선'][0],
                     station_file.loc[i + 1]['역간거리(km)'] * 1000]]]
            elif i != len(station_file)-1 and station_file.loc[i]['호선'][0] != station_file.loc[i+1]['호선'][0]:# 호선의 마지막역일때, 맨 마지막역을 뺀 나머지
                dic[station_name] = [INF, [
                    [station_file.loc[i - 1]['역명'] + station_file.loc[i - 1]['호선'][0],
                     station_file.loc[i]['역간거리(km)'] * 1000]]]
            elif i == len(station_file)-1:  #마지막역일때
                dic[station_name] = [INF, [
                    [station_file.loc[i - 1]['역명'] + station_file.loc[i - 1]['호선'][0],
                     station_file.loc[i]['역간거리(km)'] * 1000]]]
            else:
                dic[station_name] = [INF, [
                    [station_file.loc[i-1]['역명']+station_file.loc[i-1]['호선'][0],station_file.loc[i]['역간거리(km)']*1000],
                    [station_file.loc[i+1]['역명']+station_file.loc[i+1]['호선'][0],station_file.loc[i+1]['역간거리(km)']*1000]]]

    return dic

def data_trasfer(dic, transfer_station_file):
    for i in range(len(transfer_station_file)):
        transfer_data = transfer_station_file.loc[i]
        if str(transfer_data['호선']) != 9 and str(transfer_data['환승노선'][0]).isdigit() and str(transfer_data['환승노선'][0]) != 9:
            transfer = str(transfer_data['환승역명']) + str(transfer_data['호선'])
            transfer_finish = str(transfer_data['환승역명']) + str(transfer_data['환승노선'][0])

            if transfer in dic and transfer_finish in dic:
                dic[transfer][1].append([transfer_finish, int(transfer_data['환승거리(m)'])*14])
    return dic


def dijkstra(dic, start, finish):
    q =[]
    heapq.heappush(q, (0, start))
    dic[start][0] = 0

    routing = {} # 경로 담기 위한 딕셔너리
    for place in dic.keys():
        routing[place] = {'route': []}

    while q:
        dist, now = heapq.heappop(q)
        if dic[now][0] < dist:
            continue

        for i in dic[now][1]:
            cost = dist + i[1]
            if cost < dic[i[0]][0] or not routing[now]['route']:
                dic[i[0]][0] = cost
                routing[i[0]]['route'] = copy.deepcopy(routing[now]['route'])
                routing[i[0]]['route'].append(now)
                heapq.heappush(q, (cost, i[0]))
    return dic, routing

if __name__ == '__main__':
    station_file = pd.read_excel('C:\\Users\\이지순\\PycharmProjects\\Shortest_distance_project\\SeoulMetro_StationSpacing(202003)_edit.xlsx')
    transfer_station_file = pd.read_excel('C:\\Users\\이지순\\PycharmProjects\\Shortest_distance_project\\transit_station_distance.xlsx')

    dic = data_station(station_file)
    dic = data_trasfer(dic, transfer_station_file)

    tmp = sys.argv[1]
    tmp = tmp.split('a')

    start = tmp[1]+tmp[0]
    finish = tmp[3]+tmp[2]

    dic, routing = dijkstra(dic, start, finish)
    routing[finish]['route'].append(finish)
    route_list = []
    line = ''
    transfer = ''
    route = ''

    for i in routing[finish]['route']:
        route_list.append(i[:-1])
        line += i[-1]

    for i in range(len(route_list)):
        if i+1 < len(route_list) and route_list[i] == route_list[i+1]:
            route += route_list[i]+'[환승]'
            transfer += route_list[i]+ ", "
        elif i == (len(route_list)-1):
            route += route_list[i]
        else:
            route += route_list[i]+' > '

    transfer = transfer[:-2]
    if transfer is None:
        transfer = "환승역 정보 없음"

    result = str(route + "a"+str(dic[finish][0])+"m"+"a"+transfer)
    print(result)