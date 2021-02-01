import set_SubwayRoute
import queue
import sys

def SPFA(s_station, routing, station):
    _q = queue.Queue()
    _q.put(s_station)
    routing[s_station]['sDist'] = 0
    while not _q.empty():
        s = _q.get()
        inque[s] = False

        adj_list = list(station[s].keys())
        for i in range(len(adj_list)):
            spacingDist = routing[s]['sDist'] + station[s][adj_list[i]]
            n_station = adj_list[i]
            if routing[n_station]['sDist'] > spacingDist:
                routing[n_station]['sDist'] = spacingDist
                routing[n_station]['route'] = routing[s]['route'].copy()
                routing[n_station]['route'].append(n_station)
                if inque[n_station] is False:
                    _q.put(n_station)
                    inque[n_station] = True
    return routing


#실행문
#def main(station):
if __name__=="__main__":
    station = ''.join(sys.argv[1])
    departureLine, departure, destinationLine, destination = station.split("a")
    """
    departureLine = '1'
    departure = '시청'
    destinationLine = '4'
    destination = '동대문'
    """
    departure_station = departureLine + departure
    destination_station = destinationLine + destination

    station_dic, routing, inque = {}, {}, {}
    station_dic = set_SubwayRoute.main()

    for place in station_dic.keys():
        routing[place] = {'sDist': 1e9, 'route': []}
        inque[place] = False

    minRoute = SPFA(departure_station, routing, station_dic)

    final_route = minRoute[destination_station]['route']
    final_route = list(map(lambda x: x[1:], final_route))
    final_route.insert(0, departure)
    distance = str(minRoute[destination_station]['sDist'])
    transfer_station = []
    for i in range(1, len(final_route)):
        if final_route[i - 1] == final_route[i]:
            transfer_station.append(final_route[i - 1])
            final_route[i - 1] = final_route[i - 1] + "|환승|" + final_route[i]
            final_route[i] = ''
    while '' in final_route:
        final_route.remove('')
    route = ' > '.join(final_route)

    print(route + 'a' + distance + 'a' + ', '.join(transfer_station))
    #return route+'a'+time+'a'+transfer_station
