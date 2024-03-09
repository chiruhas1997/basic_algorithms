#find largest sum of subarray with largest sum
arr = [1,2,5,8,-44,5,6]

def kadanes_algo(arr):
    max_sum = arr[0]
    cur_sum = 0

    for x in arr:
        cur_sum=max(cur_sum,0)
        cur_sum+=x
        max_sum=max(max_sum,cur_sum)
        return max_sum

def silding_window(arr):
    max_sum = arr[0]
    cur_sum = 0
    max_l, max_r = 0,0
    L=0

    for R in range(len(arr)):
        if cur_sum<0:
            cur_sum = 0
            L=R
        cur_sum+=arr[R]

        if max_sum<cur_sum:
            max_sum=cur_sum
            max_l,max_r= L,R
        return max_l,max_r