# P1028 题解

[P1028](https://www.luogu.com.cn/problem/P1028)
# 题意
输入一个整数 $n$，做为现在数列的最后一个数。每次在后面只能加一个比现在最后的一个数的一半小的数，也可以不加。问有多少个合法数列。

# 分析
用 $f$ 数组记录以 $i$ 结尾有多少个合法数列。

现依次找寻比现在小一半的数中合法个数再累加起来，最后还有自己结尾的情况。
# 代码
```cpp
#include<bits/stdc++.h>
using namespace std ;
int n ;
int f[1005] ;
int main()
{
    cin >> n ;
    for( int i = 1 ; i <= n ; i++ )
	{
        for( int j = 1 ; j <= i / 2 ; j++ )
		{
            f[i] += f[j] ;
        }
        f[i]++ ;
    }
    cout << f[n] ;
    return 0 ;
}
```