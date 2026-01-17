# P2419 题解

floyed算法

floyed不仅能求任意两点的最短路，还能求一个点能否到另一个点。

f[i][j]=f[i][j]|(f[i][k]&f[k][j])表示i能否走到j，即要么一开始i能到j,要么i能到k，k再能到j。

那么这里表示的是i能否赢j。用floyed求出每个点与个点的关系，只要这个点和其他

n-1个点的关系都确定了，就能确定他的排名。

代码
```cpp
#include<iostream>
#include<cstdio>
using namespace std;
int a,b,n,m,f[101][101],ans;
int main(){
    scanf("%d%d",&n,&m);
    for(int i=1;i<=m;i++){
        scanf("%d%d",&a,&b);
        f[a][b]=1;
    }
    for(int k=1;k<=n;k++)
        for(int i=1;i<=n;i++)
            for(int j=1;j<=n;j++)
              f[i][j]=f[i][j]|f[i][k]&f[k][j];
    for(int i=1;i<=n;i++){
        int gg=1;
        for(int j=1;j<=n;j++)
        if(i==j)continue;else 
         gg=gg&(f[i][j]|f[j][i]);
         ans+=gg;
    }
    printf("%d\n",ans);
}
```