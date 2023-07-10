## 斐波那契数列 递归实现，执行时间呈指数上升

def fi(i: int) -> int:
    if i == 0:
        return 0
    if i == 1:
        return 1
    
    return fi(i - 1) + fi(i - 2)

if __name__ == "__main__":
    result = fi(i=37)
    print(result)