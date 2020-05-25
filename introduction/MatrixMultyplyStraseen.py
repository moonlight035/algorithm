import numpy
import math


def add_matrix(matrix_a,matrix_b,a_beside,b_beside):
    matrix_left = [matrix_a[i][a_beside[2]:a_beside[3] + 1] for i in range(a_beside[0],a_beside[1]+1)]
    matrix_right = [matrix_b[i][b_beside[2]:b_beside[3] + 1] for i in range(b_beside[0], b_beside[1] + 1)]
    matrix_result = numpy.zeros((len(matrix_left), len(matrix_left[0]))).tolist()
    for i in range(0,len(matrix_left)):
        for j in range(0,len(matrix_left[0])):
            matrix_result[i][j] = matrix_left[i][j] + matrix_right[i][j]
    return matrix_result


def add_all_matrix(matrix_a,matrix_b):
    matrix_result = numpy.zeros((len(matrix_a),len(matrix_a))).tolist()
    for i in range(0,len(matrix_a)):
        for j in range(0,len(matrix_a)):
            matrix_result[i][j] = matrix_a[i][j] + matrix_b[i][j]
    return matrix_result


def del_matrix(matrix_a, matrix_b, a_beside, b_beside):
    matrix_left = [matrix_a[i][a_beside[2]:a_beside[3] + 1] for i in range(a_beside[0],a_beside[1] + 1)]
    matrix_right = [matrix_b[i][b_beside[2]:b_beside[3] + 1] for i in range(b_beside[0], b_beside[1] + 1)]
    matrix_result = numpy.zeros((len(matrix_left), len(matrix_left[0]))).tolist()
    for i in range(0,len(matrix_left)):
        for j in range(0,len(matrix_left[0])):
            matrix_result[i][j] = matrix_left[i][j] - matrix_right[i][j]
    return matrix_result


def del_all_matrix(matrix_a,matrix_b):
    matrix_result = numpy.zeros((len(matrix_a),len(matrix_a))).tolist()
    for i in range(0,len(matrix_a)):
        for j in range(0,len(matrix_a)):
            matrix_result[i][j] = matrix_a[i][j] - matrix_b[i][j]
    return matrix_result


