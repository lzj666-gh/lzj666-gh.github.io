# P2888 题解

再用佛洛依德进行新状态转移时，因为是以k作为中间点，所以牛跨过的最高高度是

max(d[i][k],d[k][j])，但是在i->j的整条路径上，跨过的最高高度应该最小，所以最后要取一个MIN，即d[i][j]=min(max(d[i][k],d[k][j]),d[i][j]);

```cpp
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<map>
#include<queue>
#define mod 100000007
#define inf 336860180
#define PI 3.1415926
#define ll long long
using namespace std;
int T,s,t,n,m,d[400][400];
int main()
{
    memset(d,20,sizeof(d));
    scanf("%d%d%d",&n,&m,&T);
    for(int i=1;i<=m;i++)
    {
     int x,y,h;scanf("%d%d%d",&x,&y,&h);
      d[x][y]=h;    
    }
    for(int k=1;k<=n;k++)
     for(int i=1;i<=n;i++)
      for(int j=1;j<=n;j++)
       d[i][j]=min(max(d[i][k],d[k][j]),d[i][j]);
       //重点 
    for(int i=1;i<=T;i++)
    {
      int x,y;scanf("%d%d",&x,&y);    
      if(d[x][y]!=inf) cout<<d[x][y]<<endl;
      else cout<<"-1"<<endl;//不要忘记这种情况啊 
    }
    return 0;
}
```