# P2661 题解

嗯……本人表示真的还不会toposort……所以，我就打了个奇奇怪怪的方法，居然也过了。

下面介绍一下我在本题的经历——

首先，我以为用set暴力判重能过，然而T了6个点。

然后，我彻夜不眠，思考着本题。然后，我就想出来了，然后就过了……

好吧，还是介绍一下思路。

可以把这些关系看成一个有向图。对于任意一个节点进入，因为每个点的出度均为1，所以最多只能构成三种情况：1、一条链；2、一个环链；3、一条链连接着一个环链。因为这三种情况极为的简单，所以就可以如下处理：

找任意一个点进入，记录到达每一个点所走过的遍数。当走到一个在这次查找中已经出现过的节点，即找到了一个环，用当前走到的步数减去在此节点原先记录的步数，便得到这个环的长度。由此搜遍所有点，找到这些环中最小长度的一个，并把它输出就可以了。

而如果就这样去做，会TLE，所以得再加一点优化。对于一次查找环中，由于此次查找中至多只有一个环，而此环已经确定，所以再有外部的链介入此环，它的状态仍然不变。所以可以加个判断，如果走到了已经被查找过的节点，便直接跳出。

下为代码，供大家参考：

```cpp
#include<cstdio>
#include<iostream>
#include<cstring>
#include<string>
#include<algorithm>
#include<cmath>
using namespace std;
int dx[300000];//存每一个人传话的对象
bool visit[300000]={0},novisit[300000]={0};//visit存每次查找中被查到的点，而novisit存每次查找前，已经被查找过的点（及不用继续查找了）
int bs[300000]={0};//每次查找中第一次到一个节点所经过的边数
int minn=2e9;
void dfs(int node,int num)
{
    if(novisit[node])return;//不需要继续找了
    if(visit[node])//在此次查找中出现过
    {
        minn=min(minn,num-bs[node]);//形成一个环，取最小值
    }
    else
    {
        visit[node]=true;//在此次循环中经过
        bs[node]=num;//记录第一次到达时的步数
        dfs(dx[node],num+1);//搜索
        novisit[node]=true;//已经搜过
    }
}
int main()
{
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
    {
        scanf("%d",&dx[i]);
    }
    for(int i=1;i<=n;i++)
    {
        dfs(i,0);//枚举全部节点
    }
    printf("%d",minn);//输出
    return 0;//时间复杂度O(n)
}
```