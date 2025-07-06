# P1731 题解

[题面传送门](https://www.luogu.org/problem/show?pid=1731)

###如果不懂DFS，请自觉睡觉；

###如果不懂剪枝，请自觉睡觉；


啊哈，大家的思路一定和我一样——DFS，找个数组存储半径和高，可是如单单使用DFS不加剪枝的话，10分——20分。

所以，我们来想一想如何剪枝

###1.当前的奶油面积+之后的最小奶油面积>现在已求出的的最小奶油面积——果断return；

###2.当前的体积>n,return;

###3.当前的体积+之后的最大体积<体积总数，果断return；

###4.发现每次枚举半径和高时，是从上一个的半径和高，***到还剩下的层数***。为什么呢，是因为每一层的半径和高都要比下一层的小1，所以你得每一层都留一个1，so，是从上一个的半径和高，***到还剩下的层数***；

OK，现在我们加上剪枝之后就可以A了

```cpp
#include<cstdio>
#include<cstring>
#include<iostream>
#include<cmath>
using namespace std;
int r[30],h[30],minn=2147483647,n,m;
void dfs(int x,int y,int k,int z)
{  if(y<0) return;
    if(x>m+1) return;
     if(k>=minn) return;
    if(y==0&&x==m+1)
    {  k+=r[1]*r[1];
         if(k<minn) minn=k;
         return;
    }
    if(k+z+r[1]*r[1]>minn) return;
   if(y-(r[x-1])*(r[x-1])*(h[x-1])*z>0) return;
    for(int i=r[x-1]-1;i>=z;i--)
      for(int j=h[x-1]-1;j>=z;j--)
      {
            if(y-i*i*j>=0&&x+1<=m+1)
             {     r[x]=i;
                   h[x]=j;
                    dfs(x+1,y-i*i*j,k+(i*2*j),z-1);
                   h[x]=0;
                   r[x]=0;
             }
      }
}
int main()
{
    scanf("%d%d",&n,&m);
    r[0]=(int)sqrt(n);
    h[0]=(int)sqrt(n);
    dfs(1,n,0,m);
    if(minn==2147483647) printf("%d",0);
      else printf("%d",minn);
    return 0;
}
```
记得，顶一下