def matrix_multiply(matrix_a,matrix_b,a_beside,b_beside):
    if a_beside[0]==a_beside[1]:
        return [[sum([matrix_a[a_beside[0]][i]*matrix_b[j][b_beside[2]] for i, j in zip(range(a_beside[2],a_beside[3]+1),range(b_beside[0],b_beside[1]+1))])]]
    a_x = math.floor((a_beside[0] + a_beside[1]) / 2)
    a_y = math.floor((a_beside[2] + a_beside[3]) / 2)
    b_x = math.floor((b_beside[0] + b_beside[1]) / 2)
    b_y = math.floor((b_beside[2] + b_beside[3]) / 2)
    # B12-B22
    matrix_s1 = del_matrix(matrix_b,matrix_b,[b_beside[0],b_x,b_y+1,b_beside[3]],[b_x+1,b_beside[1],b_y+1,b_beside[3]])
    # A11+A12
    matrix_s2 = add_matrix(matrix_a,matrix_a,[a_beside[0],a_x,a_beside[2],a_y],[a_beside[0],a_x,a_y+1,a_beside[3]])
    # A21+A22
    matrix_s3 = add_matrix(matrix_a,matrix_a,[a_x+1,a_beside[1],a_beside[2],a_y],[a_x+1,a_beside[1],a_y+1,a_beside[3]])
    # B21-B11
    matrix_s4 = del_matrix(matrix_b,matrix_b,[b_x+1,b_beside[1],b_beside[2],b_y],[b_beside[0],b_x,b_beside[2],b_y])
    # A11+A22
    matrix_s5 = add_matrix(matrix_a,matrix_a,[a_beside[0],a_x,a_beside[2],a_y],[a_x+1,a_beside[1],a_y+1,a_beside[3]])
    # B11+B22
    matrix_s6 = add_matrix(matrix_b,matrix_b,[b_beside[0],b_x,b_beside[2],b_y],[b_x+1,b_beside[1],b_y+1,b_beside[3]])
    # A12-A22
    matrix_s7 = del_matrix(matrix_a,matrix_a,[a_beside[0],a_x,a_y+1,a_beside[3]],[a_x+1,a_beside[1],a_y+1,a_beside[3]])
    # B21+B22
    matrix_s8 = add_matrix(matrix_b,matrix_b,[b_x+1,b_beside[1],b_beside[2],b_y],[b_x+1,b_beside[1],b_y+1,b_beside[3]])
    # A11-A21
    matrix_s9 = del_matrix(matrix_a,matrix_a,[a_beside[0],a_x,a_beside[2],a_y],[a_x+1,a_beside[1],a_beside[2],a_y])
    # B11+B12
    matrix_s10 = add_matrix(matrix_b,matrix_b,[b_beside[0],b_x,b_beside[2],b_y],[b_beside[0],b_x,b_y+1,b_beside[3]])
    # A11*S1
    matrix_p1 = matrix_multiply(matrix_a,matrix_s1,[a_beside[0],a_x,a_beside[2],a_y],[0,len(matrix_s1)-1,0,len(matrix_s1[0])-1])
    # S2*B22
    matrix_p2 = matrix_multiply(matrix_s2,matrix_b,[0,len(matrix_s2)-1,0,len(matrix_s2[0])-1],[b_x+1,b_beside[1],b_y+1,b_beside[3]])
    # S3*B11
    matrix_p3 = matrix_multiply(matrix_s3,matrix_b,[0,len(matrix_s3)-1,0,len(matrix_s3[0])-1],[b_beside[0],b_x,b_beside[2],b_y])
    # A22*S4
    matrix_p4 = matrix_multiply(matrix_a,matrix_s4,[a_x+1,a_beside[1],a_y+1,a_beside[3]],[0,len(matrix_s4)-1,0,len(matrix_s4[0])-1])
    # S5*S6
    matrix_p5 = matrix_multiply(matrix_s5,matrix_s6,[0,len(matrix_s5)-1,0,len(matrix_s5[0])-1],[0,len(matrix_s6)-1,0,len(matrix_s6[0])-1])
    # S7*S8
    matrix_p6 = matrix_multiply(matrix_s7,matrix_s8,[0,len(matrix_s7)-1,0,len(matrix_s7[0])-1],[0,len(matrix_s8)-1,0,len(matrix_s8[0])-1])
    # S9*S10
    matrix_p7 = matrix_multiply(matrix_s9,matrix_s10,[0,len(matrix_s9)-1,0,len(matrix_s9[0])-1],[0,len(matrix_s10)-1,0,len(matrix_s10[0])-1])
    # P5+P4-P2+P6
    matrix_left_top = add_all_matrix(del_all_matrix(add_all_matrix(matrix_p5,matrix_p4),matrix_p2),matrix_p6)
    # P1+P2
    matrix_right_top = add_all_matrix(matrix_p1,matrix_p2)
    # P3+P4
    matrix_left_bottom = add_all_matrix(matrix_p3,matrix_p4)
    # P5+P1-P3-P7
    matrix_right_bottom = del_all_matrix(del_all_matrix(add_all_matrix(matrix_p5,matrix_p1),matrix_p3),matrix_p7)
    for m in range(0,len(matrix_left_top)):
        matrix_left_top[m].extend(matrix_right_top[m])
    for n in range(0,len(matrix_left_bottom)):
        matrix_left_bottom[n].extend(matrix_right_bottom[n])
    matrix_left_top.extend(matrix_left_bottom)
    return matrix_left_top


def format_matrix(matrix_a,matrix_b):
    max_len = max(len(matrix_a),len(matrix_a[0]),len(matrix_b[0]))
    des_len = int(math.pow(2,math.ceil(math.log2(max_len))))
    res_a = [ [0]*des_len for i in range(des_len)]
    res_b = [ [0]*des_len for i in range(des_len)]
    for i in range(0, len(matrix_a)):
        for j in range(0, len(matrix_a[i])):
            res_a[i][j] = matrix_a[i][j]
    for i in range(0, len(matrix_b)):
        for j in range(0, len(matrix_b[i])):
            res_b[i][j] = matrix_b[i][j]
    return [res_a,res_b]


def handle_matrix_multiply(matrix_a, matrix_b):
    des_x = len(matrix_a)-1
    des_y = len(matrix_b[0])-1
    [res_a,res_b] = format_matrix(matrix_a,matrix_b)
    temp_res = matrix_multiply(res_a, res_b, [0,len(res_a)-1,0,len(res_a[0])-1],[0,len(res_b)-1,0,len(res_b[0])-1])
    return [temp_res[i][0:des_y+1] for i in range(des_x+1)]


if __name__ == '__main__':
    a=[[1,3,4,5],[12,345,34,5],[56,345,34,5],[34,32,3,12]]
    b=[[456,456,45,6],[45,64,56,456],[67,67,6,7],[1,2,12,1]]
    c = [[456, 456], [45, 64], [67, 67], [1, 2]]
    # matrix_result = matrix_multiply(a, b, [0,len(a)-1,0,len(a[0])-1],[0,len(b)-1,0,len(b[0])-1])
    # for i in matrix_result:
    #     print(i)
    matrix_result = handle_matrix_multiply(a, c)
    for i in matrix_result:
        print(i)



# [864, 926, 297, 1407]
# [23280, 29840, 20124, 157635]
# [43344, 49904, 22104, 157899]
# [17157, 17777, 3484, 14829]