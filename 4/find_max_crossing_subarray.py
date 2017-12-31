import math
def find_max_crossing_subarray(arr,low,mid,high):
    left_sum = float("-inf")
    sum = 0
    for i in range(mid,low-1,-1):
        sum = sum + arr[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = float("-inf")
    sum = 0
    for j in range(mid+1,high+1,1):
        sum = sum + arr[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return (max_left,max_right,left_sum+right_sum)

def find_maximum_subarray(arr,low,high):
    if high == low:
        return (low,high,arr[low])
    else:
        mid = math.floor((low+high)/2)
        (left_low,left_high,left_sum) = find_maximum_subarray(arr,low,mid)
        (right_low,right_high,right_sum) = find_maximum_subarray(arr,mid+1,high)
        (cross_low,cross_high,cross_sum) = find_max_crossing_subarray(arr,low,mid,high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low,left_high,left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low,right_high,right_sum)
        else:
            return (cross_low,cross_high,cross_sum)


# arr = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
# print(find_maximum_subarray(arr,0,15))