# P1025 题解

这道题我们可以用dp:


f[i][x] 表示 i 分成 x 个非空的数的方案数。


显然 i<x 时 f[i][x]=0 , i=x 时 f[i][x]=1;


其余的状态，我们分情况讨论：

①有1的 ②没有1的

第一种情况，方案数为 f[i-1][x-1]

第二种情况，方案数为 f[i-x][x] (此时 i 必须大于 x)


所以，状态转移方程为： f[i][x]=f[i-1][x-1]+f[i-x][x]


程序如下：

    
```cpp
#include<bits/stdc++.h>
using namespace std;
int n,k,f[201][7];  //f[k][x] k 分成 x 份 ={f[k-1][x-1],f[k-x][x]}
int main(){
    cin >> n >> k;
    for (int i=1;i<=n;i++) {f[i][1]=1;f[i][0]=1;}for (int x=2;x<=k;x++) {f[1][x]=0;f[0][x]=0;}  // 边界，为了防止炸，我把有0的也处理了
    for (int i=2;i<=n;i++)
        for (int x=2;x<=k;x++)
            if (i>x) f[i][x]=f[i-1][x-1]+f[i-x][x];
            else f[i][x]=f[i-1][x-1];
    cout<<f[n][k];
    return 0;
}
```