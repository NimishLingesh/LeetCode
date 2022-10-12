class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[timestamp] = {key: value}

    def get(self, key: str, timestamp: int) -> str:
        if self.time_map.get(timestamp):
            if self.time_map[timestamp].get(key):
                return self.time_map[timestamp][key]
            else:
                return ""
        else:
            while(timestamp):
                timestamp -= 1
                if self.time_map.get(timestamp):
                    if self.time_map[timestamp].get(key):
                        return self.time_map[timestamp][key]
            return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)