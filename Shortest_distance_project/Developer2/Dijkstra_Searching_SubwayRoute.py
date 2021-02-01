import set_SubwayRoute
import queue
import sys

def Dijkstra(s_station, routing, station):
    _q = queue.PriorityQueue()
    _q.put((0, s_station))
    routing[s_station]['sDist'] = 0
    while not _q.empty():
        q_item = _q.get()
        s = q_item[1]
        dist = q_item[0]

        if routing[s]['sDist'] < dist:
            continue

        for i in station[s]:
            spacingDist = dist + station[s][i]
            if routing[i]['sDist'] > spacingDist:
                routing[i]['sDist'] = spacingDist
                routing[i]['route'] = routing[s]['route'].copy()
                routing[i]['route'].append(i)
                _q.put((spacingDist, i))

    return routing


#실행문
#def main(argv):
if __name__=="__main__":
    station = ''.join(sys.argv[1])
    departureLine, departure, destinationLine, destination = station.split("a")
    """
    departureLine = '4'
    departure = '서울'
    destinationLine = '6'
    destination = '이태원'
    """
    departure_station = departureLine + departure
    destination_station = destinationLine + destination

    station_dic, routing = {}, {}
    station_dic = set_SubwayRoute.main()

    for place in station_dic.keys():
        routing[place] = {'sDist': 1e9, 'route': []}

    minRoute = Dijkstra(departure_station, routing, station_dic)

    final_route = minRoute[destination_station]['route']
    final_route = list(map(lambda x: x[1:], final_route))
    final_route.insert(0, departure)
    distance = str(minRoute[destination_station]['sDist'])
    transfer_station = []
    for i in range(1, len(final_route)):
        if final_route[i - 1] == final_route[i]:
            transfer_station.append(final_route[i - 1])
            final_route[i-1] = final_route[i - 1] + "|환승|" + final_route[i]
            final_route[i] = ''
    while '' in final_route:
        final_route.remove('')
    route = ' > '.join(final_route)

    print(route+'a'+distance+'a'+', '.join(transfer_station))
    #return route+'a'+time+'a'+transfer_station
