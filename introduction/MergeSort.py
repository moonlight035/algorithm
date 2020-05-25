#归并排序
import sys
import math

def merge(list,begin,medium,end):
    left = list[begin:medium+1]
    right = list[medium+1:end+1]
    left.append(sys.maxsize)
    right.append(sys.maxsize)
    k=0
    j=0
    for i in range(begin,end+1):
       if(left[k]<right[j]):
            list[i]=left[k]
            k=k+1
       else:
            list[i]=right[j]
            j=j+1


def merge_sort(list,begin,end):
    if begin < end:
        q = math.floor((end+begin)/2)
        merge_sort(list,begin,q)
        merge_sort(list,q+1,end)
        merge(list,begin,q,end)


if __name__ == '__main__' :
    a=[123,1,23,123,12,3,12]
    merge_sort(a,0,len(a)-1)
    print(a)
