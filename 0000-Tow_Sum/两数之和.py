# -*- coding: utf-8 -*-
# @Project : leetCode
# @Time    : 0510
# @Author  : Shylock
# @Email   : JYFelt@163.com
# @File    : 两数之和.py
# @Software: PyCharm
# ----------------------------------------------------
# import something

# 给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
#
# 你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
#
# 示例:
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

class Soluton:

    def twoSum(self, nums, target):
        """
        O(n**2)
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lens = len(nums)
        lyst = list()

        for i in range(lens):
            for j in range(lens - 1):
                target_ = nums[i] + nums[j]
                if i != j and target_ == target:
                    lyst.append(i)
                    lyst.append(j)
                    return lyst
        return

    def twoSum1(self, nums, target):
        """
        O(n)
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return [d[target - num], i]
            d[num] = i


if __name__ == '__main__':
    solution = Soluton()
    res = solution.twoSum1([3, 2, 4], 6)
    print(res)