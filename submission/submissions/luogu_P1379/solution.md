# P1379 题解

上次发过超长代码的题解后惨遭同校大佬批斗


痛定思痛，在向大佬学习之后，带来最短代码（滑稽）

思路大体与之前相同：

map去重，

在这里只需要一个队列，因为需要较少步数达到的状态一定在步数较多的状态前入队列

（我之前那个最长程序也可以用一个队列，不需要两个队列辗转，只要加个步数的记录就行了）


stl大法好%%%


```cpp
#include<iostream>
#include<map>
#include<queue>
#include<algorithm>
#define ll long long//在这里看到一种很骚的操作：直接把int定义成long long；main函数用signed类型--麻麻再也不怕我忘开long long了！
using namespace std;
const ll dx[]={-1,0,0,1},dy[]={0,-1,1,0};//转移数组；
ll n;
int  main()
{
    cin>>n;
    queue<ll> q;
    q.push(n);
    map<ll,ll> m;
    m[n]=0;
    while(!q.empty())
    {
        int u=q.front(); //初始状态入队列
        int c[3][3],f=0,g=0,n=u;q.pop();
        if(u==123804765)break;
        for(ll i=2;i>=0;i--)
            for(ll j=2;j>=0;j--)
            {
                c[i][j]=n%10,n/=10;
                if(!c[i][j])f=i,g=j;
            }
        for(ll i=0;i<4;i++)
        {
            ll nx=f+dx[i],ny=g+dy[i],ns=0;
            if(nx<0||ny<0||nx>2||ny>2)continue; //越界就不执行
            swap(c[nx][ny],c[f][g]);
            for(ll i=0;i<3;i++)
                for(ll j=0;j<3;j++)ns=ns*10+c[i][j];//矩阵转数列 
            if(!m.count(ns))
            {
                m[ns]=m[u]+1;//map去重的同时顺便统计到达这个状态所需的步数
                q.push(ns);
            }
            swap(c[nx][ny],c[f][g]);//状态复原
        }
    }
    cout<<m[123804765]<<endl; // map的下标直接用数列表示
    return 0;
}

```