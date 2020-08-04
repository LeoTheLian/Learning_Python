# Uses python3
import sys

def fast_count_segments(starts, ends, points):
    cnt = {}
    all_points = [(s, 'left') for s in starts] 
    all_points += [(e, 'right') for e in ends] 
    all_points += [(p, 'point') for p in points]
    all_points.sort()
    count = 0
    
    for pos , kind in all_points:
        if kind == 'left':
            count += 1
        elif kind == 'right':
            count -= 1
        else:
            cnt[pos] = count

    return [cnt[p] for p in points]

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
