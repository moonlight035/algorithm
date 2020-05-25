#插入排序
def insert_sort(my_list):
    for i in range(1,len(my_list)):
        temp = my_list[i]
        j = i-1
        while j>=0:
            if my_list[j]>temp:
                my_list[j+1]=my_list[j]
            else:
                break
            j=j-1
        my_list[j+1]=temp

if __name__ == '__main__' :
    a=[123,1,23,123,12,3,12]
    insert_sort(a)
    print(a)