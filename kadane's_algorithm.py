arr = [1,2,5,8,-44,5,6]

max_sum = arr[0]
cur_sum = 0

for x in arr:
    cur_sum=max(cur_sum,0)
    cur_sum+=x
    max_sum=max(max_sum,cur_sum)
        
print(max_sum)