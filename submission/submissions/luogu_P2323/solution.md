# P2323 题解

**首先，题目应该是有些水的。**
先说思路，其实非常清晰，因为它至少要有k条一级公路，所以先将一级公路的花费排序，用kruskal进行处理。然后再将剩下的公路根据二级公路的花费排序，用kruskal2进行处理，之后再将答案按题目要求排序即可。
```cpp
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
struct node
{
       int u;
       int v;
       int w1;
       int w2;
       int num;//num记读入边的顺序，后面的输出会用到 
}road[20005];
struct nodee
{
       int bh;
       int gl;
}ans[20005];
int flag=0;
int book[20005];//book存这条路有没有建造过 
int father[20005];//父节点 
int n,k,m,minn=0;//n，m，k如题 minn存花费最多的点的价值 
bool merge(int ,int );
int getfather(int );
void kruskal1();//建一级公路 
void kruskal2();//建二级公路 
bool cmp1(node ,node);//按一级公路花费排序 
bool cmp2(node ,node);//按二级公路花费排序 
bool cmp3(nodee ,nodee);//把答案按公路的序号顺序排序 
int main()
{
    scanf("%d%d%d",&n,&k,&m);
    memset(book,0,sizeof(book));
    for(int i=1;i<=n;i++)
            father[i]=i;
    for(int i=1;i<=m-1;i++)
    {
            scanf("%d%d%d%d",&road[i].u,&road[i].v,&road[i].w1,&road[i].w2);
            road[i].num=i;
    }//初始化准备 
    sort(road+1,road+m,cmp1);
    kruskal1();
    sort(road+1,road+m,cmp2);
    kruskal2();
    sort(ans+1,ans+n,cmp3);
    printf("%d\n",minn);
    for(int i=1;i<=n-1;i++)
            printf("%d %d\n",ans[i].bh,ans[i].gl);
    getchar();
    getchar();
    return 0;
}
bool cmp1(node x,node y)
{
      return x.w1<y.w1;
}
bool cmp2(node x,node y)
{
     return x.w2<y.w2;
}
bool cmp3(nodee x,nodee y)
{
     return x.bh<y.bh;
}
int getfather(int x)
{
    if(x==father[x])
                    return x;
    else
    {
        father[x]=getfather(father[x]);
        return father[x];
    }
}
bool merge(int x,int y)
{
     int f1=getfather(x),f2=getfather(y);
     if(f1==f2)
               return false;
     else
     {
         father[f2]=f1;
         return true;
     }
}
void kruskal1()
{
     int step=0;
     for(int i=1;i<=m-1;i++)
     {
             if(book[road[i].num]==0)//这个公路的序号在book中没有被用过 
                           if(merge(road[i].u,road[i].v))
                           {
                                                         book[road[i].num]=1;
                                                         flag++;
                                                         step++;
                                                         minn=max(minn,road[i].w1);
                                                         ans[flag].bh=road[i].num;
                                                         ans[flag].gl=1;
                           }
             if(step==k)
                        return ;
     }
}
void kruskal2()
{
     int step=0;
     for(int i=1;i<=m-1;i++)
     {
             if(book[road[i].num]==0)//这个公路的序号在book中没有被用过 
                           if(merge(road[i].u,road[i].v))
                           {
                                                         book[road[i].num]=1;
                                                         flag++;
                                                         step++;
                                                         minn=max(minn,road[i].w2);
                                                         ans[flag].bh=road[i].num;
                                                         ans[flag].gl=2;
                           }
             if(step==n-1-k)
                        return ;
     }
}
```
下来说说题水在何处

- 题目的要求（即二分答案）在测试数据中根本没有体现，因为题目只说至少k条一级公路，没说不能超过k条。万一有要建造的二级公路的花费比前面k条一级公路花费高怎么办？那就只能再建一条一级公路（保证建的这条比另一条二级公路花费少）
- 没有要求建造公路的总费用最小，kruskal求最小生成树的一个特性直接被忽略了

接下来大致说一下如果这题不水该怎么合理ac

大致思路：
**唯一不同：建两个邻接表 一个存一级公路花费时间 一个存二级公路花费时间**
```cpp
void kruskal1()
{
     int step=0;
     for(int i=1;i<=m-1;i++)
     {
             if(book[road[i].num]==0)//这个公路的序号在book中没有被用过 
                           if(merge(road[i].u,road[i].v))
                           {
                                                         book[road[i].num]=1;
                                                         flag++;
                                                         step++;
                                                         minn=max(minn,road[i].w1);
                                                         ans[flag].bh=road[i].num;
                                                         ans[flag].gl=1;
                           }
             if(step==k)//此处改为找到一个就返回
                        return ;
     }
}
```
这样 先循环k次kruskal1，这个过程中要删除已经建了的边，然后循环完毕后，再用sort1排序一次存一级公路花费的邻接表，再用sort2。然后比较现在的最小的一级公路花费和二级公路花费。如果前小于后，继续建造一级公路，重复上述操作，直到二级公路花费大于一级公路。然后用一次kruskal2.

这里其实就用了**贪心**或者说**二分答案**的思想，两者在此题中都可以解释。