#!/usr/bin/env python3

import math
from tkinter import *
from rand_cof_M import generate_random_matrix

#######Matrix_read#######
def read_Mp(str, k, l):
    file_Mp = open(str, 'r')
    Mp = []

    k_ch = 0
    i_temp1 = 0
    i_temp2 = 0

    for line in file_Mp:
        k_ch += 1
        if k_ch <= k:
            Mp.append([])
        else:
            break
        l_ch = 0
        i = 0
        i_temp1 = 0
        i_temp2 = 0
        while line[i] != '\n':
            if (line[i] == ' ') or (line[i + 1] == '\n'):
                if i_temp2 == 0:
                    i_temp1 = i_temp2
                else:
                    i_temp1 = (i_temp2 + 1)
                if line[i + 1] == '\n':
                    i_temp2 = i + 1
                else:
                    i_temp2 = i
                l_ch += 1
                if l_ch <= l:
                    Mp[(k_ch - 1)].append(float(line[i_temp1:i_temp2]))
                else:
                    break
            i += 1
    file_Mp.close()
    return Mp


#######Target_func#######
def Fy(x, y, Aij, Bij, Cij, Dij, cof_s1, cof_s2, cof_p1, cof_p2):
    Res_fi = 0.000
    prev_s1 = 0.000
    prev_s2 = 0.000
    for i in range(0, k):
        for j in range(0, l):
            prev_s1 += (Aij[i][j] * (math.sin(math.pi * i * x) * math.sin(math.pi * j * y)) + cof_p1 * (
                Bij[i][j] * (math.cos(math.pi * i * x) * math.cos(math.pi * j * y))))
            prev_s2 += (Cij[i][j] * (math.sin(math.pi * i * x) * math.sin(math.pi * j * y)) + cof_p2 * (
                Dij[i][j] * (math.cos(math.pi * i * x) * math.cos(math.pi * j * y))))
    Res_fi = -1 * (cof_s1 * prev_s1 + cof_s2 * prev_s2)
    return Res_fi


####### m_find #######
def find_m_x(r, M, c, y):
    max = 0
    for i in range(1, c):
        z1 = Fy(M[i], y, Aij, Bij, Cij, Dij, cof_s1, cof_s2, cof_p1, cof_p2)
        z2 = Fy(M[i - 1], y, Aij, Bij, Cij, Dij, cof_s1, cof_s2, cof_p1, cof_p2)
        temp = ((z1 - z2) / (M[i] - M[i - 1]))
        if temp < 0:
            temp *= -1
        if temp > max:
            max = temp
    if max > 0:
        m = max * r
    else:
        m = 0
    return m


####### Charact_par #######
def Rs(i, M, m, z1, z2):
    rs = (m * (M[i] - M[i - 1]) - (z1 + z2)) / 2
    return rs


####### add_new_y #######
def add_y(M, c, R, sqx, x_min, y_pro, res_x, curr, r, canv):
    max_id = 0
    i_id = 0
    min1 = 0
    c1 = 2
    max = R[0]
    for i in range(1, c - 1):
        if R[i] > max:
            max = R[i]
            max_id = i
    i = max_id
    new_y = (M[i + 1] + M[i]) / 2
    ##new_y=(M[i+1]+M[i])/2
    M.insert(i + 1, new_y)
    c += 1
    m3 = find_m_x(r, sqx, c1, M[i + 1])
    z1 = Fy(sqx[0], M[i + 1], Aij, Bij, Cij, Dij, cof_s1, cof_s2, cof_p1, cof_p2)
    z2 = Fy(sqx[1], M[i + 1], Aij, Bij, Cij, Dij, cof_s1, cof_s2, cof_p1, cof_p2)
    rs_t = Rs(1, sqx, m, z1, z2)
    ##rs_t=(M[i+1]-M[i])
    R1.append(rs_t)
    while min1 == 0:
        x_min = add_x(m3, sqx, c1, R1, M[i + 1], x_min, r, canv)
        c1 += 1
        min1 = dif_stop(sqx, c1, e)
    y_pro.insert(i + 1, x_min[1])
    res_x.insert(i + 1, x_min[0])
    R.remove(max)
    R.insert(i, ((M[i + 1] - M[i]) / 2))
    #Rs(i+1,M,m,res_x[i],res_x[i+1])
    R.insert(i + 1, ((M[i + 2] - M[i + 1]) / 2))
    #Rs(i+2,M,m,res_x[i+1],res_x[i+2])
    if curr[0] > res_x[i + 1]:
        curr.insert(0, res_x[i + 1])
        curr.insert(1, y_pro[i + 1])
        curr.insert(2, M[i + 1])
    return curr


####### add_new_x #######
def add_x(m, M, c, R, y, curr, r, canv):
    max_id = 0
    i_id = 0
    max = R[0]
    for i in range(1, c - 1):
        if R[i] > max:
            max = R[i]
            max_id = i
    i = max_id
    z1 = Fy(M[i + 1], y, Aij, Bij, Cij, Dij, cof_s1, cof_s2, cof_p1, cof_p2)
    z2 = Fy(M[i], y, Aij, Bij, Cij, Dij, cof_s1, cof_s2, cof_p1, cof_p2)
    new_x = ((M[i + 1] + M[i]) + ((z1 - z2) / m)) / 2
    ##new_x=new_x+M[i]
    M.insert(i + 1, new_x)
    z3 = Fy(M[i + 1], y, Aij, Bij, Cij, Dij, cof_s1, cof_s2, cof_p1, cof_p2)
    R.remove(max)
    R.insert(i, Rs(i + 1, M, m, z1, z3))
    R.insert(i + 1, Rs(i + 2, M, m, z3, z2))
    canv.create_oval(((q * new_x) + 48), (-q * (y) + 602), (q * (new_x) + 52), (-q * (y) + 598), fill='black')
    m = find_m_x(r, M, c, y)
    if curr[0] > z3:
        curr.insert(0, z3)
        curr.insert(1, M[i + 1])
    return curr


