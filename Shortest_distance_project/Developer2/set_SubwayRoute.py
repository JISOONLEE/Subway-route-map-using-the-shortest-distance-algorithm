import pandas as pd

#기본역에 이전역, 다음역 가중치를 추가하여 지하철 노선도 그래프 생성(Dictionary)
def setDefaultRoute(station_dic, file_station):
    for i in range(0, len(file_station)):
        station = file_station.loc[i]
        file_size = len(file_station)
        #첫역/마지막 역이 아닌 경우
        if i != file_size-1 and station['누계(km)'] != 0 and file_station.loc[i+1]['누계(km)'] != 0:
            # 같은 호선일 경우 이전역 설정
            if station['호선'] == file_station.loc[i - 1]['호선']:
                previous_station = file_station.loc[i - 1]
                previous_name = previous_station['호선'][:1] + previous_station['역명']
            # 같은 호선일 경우 다음역 설정
            if station['호선'] == file_station.loc[i + 1]['호선']:
                next_station = file_station.loc[i + 1]
                next_name = next_station['호선'][:1] + next_station['역명']
        #첫역인 경우
        elif i != file_size-1 and station['누계(km)'] == 0:
            # 같은 호선일 경우 다음역 설정
            if station['호선'] == file_station.loc[i + 1]['호선']:
                next_station = file_station.loc[i + 1]
                next_name = next_station['호선'][:1] + next_station['역명']
        #마지막 역인 경우
        elif i == file_size-1 or file_station.loc[i+1]['누계(km)'] != 0:
            # 같은 호선일 경우 이전역 설정
            if station['호선'] == file_station.loc[i - 1]['호선']:
                previous_station = file_station.loc[i - 1]
                previous_name = previous_station['호선'][:1] + previous_station['역명']

        station_name = station['호선'][:1]+station['역명']

        if i!= file_size-1:
            #해당 역이 역딕셔너리 키 값이 아니고, 호선의 첫역/마지막역이 아닐때 (==>누계가 0km가 아닐 때)
            if station_name not in station_dic.keys() and station['누계(km)'] != 0:
                station_dic[station_name] = {previous_name : int(station['역간거리(km)']*1000)}
                station_dic[station_name][next_name] = int(next_station['역간거리(km)']*1000)
            #해당 역이 역딕셔너리 키 값이 아니고, 호선의 첫역일 때
            elif station_name not in station_dic.keys() and station['누계(km)'] == 0:
                station_dic[station_name] = {next_name: int(next_station['역간거리(km)']*1000)}
            #해당 역이 역 딕셔너리 키 값이 아니고, 호선의 마지막 역일 때
            elif station_name not in station_dic.keys() and file_station.loc[i+1]['누계(km)'] == 0:
                station_dic[station_name] = {previous_name: int(station['역간거리(km)']*1000)}
        else:
            station_dic[station_name] = {previous_name: int(station['역간거리(km)']*1000)}

    return station_dic

def setTransferRoute(station_dic, file_transfer):
    for i in range(len(file_transfer)):
        transfer_station = file_transfer.loc[i]
        station_name = str(transfer_station['호선'])+str(transfer_station['환승역명'])
        transfer_line = transfer_station['환승노선'][0]
        if transfer_line.isdigit() and int(transfer_line) != 9 and int(transfer_station['호선']) != 9:
            transfer_name = str(transfer_line)+str(transfer_station['환승역명'])
        else:
            continue

        if station_name in station_dic and transfer_name in station_dic:
            station_dic[station_name][transfer_name] = int(transfer_station['환승거리(m)'])
            station_dic[transfer_name][station_name] = int(transfer_station['환승거리(m)'])

    return station_dic


def main():
    station_dictionary = {}
    file_station = pd.read_excel(
        "User's STS workspace Path" + "\\MetroRoute\\src\\main\\resources\\static\\SeoulMetro_StationSpacing.xlsx")
    file_transfer = pd.read_excel(
        "User's STS workspace Path" + "\\MetroRoute\\src\\main\\resources\\static\\SeoulMetro_TransferStation_Distance_and_NecessaryTime.xlsx")

    station_dictionary = setDefaultRoute(station_dictionary, file_station)
    station_dictionary = setTransferRoute(station_dictionary, file_transfer)

#    for i in station_dictionary:
#        print(i, station_dictionary[i])

    return station_dictionary




