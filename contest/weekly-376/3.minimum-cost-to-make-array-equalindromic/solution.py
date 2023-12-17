# Created by Jones at 2023/12/17 14:14
# leetgo: dev
# https://leetcode.cn/problems/minimum-cost-to-make-array-equalindromic/
# https://leetcode.cn/contest/weekly-contest-376/problems/minimum-cost-to-make-array-equalindromic/

from typing import *
from leetgo_py import *

from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop, heapreplace
from itertools import accumulate, chain, count, pairwise, zip_longest
from math import ceil, comb, floor, gcd, inf, isqrt, log2, perm, sqrt
from operator import xor
from string import ascii_lowercase
from typing import List, Optional

# @lc code=begin
# from sortedcontainers import SortedList


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        nums.sort()

        p = list(accumulate(nums, initial=0))
        n = len(nums)
        res = inf
        flg = False

        for left in range(10 ** (len(str(nums[-1])) // 2 + 1)):
            if flg:
                break
            tmp = left
            x = left
            while tmp:
                x = x * 10 + tmp % 10
                tmp //= 10

            def cal(x):
                i = bisect_left(nums, x)  # a[i] >= x
                return x * (i) - p[i] + (p[-1] - p[i] - (n - i) * x)

            # print(x, cal(x))

            res = min(res, cal(x))
            if x > nums[-1] and res != inf:
                flg = True
            if left < 10**4:
                for mid in range(10):
                    x = left * 10 + mid
                    tmp = left
                    while tmp:
                        x = x * 10 + tmp % 10
                        tmp //= 10

                    # print(x, cal(x))
                    res = min(res, cal(x))

        return res


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumCost(nums)

    print("\noutput:", serialize(ans))