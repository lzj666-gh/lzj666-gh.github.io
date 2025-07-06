# P7075 题解

在一种历法中，日期计算以400年为周期，每400年都有恰好146097天

预处理出400年内的情况，将年份模400即可快速得到答案

几个简化代码的技巧：

对于格里高利历，以1200年1月1日为起始日，$r$减去跳过的天数（2159351）

判断历法：$r\leqslant2299160$即为儒略历

公元前$x$年视为$1-x$年

```cpp
#include<bits/stdc++.h>
typedef long long ll;
const int N=146097;//格里高利历400年的天数
int T,y[N],m[N],d[N];
ll n,t;
inline int md(int y,int m){//格里高利历y年m月的天数
    if(m==2)return y%4?28:y%100?29:y%400?28:29;
    return m==4||m==6||m==9||m==11?30:31;
}
int main(){
    m[0]=d[0]=1;
    for(int i=1;i<N;++i){
        d[i]=d[i-1]+1;m[i]=m[i-1];y[i]=y[i-1];
        if(d[i]>md(y[i],m[i]))++m[i],d[i]=1;
        if(m[i]>12)++y[i],m[i]=1;
    }//y[i],m[i],d[i]分别表示从0年1月1日经过i天的年月日
    scanf("%d",&T);
    while(T--){
        scanf("%lld",&n);
        if(n>2299160){//格里高利历
            n-=2159351;
            t=n/N*400+1200;
            n%=N;
        }else{
            t=n/1461*4-4712;//1461是儒略历4年的天数
            n%=1461;
        }
        if(t+y[n]>0)printf("%d %d %lld\n",d[n],m[n],t+y[n]);
        else printf("%d %d %lld BC\n",d[n],m[n],1-t-y[n]);
    }
}
```
