# P1525 题解

淳朴的并查集~但因为它们带有权值，因此排序是必须的，我们要尽可能让危害大的罪犯在两个监狱里。

那么，再结合敌人的敌人和自己在一个监狱的规律合并。

当查找时发现其中两个罪犯不可避免地碰撞到一起时，只能将其输出并结束。

还有一点很重要，就是没有冲突时一定输出0！！！








```cpp
#include <cstdio>
#include <algorithm>
using namespace std;
struct data {int x,y,z;};//结构体便于排序的变换
data f[100005];
int n,m,a[20005],b[20005],i;
inline bool cmp(data a,data b)//重写cmp函数
{
    return a.z>b.z;
}
inline int find(int x)
{
    if(a[x]==x) return x;
    a[x]=find(a[x]);
    return a[x];
}
inline void ad(int x,int y)//合并
{
    x=find(a[x]);
    y=find(a[y]);
    a[x]=y;
}
inline bool check(int x,int y)//查找
{
    x=find(x);
    y=find(y);
    if(x==y) return true;
    return false;
}
int main()
{
    scanf("%d%d",&n,&m);
    for(i=1;i<=n;i++) a[i]=i;
    for(i=1;i<=m;i++)
        scanf("%d%d%d",&f[i].x,&f[i].y,&f[i].z);
    sort(f+1,f+m+1,cmp);//c党的优越感~
    for(i=1;i<=m+1;i++)//为什么m+1呢？如果运行到m+1会输出0，想想为什么。
    {
        if(check(f[i].x,f[i].y)) {printf("%d",f[i].z);break;}//如果两个罪犯已经在同一监狱就输出 ，并退出
        else
        {
            if(!b[f[i].x]) b[f[i].x]=f[i].y;//标记“敌人”
                else {ad(b[f[i].x],f[i].y);}//将敌人的敌人合并
            if(!b[f[i].y]) b[f[i].y]=f[i].x;
                else {ad(b[f[i].y],f[i].x);}
        }
    }
    return 0;
}
```