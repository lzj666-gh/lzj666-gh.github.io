# P1948 题解

###本题的解法：二分答案+spfa###

首先概括一下题意：求原点1到n的所有路中的第k+1长的路最小。

**思考**：为什么可以这样概括呢？因为题意中的答案要最小，我们贪心肯定要使k次免费的资格用完，那么最划算的方案肯定是拿最长的k条路使之免费，然后付第k+1长路的长度的钱。。。这样的贪心思路显然是正确的。

**思路**：我们首先二分第k+1长的路的长度(即答案)，边界值l显然是0、r是1000000(题目中说边最长为1000000)，然后关键是如何判断正确性。我们考虑简化问题，对于长度小于二分出的答案的线段，因为不需要付价钱，所以可以将其权值看作是0;同理，大于二分的值的路径，我们将长度看作1(意味着我需要使用1次免费的资格)。so，我们跑一遍spfa，看到了n点的最短路的长度，如果大于k，则不行，缩小r范围继续二分;如果小于，则有可能更小，缩小l范围继续二分。

```cpp
#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cstdlib>
using namespace std;
#define ll long long 
#define il inline
struct edge{
int to,next,v;
}e[20005];
int n,p,k,cnt,h[1005],dis[1005],q[1005];
bool pd[1005];
il void add(int u,int v,int w){
    e[++cnt].to=v;
    e[cnt].v=w;
    e[cnt].next=h[u];
    h[u]=cnt;
}
il bool check(int x)
{
         memset(dis,0x3f,sizeof(dis));
    int t=0,w=1,i,now,s;
         dis[1]=0;q[t]=1;pd[1]=1;
    while(t!=w)
     {
        now=q[t];t++;
        if(t==1001)t=0;
        i=h[now];
            while(i){
                if(e[i].v>x)s=dis[now]+1;
                else s=dis[now];
                if(s<dis[e[i].to])
                    {
                        dis[e[i].to]=s;
                        if(!pd[e[i].to])
                            {
                                q[w++]=e[i].to;
                                pd[e[i].to]=1;
                                if(w==1001)w=0;
                            }
                    }
                    i=e[i].next;
                    }
            pd[now]=0; 
        }
     if(dis[n]<=k)return 1;
     return 0;
 }
int main()
{
    //freopen("phoneline.in","r",stdin);
    //freopen("phoneline.out","w",stdout);
    scanf("%d%d%d",&n,&p,&k);
    int u,v,w,l=0,r=1000000,mid;
    for(int i=1;i<=p;i++){
            scanf("%d%d%d",&u,&v,&w);
            add(u,v,w);
            add(v,u,w);
    }
    int ans=-1;
    while(l<=r){
                   mid=(l+r)>>1;
            if(check(mid)){r=mid-1;ans=mid;}
            else l=mid+1;
    }
    cout<<ans;
    return 0;
}
```