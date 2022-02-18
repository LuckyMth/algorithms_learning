
import random


def get_ram_array(_num):
    _ram = []
    k = random.randint(0, 1000)
    for _i in range(_num):
        while k in _ram:
            k = random.randint(0, 500)
        _ram.append(k)
    return _ram


# 最大子数组问题：给定数组，在前端选择较小值，在后端选择较大值，作差。输出最大差值及选择的方法
if __name__ == "__main__":
    ram = get_ram_array(50)
    print(ram)
    # 暴力求解
    mi = -1
    ii = -1
    jj = -1
    for i in range(len(ram)-1):
        for j in range(i+1, len(ram)):
            if ram[j] > ram [i] and ram[j] - ram [i] > mi:
                mi = ram[j] - ram[i]
                ii = i
                jj = j
    print(mi, ii, jj)
