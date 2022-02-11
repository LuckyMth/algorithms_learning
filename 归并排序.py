def sort_merge(arr, p, q):
    if p == q:
        res[p] = arr[p]
    # 每个部分分别排序
    elif q - p == 1:
        res[p:q+1] = arr[p:q+1]
        if arr[p] > arr[q]:
            temp = res[p]
            res[p] = res[q]
            res[q] = temp
    # 排序好的两个部分进行合并
    else:
        t = int((p+q)/2)
        sort_merge(arr, p, t)
        sort_merge(arr, t+1, q)
        arr[p:q+1] = res[p:q+1]
        il = 0
        ir = 0
        ik = 0
        while il != t-p+1 and ir != q-t:
            if arr[p+il] <= arr[t+1+ir]:
                res[p+ik] = arr[p+il]
                il = il+1
            else:
                res[p+ik] = arr[t+1+ir]
                ir = ir+1
            ik = ik+1
        if il == t-p+1:
            for i_temp in range(ir, q-t):
                res[p+ik] = arr[t+1+i_temp]
                ik = ik+1
        else:
            for i_temp in range(il, t-p+1):
                res[p+ik] = arr[p+i_temp]
                ik = ik+1
