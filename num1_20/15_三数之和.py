"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

def threeSum(nums):
    nums.sort()
    # print(nums)
    nums_len = len(nums)
    result = []
    if nums_len < 3:
        return result
    if nums[0] == nums[1] == nums[2] == 0:
        return [[0, 0, 0]]
    if nums[0] >= 0 or nums[nums_len - 1] <= 0:
        return result

    index = 0
    last_value = None
    while index < nums_len-2 and nums[index] <=0:
        # print("============================================")
        # print("第一步选择:", nums[index])

        if last_value == None or nums[index] != last_value:
            index2 = nums_len - 1
            flag = 0
            while index2 > index + 1 and flag == 0:
                sum_2 = nums[index] + nums[index2]
                # print("第二步选择：", nums[index2], "和为：", sum_2)
                if sum_2 >= 0 and sum_2 + nums[index] > 0:
                    # print("if1")
                    index2 = index2 - 1
                elif sum_2 >= 0 and sum_2 + nums[index] <= 0:
                    # print("if2")
                    # 从负数找
                    index3 = index + 1
                    while index3 < index2 and nums[index3] <= 0:
                        if nums[index3] + sum_2 == 0:
                            tmp_result = [nums[index], nums[index3], nums[index2]]
                            result.append(tmp_result)
                            flag = 1
                            break
                        if nums[index3] + sum_2 > 0:
                            break
                        index3 = index3 + 1
                    index2 = index2 - 1
                elif sum_2 < 0 and sum_2 + nums[index2] < 0:
                    # print("if3")
                    break
                elif sum_2 < 0 and sum_2 + nums[index2] >= 0:
                    # print("if4")
                    # 从正数找
                    index3 = index2 - 1
                    while index3 > index and nums[index3] >= 0:
                        if nums[index3] + sum_2 == 0:
                            tmp_result = [nums[index], nums[index3], nums[index2]]
                            result.append(tmp_result)
                            flag = 1
                            break
                        if nums[index3] + sum_2 < 0:
                            break
                        index3 = index3 - 1
                    index2 = index2 - 1
        last_value == nums[index]
        index = index + 1

    return result


if __name__ == '__main__':
    print(threeSum([-1, 0, 1, 2, -1, -4]))