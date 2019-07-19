# encoding=utf8
"""通过list.index()方法"""
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 抛出的异常利用 try except来承接
        length = len(nums)
        for i in range(length):
            # 使用目标值减去列表值
            tmp = target - nums[i]
            # 使用列表的索引，如果找不到值会抛出异常
            try:
                # 控制其不等于本身
                if nums.index(tmp) != i:
                    return [i, nums.index(tmp)]
                    # 假设只有一种答案直接退出'''
                    break
            # 抛出的异常利用 try except来承接
            except:
                continue

if __name__ == '__main__':
    nums = [2, 5, 5, 11]
    target = 10
    solution = Solution()
    result = solution.twoSum(nums, target)
    print(result)
