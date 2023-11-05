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
        left1, left2, right1, right2 = 0, 0, len(nums1) - 1, len(nums2) - 1

        # to deal with even length, run algorithm on odd \pm maxValue
        if (len1+len2) %2 == 0:
            maxValue = max(nums1[right1], nums2[right2])

            if nums1[right1] == maxValue:
                nums1.append(maxValue + 1)
                lowerMedianValue = self.handleOdd(nums1, nums2)
                print("LowerMedianValue for nums1:", lowerMedianValue)

                nums1.pop() # pop out maxValue + 1
                nums1.pop() # pop out maxValue
                upperMedianValue = self.handleOdd(nums1, nums2)
                print("UpperMedianValue for nums1:", upperMedianValue)

                return (lowerMedianValue + upperMedianValue)/2

            else:
                print("Before appending:", nums2)
                nums2.append(maxValue + 1)
                print("After appending:", nums2)
                lowerMedianValue = self.handleOdd(nums1, nums2)
                print("LowerMedianValue for nums2:", lowerMedianValue)

                nums2.pop() # pop out maxValue + 1
                nums2.pop() # pop out maxValue
                upperMedianValue = self.handleOdd(nums1, nums2)
                print("UpperMedianValue for nums2:", upperMedianValue)

                return (lowerMedianValue + upperMedianValue)/2

        else:
            return self.handleOdd(nums1, nums2)

    # ** IDEA **
    # m = len1, n = len2
    # by defn, median of array of length m+n is the value at "index" (m+n)/2
    # look at m//2 and n//2. suppose WLOG nums1[m//2] >= nums2[n//2]. (if equality, we're done by chain below)
    # then, n+m/2 <= m//2 <= (m+n)/2 <= n/2 <= m + n/2,
    # where the first and last two inequalities are sharp by "direct concatenation" (e.g. 12||34),
    # and the second and third are sharp by "zig-zag" (e.g. 13 || 24)

    # In the odd case, the median is guaranteed to be an element in the list
    # DON'T WRITE AS A RECURSIVE ALGO. CANNOT PRESERVE SUM = ODD!

    def handleOdd(self, nums1, nums2) -> int:
        left1, left2, right1, right2 = 0, 0, len(nums1) - 1, len(nums2) - 1
        len1 = right1 - left1 + 1
        len2 = right2 - left2 + 1

        while (len1 != 1 and len2 == 2) or (len2 != 1 and len1 == 2):
            #find the two mid values to compare. even/odd separation
            len1 = right1 - left1 + 1
            len2 = right2 - left2 + 1

            if len1 % 2 == 0:
                upperMid1 = len1//2
                lowerMid1 = upperMid1 - 1
                mid1Value = (nums1[lowerMid1] + nums1[upperMid1])/2

            else:
                mid1 = (len1 - 1)//2
                mid1Value = nums1[mid1]

            if len2 % 2 == 0:
                upperMid2 = len2//2
                lowerMid2 = upperMid2 - 1
                mid2Value = (nums2[lowerMid2] + nums2[upperMid2])/2

            else:
                mid2 = (len2 - 1)//2
                mid2Value = nums2[mid2]

            #compare two values and continue search
            if mid1Value > mid2Value:
                if len1 % 2 == 0 and len2 % 2 == 0: # E E
                    right1 = lowerMid1
                    left2 = upperMid2

                elif len1 % 2 != 0 and len2 % 2 == 0: # O E
                    right1 = mid1
                    left2 = upperMid2

                elif len1 % 2 == 0 and len2 % 2 != 0: # E O
                    right1 = lowerMid1
                    left2 = mid2

                elif len1 % 2 != 0 and len2 % 2 != 0: # O O
                    right1 = mid1
                    left2 = mid2

            if mid1Value < mid2Value:
                if len1 % 2 == 0 and len2 % 2 == 0: # E E
                    left1 = upperMid1
                    right2 = lowerMid2

                elif len1 % 2 != 0 and len2 % 2 == 0: # O E
                    left1 = mid1
                    right2 = lowerMid2

                elif len1 % 2 == 0 and len2 % 2 != 0: # E O
                    left1 = upperMid1
                    right2 = mid2

                elif len1 % 2 != 0 and len2 % 2 != 0: # O O
                    left1 = mid1
                    right2 = mid2

            else: #if we've found median early
                return nums1[mid1]

        # now in base case of 1 + 2 or 2 + 1
        if len1 == 1 and len2 == 2:
            arr = [nums1[left1], nums2[left2], nums2[right2]]
            arr = sorted(arr)
            return arr[1]
        else:
            arr = [nums2[left2], nums1[left1], nums1[right1]]
            arr = sorted(arr)
            return arr[1]




