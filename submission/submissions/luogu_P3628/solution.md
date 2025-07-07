# P3628 题解

斜率优化DP

找斜率式的方法还可以把dp方程化为kx+b=y的一次函数形式。

参考资料:http://www.cnblogs.com/MashiroSky/p/6009685.html

显然先预处理前缀和$s(i)=\sum_{k=1}^ix_i$

设$d(i)$为将前$i$个士兵分组的最大修正后战斗力。

$d(i)=max\{\ d(j)+a(s(i)-s(j))^2+b(s(i)-s(j))+c\ \}$

$d(i)=max\{\ d(j)+a\times s(i)^2-2a\times s(i)s(j)+a\times s(j)^2+b\times s(i)-b\times s(j)+c\ \}$

$d(i)=max\{\ d(j)-2a\times s(i)s(j)+a\times s(j)^2-b\times s(j)\ \}+a\times s(i)^2+b\times s(i)+c$

设
$K_i=2a\times s(i)$

$X_j=s(j)$

$B_i=d(i)-a\times s(i)^2-b\times s(i)-c$

$Y_j=d(j)+a\times s(j)^2-b\times s(j)$

直线解析式为$K_iX_j+B_i=Y_j$其中斜率$K_i$单减,$X_j$单增。

要求$d(i)$最大即求$B_i$最大，结合图像可得最优点$(X_j,Y_j)$一定在上凸包上。

用单调队列维护上凸包即可。

**代码**


```cpp
#include<cstdio>
#include<iostream>
#include<cstring>
#define k(A) (2*a*s[A])
#define x(A) s[A]
#define b(A) (d[A]-a*s[A]*s[A]-b*s[A]-c)
#define y(A) (d[A]+a*s[A]*s[A]-b*s[A])
using namespace std;
const int maxn=1000010;
long long d[maxn],s[maxn];
int q[maxn],n,a,b,c;
double slope(int i,int j){
    return 1.0*(y(i)-y(j))/(x(i)-x(j));
}
int main(){
    cin>>n>>a>>b>>c;
    s[0]=q[0]=d[0]=0;
    for(int i=1;i<=n;i++){
        int x;
        scanf("%d",&x);
        s[i]=s[i-1]+x;
    }
    int head=0,tail=0;
    for(int i=1;i<=n;i++){
        while(head<tail&&slope(q[head],q[head+1])>k(i)) head++;
        d[i]=-(k(i)*x(q[head])-y(q[head])-a*s[i]*s[i]-b*s[i]-c);
        while(head<tail&&slope(q[tail-1],q[tail])<=slope(q[tail],i)) tail--;
        q[++tail]=i;
    }
    cout<<d[n]<<endl;
}
    
```