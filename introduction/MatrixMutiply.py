# 矩阵相乘
import math
import numpy


def merge_matrix(matrix_a,matrix_b):
    matrix_result = numpy.zeros((len(matrix_a),len(matrix_a))).tolist()
    for i in range(0,len(matrix_a)):
        for j in range(0,len(matrix_a)):
            matrix_result[i][j] = matrix_a[i][j] + matrix_b[i][j]
    return matrix_result


def del_matrix(matrix_a,matrix_b):
    matrix_result = numpy.zeros((len(matrix_a),len(matrix_a))).tolist()
    for i in range(0,len(matrix_a)):
        for j in range(0,len(matrix_a)):
            matrix_result[i][j] = matrix_a[i][j] - matrix_b[i][j]
    return matrix_result


# T(n) = 8T(n/2)+n*n
def matrix_multiply(matrix_a,matrix_b,a_beside,b_beside):
    if a_beside[0]==a_beside[1]:
        return [[matrix_a[a_beside[0]][a_beside[2]]*matrix_b[b_beside[0]][b_beside[2]]]]
    a_x = math.floor((a_beside[0] + a_beside[1]) / 2)
    a_y = math.floor((a_beside[2] + a_beside[3]) / 2)
    b_x = math.floor((b_beside[0] + b_beside[1]) / 2)
    b_y = math.floor((b_beside[2] + b_beside[3]) / 2)
    matrix_left_top = merge_matrix(matrix_multiply(matrix_a,matrix_b,[a_beside[0],a_x,a_beside[2],a_y],[b_beside[0],b_x,b_beside[2],b_y])
                                   ,matrix_multiply(matrix_a,matrix_b,[a_beside[0],a_x,a_y+1,a_beside[3]],[b_x+1,b_beside[1],b_beside[2],b_y]))
    matrix_right_top = merge_matrix(matrix_multiply(matrix_a, matrix_b, [a_beside[0], a_x, a_beside[2], a_y], [b_beside[0],b_x,b_y+1,b_beside[3]])
                                    ,matrix_multiply(matrix_a, matrix_b, [a_beside[0],a_x,a_y+1,a_beside[3]],[b_x+1,b_beside[1],b_y+1,b_beside[3]]))
    matrix_left_bottom = merge_matrix(matrix_multiply(matrix_a,matrix_b,[a_x+1,a_beside[1],a_beside[2],a_y],[b_beside[0],b_x,b_beside[2],b_y])
                                   ,matrix_multiply(matrix_a,matrix_b,[a_x+1,a_beside[1],a_y+1,a_beside[3]],[b_x+1,b_beside[1],b_beside[2],b_y]))
    matrix_right_bottom = merge_matrix(matrix_multiply(matrix_a,matrix_b,[a_x+1,a_beside[1],a_beside[2],a_y],[b_beside[0],b_x,b_y+1,b_beside[3]])
                                   ,matrix_multiply(matrix_a,matrix_b,[a_x+1,a_beside[1],a_y+1,a_beside[3]],[b_x+1,b_beside[1],b_y+1,b_beside[3]]))
    for i in range(0,len(matrix_left_top)):
        matrix_left_top[i].extend(matrix_right_top[i])
    for i in range(0,len(matrix_left_bottom)):
        matrix_left_bottom[i].extend(matrix_right_bottom[i])
    matrix_left_top.extend(matrix_left_bottom)
    return matrix_left_top


if __name__ == '__main__':
    a=[[1,3,4,5],[12,345,34,5],[56,345,34,5],[34,32,3,12]]
    b=[[456,456,45,6],[45,64,56,456],[67,67,6,7],[1,2,12,1]]
    matrix_result = matrix_multiply(a, b, [0,len(a)-1,0,len(a[0])-1],[0,len(b)-1,0,len(b[0])-1])
    for i in matrix_result:
        print(i)