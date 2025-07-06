# B2132 题解

## 解法
由于本题数据范围较小，因此用 $i$ 直接从 3 到 $n$ 枚举每个数，若 $i$ 和 $i-2$ 均为素数则输出即可 
## 代码
```cpp
#include<bits/stdc++.h>
using namespace std;
int n;
bool prime(int x)//判断是否为质数的函数 
{
    if(x==1) return false;
    if(x==2) return true;
    int j=2;
    while(j*j<=x && x%j!=0) j++;
    if(x%j==0) return false;
    else return true;
}
bool pd=true; 
int main()
{
    cin>>n;
    for(int i=3;i<=n;i++)
    {
        if(prime(i) && prime(i-2))//枚举 
        {
            cout<<i-2<<" "<<i<<endl;
            pd=false;
        }
    }
    if(pd) cout<<"empty"<<endl;
    //若没有找到，则输出 "empty"
    return 0;
}
```
