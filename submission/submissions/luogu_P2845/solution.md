# P2845 题解

标签里说的广搜实际上深搜也是可以做的……

代码的主要部分是深搜，visited数组用来标记到达过的点（没有这个会死循环），b数组用来标记可以到达（已经开灯）的点。

另外，为了防止暴力找边（100\*100），我很快乐的用了二维邻接表（话说我已经被链式向前星洗脑了，建表就用len、head数组和a数组。

有一个很重要的操作，就是当点亮一间房时，如果这间房旁边有已到达的点，就直接深搜这间被点亮的房间（相当于完成之前那间房没有完成的任务）。

代码如下：

```cpp
#include<iostream>
#include<cstdio>
inline int getint()
{
    int s=0,w=1;
    char ch=getchar();
    while (ch!='-'&&(ch<'0'||ch>'9'))ch=getchar();
    if (ch=='-')w=-w,ch=getchar();
    while (ch>='0'&&ch<='9')s=s*10+ch-'0',ch=getchar();
    return s*w;
}
using namespace std;
struct node
{
    int tx,ty,nt;
}a[200005];
int n,m,head[105][105],len,b[105][105],v[105][105],c;
void dfs(int x,int y)
{
    if (x<1||x>n||y<1||y>n)return;
    v[x][y]=1;
    for (int i=head[x][y];i!=0;i=a[i].nt)
    if (b[a[i].tx][a[i].ty]==0)
    {
        b[a[i].tx][a[i].ty]=1;
        c++;
        if (v[a[i].tx+1][a[i].ty]==1||v[a[i].tx][a[i].ty+1]==1||v[a[i].tx-1][a[i].ty]==1||v[a[i].tx][a[i].ty-1]==1)dfs(a[i].tx,a[i].ty);
    }
    if (v[x+1][y]==0&&b[x+1][y]==1)dfs(x+1,y);
    if (v[x][y+1]==0&&b[x][y+1]==1)dfs(x,y+1);
    if (v[x-1][y]==0&&b[x-1][y]==1)dfs(x-1,y);
    if (v[x][y-1]==0&&b[x][y-1]==1)dfs(x,y-1);
}
int main()
{
    n=getint();
    m=getint();
    int fx,fy,tx,ty;
    for (int i=1;i<=m;i++)
    {
        fx=getint();
        fy=getint();
        tx=getint();
        ty=getint();
        a[++len].tx=tx;
        a[len].ty=ty;
        a[len].nt=head[fx][fy];
        head[fx][fy]=len;
    }
    b[1][1]=1;
    c=1;
    dfs(1,1);
    printf("%d",c);
}
```