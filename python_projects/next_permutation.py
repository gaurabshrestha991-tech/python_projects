class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        n = len(nums)

        i = n - 2

        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
          
        if i >= 0:
            j = n - 1

            while nums[j] <= nums[i]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]

        left = i + 1
        right = n - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

if __name__ == "__main__":
    solution = Solution()

    nums1 = [1, 2, 3]
    solution.nextPermutation(nums1)
    print(nums1) 

    nums2 = [3, 2, 1]
    solution.nextPermutation(nums2)
    print(nums2)  

    nums3 = [1, 1, 5]
    solution.nextPermutation(nums3)
    print(nums3) 
