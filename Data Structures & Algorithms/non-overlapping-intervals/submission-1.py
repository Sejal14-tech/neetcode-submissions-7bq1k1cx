class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        n = len(intervals)
        i=1
        start=0
        count=0
        while i<n:
            if intervals[start][-1]>intervals[i][0]:
                count+=1
                if intervals[start][-1]>intervals[i][-1]:
                    start = i
            else:
                start=i
            i+=1
        return count
        