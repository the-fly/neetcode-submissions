class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxFreq = 0
        taskFreq = {}
        maxFreqTaskNum = 0
        for task in tasks:
            taskFreq[task] = taskFreq.get(task, 0) + 1
            if taskFreq[task] > maxFreq:
                maxFreq = taskFreq[task]
                maxFreqTaskNum = 1
            elif taskFreq[task] == maxFreq:
                maxFreqTaskNum += 1

        return max(len(tasks), (n+1)*(maxFreq - 1) + maxFreqTaskNum)
        