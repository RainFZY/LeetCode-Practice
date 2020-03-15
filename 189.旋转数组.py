#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # 法一
        # n = len(nums)
        # k = k % n
        # nums[:] = nums[-k:] + nums[:-k]

        # 法二，先反转整个数组，再分别反转两个部分的数
        n = len(nums)
        k %= n
        nums[:] = nums[::-1] # 反转
        nums[:k] = nums[:k][::-1]
        #print(nums)
        nums[k:] = nums[k:][::-1]
        #print(nums)



# @lc code=end

