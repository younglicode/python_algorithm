## 斐波那契数列 动态规划实现, 跟递归实现的，性能优化很好
## 碰到递归的算法，最好加缓存，以免重复计算

fi_array = [0, 1]

def fi(i: int) -> int:
    
    if i < 2:
        return fi_array[i]
    
    while len(fi_array) < i:
        fi_array.append(fi_array[-1]+fi_array[-2])
    
    return fi_array[i-1]
    

if __name__ == "__main__":
    result = fi(i=10000)
    print(fi_array)
    print(result)