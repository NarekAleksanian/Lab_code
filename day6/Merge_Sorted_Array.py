class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = 0
        j = 0

        while i < len(nums1) or j < len(nums2):
            if i >= m:
                del nums1[i]
                continue
            if i >= n:
                del nums2[i]
                continue
            i += 1
            j += 1

        nums1 = sorted(nums1 + nums2)
        return nums1
