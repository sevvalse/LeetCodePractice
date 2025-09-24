class Solution(object):
    def twoSum(self, nums, target):
        sol = []
        count_n = -1
        for n in nums:
            count_i = -1
            count_n += 1
            for i in nums:
                count_i += 1
                if not count_n == count_i:
                    if (n + i) == target:
                        sol.append(count_n)
                        sol.append(count_i)
                        return sol
        

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        