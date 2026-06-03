class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        #set nums1 as the smaller sized array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        #search space on the smaller array
        l, r = 0, m-1
        #number of elements on left side
        half = (m+n) // 2

        # Finde ends of left array on nums1 and nums2
        while True:
            #middle point of search space
            i = (l+r) // 2
            j = half - (i+1) -1

            Aleft = nums1[i] if i>=0 else float('-inf')
            Aright = nums1[i+1] if i+1<m else float('inf')
            Bleft = nums2[j] if j>=0 else float('-inf')
            Bright = nums2[j+1] if j+1<n else float('inf')

            if (Aleft <= Bright and Bleft <= Aright):
                if (m+n) % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright))/2
                return min(Aright, Bright)
            
            if Aleft > Bright:
                r = i-1
            else:
                l = i+1
        