# P1396 题解

都是打**最短路**或是**克鲁斯卡尔重构树**的吗??!!

我原本也想打一个**克鲁斯卡尔重构树**水过去,但后来发现~~完全没必要那么麻烦~~,一个**克鲁斯卡尔最小生成树**就可以水过去了

将边从小到大排序,然后克鲁斯卡尔最小生成树连边,这样当S和T第一次联通时,当前边的权值就是答案了.
```
#include<bits/stdc++.h>
using namespace std;
int n,m,s,t,a[20001];
struct each
{
    int x,y,cost;
}b[20001];//存边
bool com(each x,each y)
{
    return x.cost<y.cost;
}
int read()//读入优化模板
{
    char ch=getchar();
    int x=0,f=1;
    while(ch<'0'||ch>'9')
        {
        if(ch=='-')
            f=-1;
        ch=getchar();
        }
    while(ch>='0'&&ch<='9')
        {
        x=x*10+ch-'0';
        ch=getchar();
        }
    return x*f;
}
int find(int x)//并查集基本操作
{
    if(a[x]==0)
        return x;
    a[x]=find(a[x]);
    return a[x];
}
int main()
{
    n=read();
    m=read();
    s=read();
    t=read();
    for(int i=1;i<=m;i++)//无脑输入
        {
        b[i].x=read();
        b[i].y=read();
        b[i].cost=read();
        }
    sort(b+1,b+m+1,com);//排序
    for(int i=1;i<=m;i++)//克鲁斯卡尔最小生成树连边
        {
        int X=find(b[i].x),Y=find(b[i].y);
        if(X!=Y)
            a[X]=Y;
        if(find(s)==find(t))//如果联通直接输出退出
            {
            cout<<b[i].cost<<endl;
            return 0;
            }
        }
    return 0;
}
```