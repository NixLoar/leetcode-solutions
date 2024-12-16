# https://leetcode.com/problems/decompress-run-length-encoded-list/submissions/1430937124

def decompressRLElist(self, nums: List[int]) -> List[int]:
    decompressed = []

    for i in range(0, len(nums), 2):
        sublist = [nums[i + 1]] * nums[i]
        decompressed.append(sublist)
    
    result = []
    for sublist in decompressed:
        for num in sublist:
            result.append(num)
            
    return result