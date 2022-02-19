
import random
import copy

# 此算法合并步骤有问题，不一定得到最优解
# 如 ram = [77, 195, 463, 671, 36, 546, 905, 381, 65, 357, 316]时
# 最优解为 869,4,6  此算法解为 828,0,6

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
def div_merge_array(_ram, n, m):
    if n == m:
        m1 = [_ram[n], n, m]
    elif m-n == 1:
        if _ram[n] > _ram[m]:
            m1 = [_ram[n], n, n]
        else:
            m1 = [_ram[m], m, m]
        if _ram[n]+_ram[m] > m1[0]:
            m1 = [_ram[n]+_ram[m], n, m]
    else:
        m1 = div_merge_array(_ram, n, int((n+m)/2))
        m2 = div_merge_array(_ram, int((n+m)/2)+1, m)
        if m1[2]+1 == m2[1]:
            if m1[0] > 0 and m2[0] > 0:
                m1[0] = m1[0] + m2[0]
                m1[1] = m1[1]
                m1[2] = m2[2]
        else:
            _tem = 0
            for _i in range(m1[2]+1, m2[1]):
                _tem = _tem + _ram[_i]
            if _tem + m1[0] > 0 and _tem + m2[0] > 0:
                m1[0] = _tem + m1[0] + m2[0]
                m1[1] = m1[1]
                m1[2] = m2[2]
            elif m2[0] > m1[0]:
                m1 = m2
    return m1


# 最大子数组问题：给定数组，在前端选择较小值，在后端选择较大值，作差。输出最大差值及选择的方法
if __name__ == "__main__":
    ram = get_ram_array(10, 100)
    print(ram)
    ram1 = copy.deepcopy(ram)
    # 问题转化：输入转换成后与前的差值
    for i in range(1, len(ram1)):
        ram1[i] = int(ram[i] - ram[i-1])
    print(ram1)
    # 求ram的最大字数组
    # 采用分治的策略，将为题分解为多个子数组求其自身的最大子数组，最后合并
    k = div_merge_array(ram1, 1, len(ram1)-1)
    print(k)

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
    print(mi, ii, jj)

