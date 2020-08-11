# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    segments_sorted = sorted(segments, key = lambda x: x.end)
    points = []

    while segments_sorted:
        current_segment = segments_sorted.pop(0)
        current_point = current_segment.end
        points.append(current_point)
    
        for s in segments_sorted[:]:
            if s.start <= current_point <= s.end:
                segments_sorted.remove(s)
    
    return points
    #write your code here
    

if __name__ == '__main__':
    n = sys.stdin.read().split()
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(n[::2], n[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points) 