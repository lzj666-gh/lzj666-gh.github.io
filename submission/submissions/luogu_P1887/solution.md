# P1887 题解

其实这道题没必要那么复杂，不用开数组。

# 要求乘积最大，当然要尽可能接近，最多差1最多差1最多差1（重要）。

我们可以先把N除以M，算出后面M个数字中小1的，然后再把N%M，算出有几个应该多1，挨个输出

## 注意！字典序是从小到大！（我被这个困扰了半小时）

代码

    
```cpp
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int a,b,c,d,i,j,k,n,m,ans;
    cin>>a>>b;
    n=a%b;
    ans=a/b;
    for(i=n;i<b;++i)
        cout<<ans<<" ";
    for(i=0;i<n;++i)
        cout<<ans+1<<" ";
}
——人生自古谁无死，留篇题解帮萌新——
```