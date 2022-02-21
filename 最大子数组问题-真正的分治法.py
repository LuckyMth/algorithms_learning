
import random
import copy


def max_array_mid(__ram, _n, _m):
    _mid = int((_n+_m)/2)
    # 向左方向的最大子数组
    _ml = [__ram[_mid], _mid, _mid]
    # 向右方向的最大子数组
    _mr = [__ram[_mid+1], _mid+1, _mid+1]
    # 跨过中点肯定包含_ram[_mid]和_ram[_mid+1]
    __tem = _ml[0]
    for _i in range(_n, _mid):
        _nb = _mid-1+_n-_i
        __tem = __tem + __ram[_nb]
        if _ml[0] < __tem:
            _ml[0] = __tem
            _ml[1] = _nb
    __tem = _mr[0]
    for _i in range(_mid+1, _m):
        __tem = __tem + __ram[_i+1]
        if _mr[0] < __tem:
            _mr[0] = __tem
            _mr[2] = _i+1
    return [_ml[0]+_mr[0], _ml[1], _mr[2]]


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
def div_merge_array(_ram, n, m):
    if n == m:
        m1 = [_ram[n], n, m]
    elif m-n == 1:
        if _ram[n] > _ram[m]:
            m1 = [_ram[n], n, n]
        else:
            m1 = [_ram[m], m, m]
        if _ram[n] > 0 and _ram[m] > 0:
            m1 = [_ram[n]+_ram[m], n, m]
    else:
        m1 = div_merge_array(_ram, n, int((n+m)/2))
        m2 = div_merge_array(_ram, int((n+m)/2)+1, m)
        m3 = max_array_mid(_ram, n, m)
        if m2[0] > m1[0]:
            m1 = m2
        if m3[0] > m1[0]:
            m1 = m3
    return m1


# 最大子数组问题：给定数组，在前端选择较小值，在后端选择较大值，作差。输出最大差值及选择的方法
if __name__ == "__main__":
    for ik in range(200000):
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

