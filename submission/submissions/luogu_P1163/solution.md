# P1163 题解

核心算法是秦九韶算法和二分法，另外需要一定的财经知识，否则就呵呵了。在数据里有一个坑爹的月利率214.7%的数据，这不是贷款，这是抢钱- -

所以在二分中，需要从0-5之间进行二分查找。根据题目可以得出公式a=(...（m\*(1+x)-y)(1+x)-y)...)（共t次乘法）（秦九韶算法）（m表示贷款的原值、y表示每月支付的分期付款金额、t表示分期付款还清贷款所需的总月数，a表示在t个月后按二分得到的利率还剩下多少钱没有还）。如果a是正数说明利率过大，则从左侧继续二分查找；如果a是负数说明利率过大，则从右侧继续二分查找；如果a等于零则输出结束程序。二分查找结束的另一个条件是精度小于0.0001。

```cpp
#include<iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;
double m,y,s;
int t;
int out(double k)
{
    printf("%.1f",k*100);
    exit(0);
}
void solve(double l,double r)
{
    double k=(l+r)/2,u=r-l;
    double a=m;
    if(u<0.0001) out(k);
    for(int i=1;i<=t;i++)
          a=a*(1+k)-y;
    if(a>0) solve(l,k);
    if(a<0) solve(k,r);
    if(a==0) out(k);
}
int main()
{
    cin>>m>>y>>t;
    solve(0,5);
}
```