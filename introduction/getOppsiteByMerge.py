import sys
import math


def get(list,begin,medium,end):
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
            for m in range(k,len(left)-1):
                print(left[m],right[j])
            list[i]=right[j]
            j=j+1


def getOppsite(list,begin,end):
    if begin < end:
        q = math.floor((end+begin)/2)
        getOppsite(list,begin,q)
        getOppsite(list,q+1,end)
        get(list,begin,q,end)


if __name__ == '__main__' :
    a=[123,1,23,140,12,3,333]
    getOppsite(a,0,len(a)-1)
    print(a)