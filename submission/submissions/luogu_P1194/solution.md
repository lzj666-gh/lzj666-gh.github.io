# P1194 题解

这道题如果看出题目实质就变得很简单了，不过看不穿的话就会很难想了。

大致思路如下：

第i件物品对j有优惠的话就建边，然后从0向各点连边权为a的边，然后跑一边kruskal就OK了。

```cpp
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;
struct node
{
        int u,v,w;
}e[250000];
int a,b,k,tot=1,ans,f[555];
bool cmp(node x,node y)
{
        return x.w<y.w;
}
int find(int x)
{
        if(f[x]==x) return x;
        return f[x]=find(f[x]);
}
int hb(int x,int y)
{
        int xx=find(x);
        int yy=find(y);
        if(xx!=yy) f[xx]=yy;
}
void build(int x,int y,int z)
{
        k++;
        e[k].u=x;
        e[k].v=y;
        e[k].w=z;
}
void kruskal()
{
        int j=1;
        while(j<=k&&tot<=b)
    {
            if(find(e[j].u)!=find(e[j].v))
            {
                    tot++;
                    ans+=e[j].w;
                    hb(e[j].u,e[j].v);
                    //printf("%d->%d\n",e[j].u,e[j].v);
            }
            j++;
        }
}
int main()
{
        scanf("%d%d",&a,&b);
        for(int i=1;i<=b;i++)
        {
                for(int j=1;j<=b;j++)
                {
                        int x;
                        scanf("%d",&x);
                        if(i<j&&x!=0) build(i,j,x);//千万记得没有优惠是0，不建边（我在这儿WA了三次......）
                }
        }
        for(int i=1;i<=b;i++) build(0,i,a);
        for(int i=0;i<=b;i++) f[i]=i;
        sort(e+1,e+k+1,cmp);
        kruskal();
        //for(int i=1;i<=k;i++)
        //printf("%d->%d:%d\n",e[i].u,e[i].v,e[i].w);
        printf("%d\n",ans);
        return 0;
}
```