# P7965 题解

话说这道题目的标签是认真的吗？这不是个并查集板子题吗？

根据题意我们得到，编号为 $i$ 的玩具可以放在编号为 $p_i$。又因为 $p_i$ 是一个排列，所以我们可以写一个并查集，在 $i$ 和 $p_i$ 之间建立关系，依此给 $m$ 个人处理关系。然后对于下面的询问，我们套用并查集模板的查询函数进行比较，如果 $x$ 和 $y$ 的返回值一样，那么说明它们之间是存在关系的，下面是完整代码：

```cpp
#include<bits/stdc++.h>
#define ll long long
#define F(i,a,b) for (int i=a;i<=b;i++)
#define Test ios::sync_with_stdio(false),cin.tie(nullptr),cout.tie(nullptr)
using namespace std;
const int N=1e7+10,NN=1e4+10;
ll n,m,k,x,y,u,v,w,cnt=0,ans=0,t=0,l,r,len,T;
ll mini=INT_MAX,maxi=0,Mod;
string s1,s2;
ll f[N];
ll find(ll x){//并查集 
	if(f[x]==x) return x;
	return f[x]=find(f[x]);
}
string check(ll x,ll y){//检查答案 
	if(find(x)==find(y)) return "DA\n"; 
	return "NE\n";
}
int main(){
	Test;
	cin>>n>>m>>k;
	F(i,1,n) f[i]=i;//并查集预处理 
	F(i,1,m) F(j,1,n) cin>>x,f[find(x)]=find(j);//建立关系 
	F(i,1,k){
		cin>>x>>y;
		cout<<check(x,y);//判断是否符合答案 
	} 
	return 0;
}

```
