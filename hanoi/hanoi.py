def move(n, a, b, c):
    if n == 1:
        print(a + "->" + c)
        return
    # 首先将n-1个移动到缓冲的b柱子上
    move(n - 1, a, c, b)
    # 将最大的移动到c柱子上
    move(1, a, b, c)
    # 最后将b柱子上n-1个移动到c柱子上
    move(n - 1, b, a, c)


move(3, "a", "b", "c")
