# encoding=utf8
# 题目大意 #
# 在数组中找到 2 个数之和等于给定值的数字，结果返回 2 个数字在数组中的下标。

# 解题思路 #
# 顺序扫描数组，对每一个元素，在 map 中找能组合给定值的另一半数字，
# 如果找到了，直接返回 2 个数字的下标即可。
# 如果找不到，就把这个数字存入 map 中，等待扫到“另一半”数字的时候，再取出来返回结果。
class Solution:
    def twoSum(self, nums, target):

        m = {}
        length = len(nums)
        for i in range(length):
            tmp =target - nums[i]
            if str(tmp) in m:
                return [m[str(tmp)],i]
            m[str(nums[i])]=i
        return None

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    result = solution.twoSum(nums, target)
    print(result)
