
import random


if __name__ == "__main__":
    leng = 20
    arr = []
    while leng != 0:
        while 1:
            tem = random.randint(0, 1000)
            if tem not in arr:
                arr.append(tem)
                break
        leng = leng-1
    print(arr)

    # # 插入排序
    # for m in range(len(arr)):
    #     for n in range(m-1, -1, -1):
    #         if arr[n+1] < arr[n]:
    #             tem = arr[n+1]
    #             arr[n+1] = arr[n]
    #             arr[n] = tem
    #         else:
    #             break
    # print(arr)

    # 二分插入排序
    for m in range(1, len(arr)):
        i = 0
        j = m-1
        while i <= j:
            mid = int((i+j)/2)
            if arr[mid] > arr[m]:
                j = mid-1
            else:
                i = mid+1
        tem = arr[m]
        arr[i+1:m+1] = arr[i:m]
        arr[i] = tem
    print(arr)

