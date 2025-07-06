# P1890 题解

运用动规的思想，$f[i][j]$表示区间$(i,j)$中$gcd$，则状态转移方程为

$f[i][j]=gcd(f[i][i],f[i+1][j])$

边界$f[i][i]=itself$，另外$c++$中有自带$gcd:$__gcd(x,y)

```
#include<bits/stdc++.h>
using namespace std;
long long a,b,f[1001][1001],p,q;
int main(){
    scanf("%lld%lld",&a,&b);
    for(int i=1;i<=a;i++) scanf("%lld",&f[i][i]);
    for(int i=a-1;i>=1;i--)
    for(int j=i+1;j<=a;j++)
    f[i][j]=__gcd(f[i][i],f[i+1][j]);
    for(int i=1;i<=b;i++)
    scanf("%lld%lld",&p,&q),
    printf("%lld\n",f[p][q]);
}
```