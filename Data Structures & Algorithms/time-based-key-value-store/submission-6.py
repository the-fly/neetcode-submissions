class TimeMap:

    key_to_timestamped_values_map = {}
    def __init__(self):
        self.key_to_timestamped_values_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        timestamped_values = self.key_to_timestamped_values_map.setdefault(key, [])
        timestamped_values.append((timestamp, value))
        # prev_index = self._find_prev_index(timestamped_values, timestamp, 0, len(timestamped_values)-1)
        # timestamped_values.insert(prev_index+1, (timestamp, value))
        # print ("set", self.key_to_timestamped_values_map, timestamp)
        
    def get(self, key: str, timestamp: int) -> str:
        timestamped_values = self.key_to_timestamped_values_map.get(key, [])
        prev_index = self._find_prev_index(timestamped_values, timestamp, 0, len(timestamped_values)-1)
        # print ("get", self.key_to_timestamped_values_map, timestamp)

        if prev_index == -1:
            return ""
        return timestamped_values[prev_index][1]


    def _find_prev_index(self, timestamped_values: [(int, str)], target:int, i: int, j: int ):
        # print(timestamped_values, target, i, j)
        if i>j:
            return -1
        if j-i<=1:
            if timestamped_values[j][0] <= target:
                return j
            if i == j-1 and timestamped_values[i][0] <= target:
                return i
            return -1
        
        mid = i + (j-i) // 2

        if timestamped_values[mid][0] == target:
            return mid

        # print(1, timestamped_values[mid][0], target, i, j, mid)
        if timestamped_values[mid][0] > target:
            return self._find_prev_index(timestamped_values, target, i, mid-1)
        return self._find_prev_index(timestamped_values, target, mid, j)

        
