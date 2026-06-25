class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a,b=nums1,nums2
        total=len(nums1)+len(nums2)
        half=total//2
        if len(b)<len(a):
            a,b=b,a
        l,r=0,len(a)-1
        while True:
            ma=(l+r)//2
            mb=half-ma-2
            al=a[ma] if ma>=0 else float("-infinity")
            ar=a[ma+1] if (ma+1)< len(a) else float("infinity")
            bl=b[mb] if mb>=0 else float("-infinity")
            br=b[mb+1] if (mb+1)< len(b) else float("infinity")
            if al<=br and bl<=ar:
                if total%2:
                    return min(ar,br)
                return (max(al,bl)+min(ar,br))/2
            elif al>br:
                r=ma-1
            else:
                l=ma+1

