# P1332 题解

有一句话叫暴力出奇迹，天下第一短代码

一开始做这道题写了一个BFS，莫名其妙70，一脸懵逼

一气之下给了一个暴力，AC了（？？？）

别的不说

枚举每一个领主和感染源，求他们曼哈顿距离，感染时间为min{Dis}

上代码

```cpp
#include<bits/stdc++.h>
using namespace std;
int n,m,a,b,xa[250001],ya[250001],xb[250001],yb[250001],maxx[250001];
int main()
{
    scanf("%d%d%d%d",&n,&m,&a,&b);
    for(int i=1;i<=a;i++)scanf("%d%d",&xa[i],&ya[i]);
    for(int i=1;i<=b;i++)scanf("%d%d",&xb[i],&yb[i]);
    memset(maxx,127,sizeof(maxx));
    for(int i=1;i<=b;i++)
        for(int j=1;j<=a;j++)
            maxx[i]=min(maxx[i],abs(xa[j]-xb[i])+abs(ya[j]-yb[i]));    //核心
    for(int i=1;i<=b;i++)printf("%d\n",maxx[i]);
    return 0;
}

```