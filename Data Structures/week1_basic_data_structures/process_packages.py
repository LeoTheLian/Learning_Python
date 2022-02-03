# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def process(self, request):
        # empty requests that can be finished before the this one arrives
        while self.finish_time and self.finish_time[0] <= request.arrived_at:
            self.finish_time.pop(0)
        
        # when buffer is full 
        if len(self.finish_time) == self.size:
            return Response(True, -1)
        
        # check if there is unfinished request 
        if self.finish_time:
            t_start = self.finish_time[-1]
        else:
            t_start = request.arrived_at
        
        # schedule this request 
        self.finish_time.append(t_start + request.time_to_process)
        return Response(False, t_start)

def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
