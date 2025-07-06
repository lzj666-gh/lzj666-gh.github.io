# P1287 题解

题解：[P1287 盒子与球](https://www.luogu.org/problemnew/show/P1287)

> 不了解的：[stirling数（斯特林数） - 百度百科](https://baike.baidu.com/item/%E6%96%AF%E7%89%B9%E6%9E%97%E6%95%B0/4938529?fr=aladdin)

分析如下：

> 设有n个不同的球，分别用b1,b2,……bn表示。从中取出一个球bn，bn的放法有以下两种：

> 1) bn独自占一个盒子；那么剩下的球只能放在m-1个盒子中，方案数为：f(n-1, m-1)

> 2) bn与别的球共占一个盒子；那么可以事先将b1,b2,……bn-1这n-1个球放入m个盒子中，然后再将球bn可以放入其中一个盒子中，方案数为 :m*f(n-1,m)

> 3) 边界条件

1. > a) 盒子数 < 0（盒子数“超支”），不成一种方案。

2. > b) 球数 < 盒子数（盒子数“超支”），不成一种方案。

3. > c) 球数 = 盒子数（正好），为一种方案。

so...

```cpp
#define ll long long

ll f(int n, int m)
{
	if (m <= 0 || n < m)
    	return 0;
    if (n == m)
    	return 1;
    else
    	return fun(n-1, m-1) + fun(n-1, m) * m;
}
```

and than...

> 现有r个互不相同的盒子!!!

> 不同!!!

> 所以还要乘上盒子的排列组合

```cpp
#define ll long long

ll fac(int i) // 然而这个函数不用讲什么
{
	if (i == 1)
    	return 1;
    else
    	return i * fac(i - 1);
}
```

so...

```cpp
int main() // 完美主程序
{
    ll n, m;
    cin >> n >> m;
    cout<< f(n, m) * fac(m);
    return 0;
}
```

合成...

```cpp
#include <stdio.h>
#include <iostream>
#define ll long long
using namespace std;

ll f(int n, int m)
{
    if (m <= 0 || n < m)
        return 0;
    if (n == m)
        return 1;
    else
        return fun(n-1, m-1) + fun(n-1, m) * m;
}

ll fac(int i) // 然而这个函数不用讲什么
{
    if (i == 1)
        return 1;
    else
        return i * fac(i - 1);
}

int main() // 完美主程序
{
    ll n, m;
    cin >> n >> m;
    cout<< f(n, m) * fac(m);
    return 0;
}
```