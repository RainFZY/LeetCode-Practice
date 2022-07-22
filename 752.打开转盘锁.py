#
# @lc app=leetcode.cn id=752 lang=python3
#
# [752] 打开转盘锁
#

# https://leetcode.cn/problems/open-the-lock/solution/by-huan-huan-20-f37j/
# @lc code=start
# 双向BFS
# 传统的BFS是从起点向周围层层扩散，遇到终点时停止（本题是到target时停止），
# 而双向BFS是从起点和终点同时扩散，当二者有交集时停止

# set版，python set用hash table实现，相比list更省时间
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        """双向BFS"""
        if target == '0000':
            return 0
        '''在上拨、下拨数字的地方可以优化为字符串切片、拼接 不需要再写新的函数'''
        step = 0 # 记录拨动次数
        # 由于是否停止是根据两个方向扩散的是否存在交集，所以采用集合而非list，
        # 使得判断更高效（遍历时间O(n) vs O(1)）
        q1, q2, visited = set(), set(), set() 
        visited.update(deadends) # 存放已经处理过的组合、死亡组合
        
        # q1从起点扩散q2从终点扩散
        q1.add('0000')
        q2.add(target)

        while q1 and q2:
            # 在遍历的时候q1和q2不能修改 所以增加temp存放扩散结果
            temp = set()

            for cur in q1:
                # 集合无序 所以只能全部遍历 遇到不合法的（在visited中的）就跳过
                if cur in visited:
                    continue
                # 结束条件：q1和q2有交集
                if cur in q2:
                    return step
                # 已经处理过的节点要加入到visited
                visited.add(cur)
                # 扩散到相邻的节点
                for j in range(4):
                    # 上拨 合法节点加入扩散结果temp
                    up = cur[:j] + str((int(cur[j])+1) % 10) + cur[j+1:]
                    if up not in visited:
                        temp.add(up)
                    # 下拨 合法节点加入扩散结果temp
                    down = cur[:j] + str((int(cur[j])-1) % 10) + cur[j+1:]
                    if down not in visited:
                        temp.add(down)
            # 一次循环结束 增加次数
            step += 1
            # 交换扩撒（如上一次是从q1扩散的 这次从q2扩散 从哪开始扩散temp记录的就是谁的扩散结果）
            q1 = q2
            q2 = temp
        # 全部穷举了还没有交集 说明没有解 返回-1
        return -1


# list版
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        """双向BFS"""
        if target == '0000':
            return 0
        '''在上拨、下拨数字的地方可以优化为字符串切片、拼接 不需要再写新的函数'''
        step = 0 # 记录拨动次数

        q1, q2, visited = [], [], []
        visited.extend(deadends) # 存放已经处理过的组合、死亡组合
        
        # q1从起点扩散q2从终点扩散
        q1.append('0000')
        q2.append(target)

        while q1 and q2:
            # 在遍历的时候q1和q2不能修改 所以增加temp存放扩散结果
            temp = []

            for cur in q1:
                # 集合无序 所以只能全部遍历 遇到不合法的（在visited中的）就跳过
                if cur in visited:
                    continue
                # 结束条件：q1和q2有交集
                if cur in q2:
                    return step
                # 已经处理过的节点要加入到visited
                visited.append(cur)
                # 扩散到相邻的节点
                for j in range(4):
                    # 上拨 合法节点加入扩散结果temp
                    up = cur[:j] + str((int(cur[j])+1) % 10) + cur[j+1:]
                    if up not in visited:
                        temp.append(up)
                    # 下拨 合法节点加入扩散结果temp
                    down = cur[:j] + str((int(cur[j])-1) % 10) + cur[j+1:]
                    if down not in visited:
                        temp.append(down)
            # 一次循环结束 增加次数
            step += 1
            # 交换扩撒（如上一次是从q1扩散的 这次从q2扩散 从哪开始扩散temp记录的就是谁的扩散结果）
            q1 = q2
            q2 = temp
        # 全部穷举了还没有交集 说明没有解 返回-1
        return -1

# @lc code=end

