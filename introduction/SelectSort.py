#选择算法
def select_sort(my_list):
    for i in range(len(my_list)-1):
        min = my_list[i]
        index = i
        for j in range(i+1,len(my_list)):
            if my_list[j] < min:
                min = my_list[j]
                index = j
        my_list[index] = my_list[i]
        my_list[i] = min

if __name__ == '__main__' :
    a=[123,1,23,123,12,3,12]
    select_sort(a)
    print(a)