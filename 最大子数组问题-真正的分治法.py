
import random
import copy


# 求跨过中点的最大子数组
def max_arraymid3(ram3, n3, m3):
    mid3 = int((n3+m3)/2)
    # 向左方向的最大子数组
    ml3 = [ram3[mid3], mid3, mid3]
    # 向右方向的最大子数组
    mr3 = [ram3[mid3+1], mid3+1, mid3+1]
    # 跨过中点肯定包含ram3[mid3]和ram3[mid3+1]
    tem3 = ml3[0]
    for i3 in range(n3, mid3):
        nb3 = mid3-1+n3-i3
        tem3 = tem3 + ram3[nb3]
        if ml3[0] < tem3:
            ml3[0] = tem3
            ml3[1] = nb3
    tem3 = mr3[0]
    for i3 in range(mid3+1, m3):
        tem3 = tem3 + ram3[i3+1]
        if mr3[0] < tem3:
            mr3[0] = tem3
            mr3[2] = i3+1
    return [ml3[0]+mr3[0], ml3[1], mr3[2]]


# 获取随机数组
def get_ram_array(_num, _max):
    _ram = []
    _tem = random.randint(0, _max)
    for _i in range(_num):
        while _tem in _ram:
            _tem = random.randint(0, 1000)
        _ram.append(_tem)
    return _ram


# 求最大子数组
# 跨过中点的最大子数组不一定就是左端最大子数组+右端最大子数组！
def div_merge_array(ram2, n2, m2):
    if n2 == m2:
        ma0 = [ram2[n2], n2, m2]
    # elif m2-n2 == 1:
    #     if ram2[n2] > ram2[m2]:
    #         ma0 = [ram2[n2], n2, n2]
    #     else:
    #         ma0 = [ram2[m2], m2, m2]
    #     if ram2[n2] > 0 and ram2[m2] > 0:
    #         ma0 = [ram2[n2]+ram2[m2], n2, m2]
    else:
        ma1 = div_merge_array(ram2, n2, int((n2+m2)/2))
        ma2 = div_merge_array(ram2, int((n2+m2)/2)+1, m2)
        ma3 = max_arraymid3(ram2, n2, m2)
        if ma2[0] > ma1[0]:
            ma0 = ma2
        else:
            ma0 = ma1
        if ma3[0] > ma0[0]:
            ma0 = ma3
    return ma0


# 最大子数组问题：给定数组，在前端选择较小值，在后端选择较大值，作差。输出最大差值及选择的方法
if __name__ == "__main__":
    for ik in range(20000):
        ram = get_ram_array(5, 100)
        # print(ram)
        ram1 = copy.deepcopy(ram)
        # 问题转化：输入转换成后与前的差值
        for i in range(1, len(ram1)):
            ram1[i] = int(ram[i] - ram[i-1])
        # print(ram1)
        # 求ram的最大字数组
        # 采用分治的策略，将为题分解为多个子数组求其自身的最大子数组，最后合并
        k = div_merge_array(ram1, 1, len(ram1)-1)
        k[1] = k[1]-1
        # print(k)

        # 暴力求解
        mi = -1
        ii = -1
        jj = -1
        for i in range(len(ram)-1):
            for j in range(i+1, len(ram)):
                if ram[j] > ram[i] and ram[j] - ram[i] > mi:
                    mi = ram[j] - ram[i]
                    ii = i
                    jj = j
        k1 = [mi, ii, jj]
        # print(k1)
        if k != k1:
            print(ram, ram1, k, k1)

