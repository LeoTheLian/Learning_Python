# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    if tank > distance:
        return 0 # no need for refill

    current_station = 0
    refill = 0
    s = 0
    n = len(stops)
    stops.append(distance)
    stops.insert(0, 0)
    while current_station <= n:
        last_station = current_station
        while current_station <= n and stops[current_station + 1] - stops[last_station] <= tank:
            current_station += 1
        if current_station == last_station:
            return -1
        if current_station <= n:
            refill += 1
    return refill

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
