class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        left1, left2, right1, right2 = 0, 0, len1 - 1, len2 - 1

        # deal with case that either is empty (e.g. when dealing with even case). won't get both empty
        if len1 == 0:
            if len2 % 2 == 0:
                lowerMedian = (len2 - 2)/2
                upperMedian = len2/2
                return (nums2[lowerMeidan] + nums2[upperMedian])/2
            else:
                return num2[(len2 - 1)/2]
        elif len2 == 0:
            if len1 % 2 == 0:
                lowerMedian = (len1 - 2)/2
                upperMedian = len1/2
                return (nums1[lowerMeidan] + nums1[upperMedian])/2
            else:
                return num1[(len1 - 1)/2]

        # to deal with even length, run algorithm on odd \pm maxValue
        if (len1 + len2) % 2 == 0:
            maxValue = max(nums1[right1], nums2[right2])

            if nums1[right1] == maxValue:
                add = nums1.append(maxValue + 1)
                subtract = nums1.pop()

                lowerMedian = self.findMedianSortedArrays(add, nums2)
                upperMedian = self.findMedianSortedArrays(subtract, nums2)

                return (nums1[lowerMedian] + nums1[upperMedian])/2

            else:
                add = nums2.append(maxValue + 1)
                subtract = nums2.pop()

                lowerMedian = self.findMedianSortedArrays(nums1, add)
                upperMedian = self.findMedianSortedArrays(nums1, subtract)

                return (nums2[lowerMedian] + nums2[upperMedian])/2

                # ** IDEA **
            # by defn, median of array of length m+n is the value at index (m+n)/2
            # look at m//2 and n//2. suppose WLOG nums1[m//2] > nums2[n//2].
            # then, n+m/2 <= m//2 <= (m+n)/2 <= n/2 <= m + n/2,
            # where the first and last two inequalities are achieved by "direct concatenation",
            # and the second and third are achieved by "zig-zag"
            # this narrows the search space down by half

        else: # odd case, write code as in IDEA. In the odd case, the median is guaranteed to be an element in the list
            return 0




        