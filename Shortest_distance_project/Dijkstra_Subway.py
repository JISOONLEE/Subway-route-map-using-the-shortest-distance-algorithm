import pandas as pd
import heapq
import copy
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
    station_file = pd.read_excel('./SeoulMetro_StationSpacing(202003)_edit.xlsx')
    transfer_station_file = pd.read_excel('./transit_station_distance.xlsx')

    dic = data_station(station_file)
    dic = data_trasfer(dic, transfer_station_file)

    start = input('시작역을 입력하세요 : ')
    finish = input('도착역을 입력하세요 : ')

    dic, routing = dijkstra(dic, start, finish)
    routing[finish]['route'].append(finish)
    print('총 거리: ' + str(dic[finish][0]))
    print('경로: '+start+' -> '+finish)
    for i in routing[finish]['route']:
        print(i, end=' ')