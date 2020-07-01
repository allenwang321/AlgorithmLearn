s = input().strip()
p = input().strip()

nxt = []


def build_next():
    nxt.append(0)
    x = 1
    now = 0
    while x < len(p):
        if p[now] == p[x]:  # 如果p[now] == p[x] 则可以向右扩展以为
            now += 1
            x += 1
            nxt.append(now)
        elif now:
            now = nxt[now - 1]  # 缩小now,改为nxt[now-1]
        else:
            nxt.append(0)  # now 为零时，nxt[x] = 0
            x += 1


def search():
    tar = 0  # 主串中将要匹配的位置
    pos = 0  # 模式串中将要匹配的位置

    while tar < len(s):
        if s[tar] == p[pos]:  # 若两个字符串相等，则 tar，pos 各进一步
            tar += 1
            pos += 1
        elif pos:  # 失配了，若pos ≠ 0 则依据nxt数组移动标尺
            pos = nxt[pos - 1]
        else:  # pos[0] 失配了直接把标尺右移一位
            tar += 1
        if pos == len(p):  # pos走到len[p],匹配成功
            print(tar - pos + 1)
            pos = nxt[pos - 1]  # 移动标尺


build_next()
search()
print(''.join(map(str, nxt)))
