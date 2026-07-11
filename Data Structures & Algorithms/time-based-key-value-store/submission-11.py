class TimeMap:

    def __init__(self):
        self.keyStore = {}       

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        res,values = "",self.keyStore.get(key,[])
        l,r = 0,len(values)-1
        while l <= r:
            m = (r+l)//2
            if timestamp >= values[m][0]:
                res = values[m][1]
                l = m + 1
            else:
                r = m - 1
        return res
