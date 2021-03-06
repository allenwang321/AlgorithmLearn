### 汉诺塔问题

#### 问题

有三个金刚石塔，第一个从小到大摞着64片黄金圆盘。现在把圆盘按大小顺序重新摆放在最后一个塔上。并且规定，在小圆盘上不能放大圆盘，在三个塔之间一次只能移动一个圆盘。

#### 解决方案

```python
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
```

> 首先将n-1个盘子移动到中间的缓冲的b柱子上，此时a柱子上只剩下最后一个最大的移动到c柱子上，然后将b柱子上剩下的n-1个移动到c柱子上