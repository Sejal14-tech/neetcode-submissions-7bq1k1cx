class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = {}
        for i in range(len(hand)):
            count[hand[i]]=count.get(hand[i],0)+1
        sortcards = sorted(count.keys())
        print(sortcards,count)
        for i in sortcards:
            if count[i]>0:
                times = count[i]
                for j in range(groupSize):
                    if count.get(i+j,0)<times:
                        return False
                    count[i+j]-=times
        return True
