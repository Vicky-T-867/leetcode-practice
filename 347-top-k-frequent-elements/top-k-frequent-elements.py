class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = Counter(nums)

        heap = [] #place freq, items
        for num, freq in count.items():
            heapq.heappush(heap,(freq,num)) #adding new things on the top
            if len(heap)>k: #k is max storage, if storage full need to remove an item
                heapq.heappop(heap) #remove the lowest freq item
        return[num for freq, num in heap]
            

