class Solution:
    def findMedianSortedArrays(self, nums1, nums2) :
        arr = []
        l, r = 0, 0
        while (l < len(nums1) and r < len(nums2)):
            if nums1[l] < nums2[r]:
                arr.append(nums1[l])
                l += 1
            else:
                arr.append(nums2[r])
                r += 1
        if l < len(nums1):
            arr.extend(nums1[l:])
        else:
            arr.extend(nums2[r:])
        midi = len(arr) // 2
        if len(arr) % 2 != 0:
            return float(f"{arr[midi]:.5f}")
        else:
            print(arr)
            stri = (arr[midi] + arr[midi-1]) / 2
            return float(f"{stri:.5f}")


obj=Solution()
print(obj.findMedianSortedArrays([1,2],[3,4]))