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