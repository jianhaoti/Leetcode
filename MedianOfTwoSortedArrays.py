class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # thinking of bSearching both, then taking the higher one and bSorting the lower
        # array to find out exactly where that one slots in overall. do until you get to end.
        # is this fast enough?

        m, n = len(nums1), len(nums2)
        left1, left2, right1, right2 = 0, 0, m - 1, n - 1


        return 0