####### dif_stop #######
def dif_stop(M, c, e):
    min_f = 0
    for i in range(1, c):
        k = (M[i] - M[i - 1])
        if k < 0:
            k *= -1
        if k < e:
            min_f = 1
            break
    return min_f


if __name__ == "__main__":
    #k and l - matrix metric k*l#
    k = 10
    l = 10

    generate_random_matrix(k, l)

    #cof of Sum and cof between a and b#
    cof_s1 = 4
    cof_s2 = 5

    cof_p1 = 4
    cof_p2 = 6

    qx = [[1, 2], [3, 4], [6, 5]]

    ####### Reduct_min #######

    ###Aij###
    Aij = read_Mp('Aij', k, l)
    ###Bij###
    Bij = read_Mp('Bij', k, l)
    ###Cij###
    Cij = read_Mp('Cij', k, l)
    ###Dij###
    Dij = read_Mp('Dij', k, l)

    ###res###

    root = Tk()

    x0 = 50
    y0 = 600

    canv = Canvas(root, width=1000, height=1000, bg="white", cursor="pencil")

    dl_x = (qx[0][1] - qx[0][0]) * 0.002
    q = 1 / dl_x

    e = 0.02
    r = 6000
    c1 = 2
    c2 = 2
    Res_y = []
    y_prox_x = []
    R1 = []
    R2 = []
    min1 = 0
    min2 = 0
    m2 = 2
    y_min = [1, 0, 0]
    count = 0
    gdb_c1 = 0
    while min2 == 0:
        min1 = 0
        x_min = [1, 0]
        sqx = [qx[0][0], qx[0][1]]
        c1 = 2
        if count == 0:
            m = find_m_x(r, sqx, c1, qx[1][0])
            z1 = Fy(sqx[0], qx[1][0], Aij, Bij, Cij, Dij, cof_s1, cof_s2, cof_p1, cof_p2)
            z2 = Fy(sqx[1], qx[1][0], Aij, Bij, Cij, Dij, cof_s1, cof_s2, cof_p1, cof_p2)
            rs_t = Rs(1, sqx, m, z1, z2)
            R1.append(rs_t)
            while min1 == 0:
                x_min = add_x(m, sqx, c1, R1, qx[1][0], x_min, r, canv)
                c1 += 1
                min1 = dif_stop(sqx, c1, e)
            y_prox_x.append(x_min[1])
            count += 1
            Res_y.append(x_min[0])
        elif count == 1:
            m = find_m_x(r, sqx, c1, qx[1][1])
            z1 = Fy(sqx[0], qx[1][1], Aij, Bij, Cij, Dij, cof_s1, cof_s2, cof_p1, cof_p2)
            z2 = Fy(sqx[1], qx[1][1], Aij, Bij, Cij, Dij, cof_s1, cof_s2, cof_p1, cof_p2)
            rs_t = Rs(1, sqx, m, z1, z2)
            R1.append(rs_t)
            while min1 == 0:
                x_min = add_x(m, sqx, c1, R1, qx[1][1], x_min, r, canv)
                c1 += 1
                min1 = dif_stop(sqx, c1, e)
            y_prox_x.append(x_min[1])
            count += 1
            Res_y.append(x_min[0])
            ##rs_t2=Rs(1,qx[1],m2,Res_y[0],Res_y[1])
            rs_t2 = qx[1][1] - qx[1][0]
            R2.append(rs_t2)
        else:
            y_min = add_y(qx[1], c2, R2, sqx, x_min, y_prox_x, Res_y, y_min, r, canv)
            c2 += 1
            min2 = dif_stop(qx[1], c2, e)

    #print(qx[0])
    #print(qx[1])
    #print(Res_y)
    print("f_min(x,y)= " + repr(y_min[0]))
    print("point = x,y (" + repr(y_min[1]) + " " + repr(y_min[2]) + ")")
    canv.create_line(50, 600, 50, 100, width=2, arrow=LAST)
    canv.create_line(50, 600, 550, 600, width=2, arrow=LAST)

    for i in range(501):
        for j in range(501):
            x = x0 + j
            y = y0 - i
            fy = Fy((j * dl_x) + qx[0][0], i * dl_x + qx[1][0], Aij, Bij, Cij, Dij, cof_s1, cof_s2, cof_p1, cof_p2)
            if ((fy * 100.0) % 250 <= 8.0) and ((fy * 100.0) % 250 >= -8.0):
                if (fy * 10.0) <= 5.2:
                    canv.create_oval(x, y, x + 1, y + 1, fill='blue')
    print(((q * y_min[1]) + 48), (-q * (y_min[2]) + 602), (q * (y_min[1]) + 52), (-q * (y_min[2]) + 598))
    canv.create_rectangle(((q * y_min[1]) + 48), (-q * (y_min[2]) + 602), (q * (y_min[1]) + 52),
                          (-q * (y_min[2]) + 598),
                          fill='black')
    canv.pack()
    root.mainloop()
