class RecentCounter:
    def getRequestCount(self, requests, start, end):
        # start = 2
        # end = 3002
        n = len(requests)

        i = 0
        while i <= n-1:
            if requests[i] >= start:
                break
            i += 1
        return n - i

    def __init__(self):
        self.count = 0
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        return self.getRequestCount(self.requests, t - 3000, t)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)