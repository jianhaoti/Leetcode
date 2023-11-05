class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # need to deal with case that either is empty (e.g. when dealing with even case). never will both be empty
        if not nums1:
            len2 = len(nums2)

            if len2 % 2 == 0:
                lowerMedian = (len2 - 2)//2
                upperMedian = lowerMedian + 1
                return (nums2[loweMedian] + nums2[upperMedian])/2

            else:
                return nusm2[(len2 - 1)//2]

        elif not nums2:
            len1 = len(nums1)

            if len1 % 2 == 0:
                lowerMedian = (len1 - 2)//2
                upperMedian = lowerMedian + 1
                return (nums1[lowerMedian] + nums1[upperMedian])/2

            else:
                return num1[(len1 - 1)//2]

        # otherwise, both arrays nums1, nums2 are popoulated
        len1, len2 = len(nums1), len(nums2)
        left1, left2, right1, right2 = 0, 0, len1 - 1, len2 - 1

        # to deal with even length, run algorithm on odd \pm maxValue
        if (len1 + len2) % 2 == 0:
            maxValue = max(nums1[right1], nums2[right2])

            if nums1[right1] == maxValue:
                nums1.append(maxValue + 1)
                upperMedian = self.findMedianSortedArrays(nums1, nums2)
                lowerMedian = lowerMedian - 1

                nums1.pop()
                return (nums1[lowerMedian] + nums1[upperMedian])/2

            else: # even in the case maxValue are in both arrays, you only want to run this on one of them
                nums2.append(maxValue + 1)
                upperMedian = self.findMedianSortedArrays(nums1, nums2)
                lowerMedian = upperMedian - 1

                nums2.pop()
                return (nums2[lowerMedian] + nums2[upperMedian])/2

            # ** IDEA **
            # m = len1, n = len2
            # by defn, median of array of length m+n is the value at "index" (m+n)/2
            # look at m//2 and n//2. suppose WLOG nums1[m//2] > nums2[n//2].
            # then, n+m/2 <= m//2 <= (m+n)/2 <= n/2 <= m + n/2,
            # where the first and last two inequalities are achieved by "direct concatenation",
            # and the second and third are achieved by "zig-zag"
            # this narrows the search space down by half

            # for the equality case, you've found the median since the inequality m//2 <= (m+n)/2 <= n/2 becomes equality

        # odd case, write code as in IDEA. In the odd case, the median is guaranteed to be an element in the list
        # base case is when both element arrays are length 1
        else:
            #find the two mid values to compare. even/odd case separation
            if len1 % 2 == 0:
                lowerMid = (len1 - 2)//2
                upperMid = lowerMid + 1
                mid1 = (nums1[lowerMid] + nums1[upperMid])/2
            else:
                mid1 = nums1[(len1 - 1)//2]

            if len2 % 2 == 0:
                lowerMid = (len2 - 2)//2
                upperMid = lowerMid + 1
                mid2 = (nums2[lowerMid] + nums2[upperMid])/2
            else:
                mid2 = nums2[(len1 - 1)//2]

            #compare two values and continue search
            if mid1 > mid2:
                if len1 % 2 == 0 and len2 % 2 == 0:
                    self.findMedianSortedArrays(nums1[:lowerMid], nums2[upperMid:])
                elif len1 % 2 != 0 and len2 % 2 == 0:
                    self.findMedianSortedArrays(nums1[:mid1 + 1], nums2[upperMid:])
                elif len1 % 2 == 0 and len2 % 2 != 0:
                    self.findMedianSortedArrays(nums1[:upperMid])
                else:
                    self.findMedianSortedArrays(nums1[:mid1], nums2[mid2:])
            elif mid1 < mid2:
                return 1
            elif mid1 == mid2:
                return mid1




        