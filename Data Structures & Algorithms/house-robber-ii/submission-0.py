class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums, default=0)
        arr = [[x, False] for x in nums]
        arr[0] = [arr[0][0], True]
        arr[2] = [arr[0][0] + arr[2][0], True]
        for i in range(3, len(arr)-1):
            x = arr[i-3]
            y = arr[i-2]
            if x[0] > y[0]:
                maximum = x[0]
                arr[i][1] = x[1]
            elif y[0] > x[0]:
                maximum = y[0]
                arr[i][1] = y[1]
            arr[i][0] += maximum
        if arr[-4][1] == True:
            if arr[-1][0] > arr[0][0]:
                n = arr[-1][0] + arr[-4][0] - arr[0][0]
            else:
                n = arr[-4][0]
        else:
            n = arr[-1][0] + arr[-4][0]
        if arr[-3][1] == True:
            if arr[-1][0] > arr[0][0]:
                m = arr[-1][0] + arr[-3][0] - arr[0][0]
            else:
                m = arr[-3][0]
        else:
            m = arr[-1][0] + arr[-3][0]
        arr[-1][0] = max(n, m)
        return max(arr[-1][0], arr[-2][0])