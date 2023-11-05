class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # deal with case that either is empty (e.g. when dealing with even case). won't get both empty
        if not nums1:
            len2 = len(nums2)

            if len2 % 2 == 0:
                lowerMedian = (len2 - 2)//2
                upperMedian = len2//2
                return (nums2[lowerMedian] + nums2[upperMedian])/2

            else:
                return nums2[(len2 - 1)//2]

        elif not nums2:
            len1 = len(nums1)

            if len1 % 2 == 0:
                lowerMedian = (len1 - 2)//2
                upperMedian = len1//2
                return (nums1[lowerMedian] + nums1[upperMedian])/2

            else:
                return nums1[(len1 - 1)//2]

        #otherwise, both arrays nums1, nums2 are popoulated
        len1, len2 = len(nums1), len(nums2)
        left1, left2, right1, right2 = 0, 0, len1 - 1, len2 - 1

        # to deal with even length, run algorithm on odd \pm maxValue
        if (len1 + len2) % 2 == 0:
            maxValue = max(nums1[right1], nums2[right2])

            if nums1[right1] == maxValue:
                nums1.append(maxValue + 1)
                lowerMedianValue = self.findMedianSortedArrays(nums1, nums2)

                nums1.pop() # pop out maxValue + 1
                nums1.pop() # pop out maxValue
                upperMedianValue = self.findMedianSortedArrays(nums1, nums2)

                return (lowerMedianValue + upperMedianValue)/2

            else:
                nums2.append(maxValue + 1)
                lowerMedianValue = self.findMedianSortedArrays(nums1, nums2)

                nums2.pop() # pop out maxValue + 1
                nums2.pop() # pop out maxValue
                upperMedianValue = self.findMedianSortedArrays(nums1, nums2)

                return (lowerMedianValue + upperMedianValue)/2

        # ** IDEA **
        # m = len1, n = len2
        # by defn, median of array of length m+n is the value at "index" (m+n)/2
        # look at m//2 and n//2. suppose WLOG nums1[m//2] >= nums2[n//2]. (if equality, we're done by chain below)
        # then, n+m/2 <= m//2 <= (m+n)/2 <= n/2 <= m + n/2,
        # where the first and last two inequalities are sharp by "direct concatenation" (e.g. 12||34),
        # and the second and third are sharp by "zig-zag" (e.g. 13 || 24)

        # In the odd case, the median is guaranteed to be an element in the list
        # base case is when both element arrays are length 1
        else:
            if len(nums1) > 1 or len(nums2) > 1:
                #find the two mid values to compare. even/odd case separation
                if len1 % 2 == 0:
                    lowerMid1 = (len1 - 2)//2
                    upperMid1 = lowerMid1 + 1
                    mid1 = (nums1[lowerMid1] + nums1[upperMid1])/2
                else:
                    mid1 = nums1[(len1 - 1)//2]

                if len2 % 2 == 0:
                    lowerMid2 = (len2 - 2)//2
                    upperMid2 = lowerMid2 + 1
                    mid2 = (nums2[lowerMid2] + nums2[upperMid2])/2
                else:
                    mid2 = nums2[(len2 - 1)//2]

                #compare two values and continue search
                if mid1 > mid2:
                    if len1 % 2 == 0 and len2 % 2 == 0:
                        return self.findMedianSortedArrays(nums1[:upperMid1], nums2[upperMid2:])
                    elif len1 % 2 != 0 and len2 % 2 == 0:
                        return self.findMedianSortedArrays(nums1[:mid1 + 1], nums2[upperMid2:])
                    elif len1 % 2 == 0 and len2 % 2 != 0:
                        return self.findMedianSortedArrays(nums1[:upperMid1], nums2[mid2:])
                    elif len1 % 2 != 0 and len2 % 2 != 0:
                        return self.findMedianSortedArrays(nums1[:mid1 + 1], nums2[mid2:])
                if mid1 < mid2:
                    if len1 % 2 == 0 and len2 % 2 == 0:
                        return self.findMedianSortedArrays(nums1[upperMid:], nums2[:upperMid2])
                    elif len1 % 2 != 0 and len2 % 2 == 0:
                        return self.findMedianSortedArrays(nums1[mid1:], nums2[:upperMid2])
                    elif len1 % 2 == 0 and len2 % 2 != 0:
                        return self.findMedianSortedArrays(nums1[:upperMid1], nums2[:mid2 + 1])
                    elif len1 % 2 != 0 and len2 % 2 != 0:
                        return self.findMedianSortedArrays(nums1[mid1:], nums2[:mid2 + 1])
                elif mid1 == mid2:
                    return mid1
            else: #not written correctly yet, need to think about which one of the two to return
                return nums1[0]



