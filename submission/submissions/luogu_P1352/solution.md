# P1352 题解

## 题目描述
某大学有N个职员，编号为1~N。他们之间有从属关系，也就是说他们的关系就像一棵以校长为根的树，父结点就是子结点的直接上司。现在有个周年庆宴会，宴会每邀请来一个职员都会增加一定的快乐指数Ri，但是呢，如果某个职员的上司来参加舞会了，那么这个职员就无论如何也不肯来参加舞会了。所以，请你编程计算，邀请哪些职员可以使快乐指数最大，求最大的快乐指数。

## 输入输出格式
###### 输入格式：
第一行一个整数N。(1<=N<=6000)

接下来N行，第i+1行表示i号职员的快乐指数Ri。(-128<=Ri<=127)

接下来N-1行，每行输入一对整数L,K。表示K是L的直接上司。

最后一行输入0 0

###### 输出格式：
输出最大的快乐指数。

## Solution:
经典的树形dp

设

  f[x][0]表示以x为根的子树,且x不参加舞会的最大快乐值
  
  f[x][1]表示以x为根的子树，且x参加了舞会的最大快乐值
  
  则f[x][0]=sigma{max(f[y][0],f[y][1])} (y是x的儿子)
  
  f[x][1]=sigma{f[y][0]}+h[x] (y是x的儿子)
  
  先找到唯一的树根root
  
  则ans=max(f[root][0],f[root][1])

```cpp
#include<bits/stdc++.h>
using namespace std;
#define MAXN 6005
int h[MAXN];
int v[MAXN];
vector<int> son[MAXN];
int f[MAXN][2];
void dp(int x)
{
 f[x][0]=0;
 f[x][1]=h[x];
 for(int i=0;i<son[x].size();i++)
 {
  int y=son[x][i];
  dp(y);
  f[x][0]+=max(f[y][0],f[y][1]);
  f[x][1]+=f[y][0];
 }
}
int main()
{
 int n;
 cin>>n;
 for(int i=1;i<=n;i++) cin>>h[i];
 for(int i=1;i<=n-1;i++)
 {
  int x,y;
  cin>>x>>y;
  son[y].push_back(x);
  v[x]=1;
 }
 int root;
 for(int i=1;i<=n;i++)
 if(!v[i]) {root=i;break;}
 dp(root);
 cout<<max(f[root][0],f[root][1])<<endl;
 return 0;
}

```