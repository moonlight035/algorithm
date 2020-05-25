#查找最大子数组
import math


def max_across_sub_array(my_list,begin,medium,end):
    left = medium
    sum = tempSum = my_list[medium]
    leftList = list(range(begin,medium))
    leftList.reverse()
    for i in leftList:
        sum = sum+my_list[i]
        if sum>tempSum:
            tempSum = sum
            left = i
    right = medium + 1
    sum = tempSum = tempSum + my_list[medium+1]
    for j in range(medium+2,end+1):
        sum = sum + my_list[j]
        if sum > tempSum:
            tempSum = sum
            right = j
    return [left,right,tempSum]


def max_sub_array(my_list,begin,end):
    if begin==end:
        return [begin,end,my_list[begin]]
    else:
        q=math.floor((begin+end)/2)
        [leftBegin,leftEnd,leftSum] = max_sub_array(my_list,begin,q)
        [rightBegin,rightEnd,rightSum] = max_sub_array(my_list,q+1,end)
        [acrossBegin,acrossEnd,acrossSum] = max_across_sub_array(my_list,begin,q,end)
    if leftSum>=rightSum and leftSum>=acrossSum:
        return [leftBegin,leftEnd,leftSum]
    elif rightSum>=leftSum and rightSum>=acrossSum:
        return [rightBegin,rightEnd,rightSum]
    elif acrossSum>=leftSum and acrossSum>=rightSum:
        return [acrossBegin,acrossEnd,acrossSum]


def other_way(my_list):
    list_map = [None]*len(my_list)
    list_map[0] = (0,0,my_list[0],-1,0,0)
    for i in range(1,len(my_list)):
        [before_begin, before_end, before_sum, index, temp_sum, sum] = list_map[i - 1]
        sum = sum + my_list[i]
        temp_sum = temp_sum + my_list[i]
        if temp_sum < 0:
            temp_sum = 0
            index = -1
        elif index == -1:
            index = i
        if my_list[i]<0:
            list_map[i] = [before_begin, before_end, before_sum, index, temp_sum, sum]
            continue
        if temp_sum>=before_sum and temp_sum>=(before_sum+sum):
            list_map[i] = [index,i,temp_sum,-1,0,0]
        elif sum>=0:
            list_map[i] = [before_begin,i,sum+before_sum,-1,0,0]
        else:
            list_map[i] = [before_begin,before_end,before_sum,index,temp_sum,sum]
    return list_map[len(my_list)-1][0:3]

if __name__ == '__main__':
    a = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,0,-22,15,-4,7]
    print(max_sub_array(a, 0, len(a) - 1))
    print(other_way(a))
