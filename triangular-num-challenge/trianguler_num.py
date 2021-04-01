def mincount_triangular(n):
    #三角数定理の方程式にあてはまるx,y,zの組を探索
    for x in range(n+1):
        for y in range(n+1):
            for z in range(n+1):
                if x*(x+1)/2 + y*(y+1)/2 + z*(z+1)/2 == n:
                    solution = [x, y, z]
                    break
            else:
                continue
            break
        else:
            continue
        break
        
    #リストの中の0の数を確認することでいくつの三角数の組み合わせであるのかを確認し、その数を戻り値とする                
    zero_quantity = len([i for i in solution if i == 0])
    return 3 - zero_quantity