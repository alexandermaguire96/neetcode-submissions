class TimeMap:

    def __init__(self):
        
        self.dictionary = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        self.dictionary[key].append((timestamp, value))   
        print(self.dictionary)     

    def get(self, key: str, timestamp: int) -> str:
        
        low = 0
        high = len(self.dictionary[key]) -1

        while low <= high:

            mid = (low + high) // 2

            if self.dictionary[key][mid][0] <= timestamp:
                print(self.dictionary[key][mid][0])
                low = mid + 1

            elif self.dictionary[key][mid][0] > timestamp:
                high = mid - 1

        if high != -1:
            return self.dictionary[key][high][1] 
        else: return ""