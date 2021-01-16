import pandas as pd

station_file = pd.read_excel('./distance_stations_202003.xlsx')
transfer_station_file = pd.read_excel('./transit_station_distance.xlsx')
print(station_file.head(3))
#print(station_file['역명'])
#print(station_file.loc[0])
#print(station_file.loc[0]['역명'])

dic = {}

dic[station_file.loc[0]['역명']] = [10000, [
            [station_file.loc[1]['역명'], station_file.loc[1]['호선'], station_file.loc[1]['역간거리(km)']]]]

for i in range(1, len(station_file)-1):
    if dic.get(station_file.loc[i]['역명']) and station_file.loc[i]['역간거리(km)']!=0.0:
        dic[station_file.loc[i]['역명']][1].append([station_file.loc[i-1]['역명'], station_file.loc[i-1]['호선'],station_file.loc[i]['역간거리(km)']])
        dic[station_file.loc[i]['역명']][1].append([station_file.loc[i+1]['역명'], station_file.loc[i+1]['호선'],station_file.loc[i+1]['역간거리(km)']])
    elif dic.get(station_file.loc[i]['역명']) and station_file.loc[i]['역간거리(km)'] == 0.0:
        dic[station_file.loc[i]['역명']][1].append(
            [station_file.loc[i + 1]['역명'], station_file.loc[i + 1]['호선'], station_file.loc[i + 1]['역간거리(km)']])
    elif station_file.loc[i]['역간거리(km)']==0.0:
        dic[station_file.loc[i]['역명']] = [10000, [
            [station_file.loc[i + 1]['역명'], station_file.loc[i + 1]['호선'], station_file.loc[i + 1]['역간거리(km)']]]]
    else:
        dic[station_file.loc[i]['역명']] = [10000, [
            [station_file.loc[i-1]['역명'], station_file.loc[i-1]['호선'],station_file.loc[i]['역간거리(km)']],
            [station_file.loc[i+1]['역명'], station_file.loc[i+1]['호선'],station_file.loc[i+1]['역간거리(km)']]]]

dic[station_file.loc[len(station_file)-1]['역명']] = [10000, [
    [station_file.loc[len(station_file) - 2]['역명'], station_file.loc[len(station_file) - 2]['호선'], station_file.loc[len(station_file)-1]['역간거리(km)']]]]


print(dic['서울역'])
"""
station = {
    '계양': [10000, [['부평구청', 노선번호,소요시간]]]
}
"""