from ast import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = []
        num1_len = len(nums1)
        num2_len = len(nums2)

        if num1_len > num2_len:
            
        elif num2_len > num1_len:

        elif num1_len == num2_len == 0:
            return []
        else:
        
    def mergeList(self, larg ,smol):
        for ele in range(0,len(larg)/2):
            
    def findMedian(combine_list):
        listLen = len(combine_list)
        if len(listLen) == 0:
            return None
        elif listLen % 2 == 1:
            return combine_list[(listLen-1)/2]
        else:
            return (combine_list[(listLen-2)/2]+combine_list[(listLen)/2])/2

if __name__ == "__main__":
    sol = Solution()
    l1 = [1,3]
    l2 = [2]
    l3 = [1,2]
    l4 = [3,4]
    sol.findMedianSortedArrays(l1,l2)