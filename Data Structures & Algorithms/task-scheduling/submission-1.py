class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxFreq = 0
        taskFreq = [0]*26
        maxFreqTaskNum = 0
        for task in tasks:
            i = ord(task) - ord('A')
            taskFreq[i] += 1
            if taskFreq[i] > maxFreq:
                maxFreq = taskFreq[i]
                maxFreqTaskNum = 1
            elif taskFreq[i] == maxFreq:
                maxFreqTaskNum += 1

        return max(len(tasks), (n+1)*(maxFreq - 1) + maxFreqTaskNum)
        