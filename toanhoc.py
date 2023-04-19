from namslib.unicode import mutren, muduoi
def giaithua(so):
    ketqua = 1
    for x in range(so):
        ketqua = ketqua*so
        so = so - 1
    return ketqua
#Chỉnh hợp chập k của n
def chinhhop(k, n):
    ketqua = giaithua(n)/giaithua(n-k)
    return ketqua
#Tổ hợp chập k của n
def tohop(k, n):
    ketqua = chinhhop(k, n)/giaithua(k)
    return ketqua
#Nhị thức Newton
def nhithucnewton(a, b, n):
    k = n
    h = 0
    pheptinh = []
    ketqua = []
    for x in range(n+1):
        kq = tohop(k, n)*(a**(n-h))*(b**(n-k))
        if k == n:
            pt = f"C{muduoi(n)}{mutren(h)}{str(a)}{mutren(n)}"
        if h == n:
            pt = f"C{muduoi(n)}{mutren(h)}{str(b)}{mutren(n)}"
        if k != n and h != n:
            pt = f"C{muduoi(n)}{muduoi(h)}{str(a)}{muduoi(n-h)}{str(b)}{muduoi(n-k)}"
        pheptinh.append(pt)
        ketqua.append(kq)
        k = k - 1
        h = h + 1
    return f'Khai triển: {pheptinh}, kết quả lần lượt là: {ketqua}'
def kiemtrasonguyento(so):
    if so == 2:
        return f"{so} là số nguyên tố"
    elif so < 2:
        return f"{so} không phải là số nguyên tố"
    elif so % 2 == 0:
        return f"{so} không phải là số nguyên tố"
    else: 
        for i in range(3,int(so**0.5)+1,2):
            if so % i == 0:
                return f"{so} không phải là số nguyên tố"
            else:
                return f"{so} là số nguyên tố"
def lietkesonguyento(sogioihan):
    danhsach = []
    for so in range(2,sogioihan+1):
        if so == 2:
            danhsach.append(so)
        for i in range(3,int(so**0.5)+1,2):
            if so % i == 0:
                break
        else:
            danhsach.append(so)
    return danhsach