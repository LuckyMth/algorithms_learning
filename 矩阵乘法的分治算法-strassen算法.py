
import random


# 获取随机数组
def get_ram_array(_num, _max):
    _ram = []
    _tem = random.randint(0, _max)
    for _i in range(_num):
        while _tem in _ram:
            _tem = random.randint(0, 1000)
        _ram.append(_tem)
    return _ram




if __name__ == "__main__":
    aA = list()
    bB = list()
    cC = list()

    for i in range(5):
        aA.append(get_ram_array(5, 50))
    print(aA)

    for i in range(5):
        bB.append(get_ram_array(5, 50))
    print(bB)

    for i in range(5):
        for j in range(5):
            cij = 0
            for k in range(5):
                cij = cij + aA[i][k] * bB[k][j]
            cC.append(cij)
    print(cC)

