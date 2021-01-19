import pandas as pd
import heapq
INF = int(1e9)

station_file = pd.read_excel('./SeoulMetro_StationSpacing(202003)_edit.xlsx')
transfer_station_file = pd.read_excel('./transit_station_distance.xlsx')
#print(station_file.head(3))
#print(station_file['역명'])
#print(station_file.loc[0])
#print(station_file.loc[0]['역명'])

dic = {}

dic[station_file.loc[0]['역명']+station_file.loc[0]['호선'][0]] = [INF, [
            [station_file.loc[1]['역명']+station_file.loc[1]['호선'][0], station_file.loc[1]['역간거리(km)']*1000]]]

for i in range(1, len(station_file)-1):
    if dic.get(station_file.loc[i]['역명']+station_file.loc[i]['호선'][0]):
        if station_file.loc[i]['역간거리(km)']!=0.0:
            dic[station_file.loc[i]['역명']+station_file.loc[i]['호선'][0]][1].append([station_file.loc[i-1]['역명']+station_file.loc[i-1]['호선'][0],station_file.loc[i]['역간거리(km)']*1000])
            dic[station_file.loc[i]['역명']+station_file.loc[i]['호선'][0]][1].append([station_file.loc[i+1]['역명']+station_file.loc[i+1]['호선'][0],station_file.loc[i+1]['역간거리(km)']*1000])
        elif station_file.loc[i]['호선'][0] != station_file.loc[i+1]['호선'][0]:
            dic[station_file.loc[i]['역명'] + station_file.loc[i]['호선'][0]][1].append(
                [station_file.loc[i - 1]['역명'] + station_file.loc[i - 1]['호선'][0],
                 station_file.loc[i]['역간거리(km)'] * 1000])
        else:
            dic[station_file.loc[i]['역명'] + station_file.loc[i]['호선'][0]][1].append(
                [station_file.loc[i + 1]['역명'] + station_file.loc[i + 1]['호선'][0],
                 station_file.loc[i + 1]['역간거리(km)'] * 1000])
    else:
        if station_file.loc[i]['역간거리(km)']==0.0:
            dic[station_file.loc[i]['역명'] + station_file.loc[i]['호선'][0]] = [INF, [
                [station_file.loc[i + 1]['역명'] + station_file.loc[i + 1]['호선'][0],
                 station_file.loc[i + 1]['역간거리(km)'] * 1000]]]
        elif station_file.loc[i]['호선'][0] != station_file.loc[i+1]['호선'][0]:
            dic[station_file.loc[i]['역명'] + station_file.loc[i]['호선'][0]] = [INF, [
                [station_file.loc[i - 1]['역명'] + station_file.loc[i - 1]['호선'][0],
                 station_file.loc[i]['역간거리(km)'] * 1000]]]
        else:
            dic[station_file.loc[i]['역명']+station_file.loc[i]['호선'][0]] = [INF, [
                [station_file.loc[i-1]['역명']+station_file.loc[i-1]['호선'][0],station_file.loc[i]['역간거리(km)']*1000],
                [station_file.loc[i+1]['역명']+station_file.loc[i+1]['호선'][0],station_file.loc[i+1]['역간거리(km)']*1000]]]

dic[station_file.loc[len(station_file)-1]['역명']+station_file.loc[len(station_file)-1]['호선'][0]] = [INF, [
    [station_file.loc[len(station_file) - 2]['역명']+station_file.loc[len(station_file) - 2]['호선'][0], station_file.loc[len(station_file)-1]['역간거리(km)']*1000]]]

for i in range(len(transfer_station_file)):
    if str(transfer_station_file.loc[i]['호선']) != 9 and str(transfer_station_file.loc[i]['환승노선'][0]).isdigit() and str(transfer_station_file.loc[i]['환승노선'][0]) != 9:
        transfer = str(transfer_station_file.loc[i]['환승역명']) + str(transfer_station_file.loc[i]['호선'])
        transfer_finish = str(transfer_station_file.loc[i]['환승역명']) + str(transfer_station_file.loc[i]['환승노선'][0])

        if transfer in dic and transfer_finish in dic:
            dic[transfer][1].append([transfer_finish, int(transfer_station_file.loc[i]['환승거리(m)'])*14])

print(dic)


start = input('시작역을 입력하세요 : ')
finish = input('도착역을 입력하세요 : ')

print(dic[start])

route = {}
def dijkstra(start):
    q =[]
    heapq.heappush(q, (0, start))
    dic[start][0] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dic[now][0] < dist:
            continue
            
        for i in dic[now][1]:
            cost = dist + i[1]
            if cost < dic[i[0]][0]:
                dic[i[0]][0] = cost
                print(i[0])
                print(dic[i[0]])
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

print(dic[finish][0])
