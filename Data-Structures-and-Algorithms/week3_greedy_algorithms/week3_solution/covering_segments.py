# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    #write your code here
    n = segments[0].start
    W = segments[0].end
    
    return [n, W, len(segments)]

if __name__ == '__main__':
    n = sys.stdin.read().split()
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(n[::2], n[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
