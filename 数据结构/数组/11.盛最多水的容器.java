/*
 * @lc app=leetcode.cn id=11 lang=java
 *
 * [11] 盛最多水的容器
 */

// @lc code=start
class Solution {
    public int maxArea(int[] height) {
        int max = 0;
        for(int i = 0, j = height.length - 1; i < j ; ){
            int min_height = height[i] < height[j] ? height[i++] : height[j--];
            int area = (j - i + 1) * min_height;
            max = Math.max(max, area);
        }
        return max;
    }
}
// @lc code=end

