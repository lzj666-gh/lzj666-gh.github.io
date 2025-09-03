# P12000 题解

### 前情提要

这场比赛赛时 C 题与 F 题分别因未开 long long 分别从 $100\rightarrow30$ 和 $150\rightarrow0$ ，$220$ 分就这样没了。

### 分析

显然，本题答案具有单调性，可以使用二分答案。二分出一个值后，可以利用贪心的思想判断。具体的，先利用单调栈预处理每个位置下一个更优的位置在哪，再贪心的选取，尽量保证游戏币的数量能撑到下一个更优的位置，如果已是最优的，就全换。详见代码。

### 代码

赛时：

```cpp
#include<bits/stdc++.h>
using namespace std;
#define ll long long
const int N=1e6+3;
int T,n,a[N],b[N],p[N];
ll now,sum,l,r;
bool chk(int x){
	now=sum=0;
	for(int i=1;i<=n;i++){
		sum+=b[i];
		if(p[i]){
			if(now<1ll*(p[i]-i)*x){
				ll t=1ll*(p[i]-i)*x-now,l=min(t/a[i]+(t%a[i]>0),sum);
				now+=l*a[i],sum-=l;
			}
		}else now+=sum*a[i],sum=0;
		now-=x;
		if(now<0)return 0;
	}
	return 1;
}
int main(){
	cin.tie(0)->sync_with_stdio(0);
	cin>>T;
	while(T--){
		cin>>n;
		for(int i=1;i<=n;i++)cin>>a[i];
		for(int i=1;i<=n;i++)cin>>b[i];
		stack<int>s;
		for(int i=n;i;i--){
			while(!s.empty()&&a[s.top()]<=a[i])s.pop();
			p[i]=s.empty()?0:s.top();
			s.push(i);
		}
		l=0,r=1e12;
		while(l<r){
			int mid=(l+r)/2+1;
			if(chk(mid))l=mid;
			else r=mid-1;
		}
		cout<<l<<'\n';
	}
}
```

赛后：

```cpp
#include<bits/stdc++.h>
using namespace std;
#define ll long long
const int N=1e6+3;
int T,n,a[N],b[N],p[N];
ll now,sum,l,r;
bool chk(ll x){
	now=sum=0;
	for(int i=1;i<=n;i++){
		sum+=b[i];
		if(p[i]){
			if(now<1ll*(p[i]-i)*x){
				ll t=1ll*(p[i]-i)*x-now,l=min(t/a[i]+(t%a[i]>0),sum);
				now+=l*a[i],sum-=l;
			}
		}else now+=sum*a[i],sum=0;
		now-=x;
		if(now<0)return 0;
	}
	return 1;
}
int main(){
	cin.tie(0)->sync_with_stdio(0);
	cin>>T;
	while(T--){
		cin>>n;
		for(int i=1;i<=n;i++)cin>>a[i];
		for(int i=1;i<=n;i++)cin>>b[i];
		stack<int>s;
		for(int i=n;i;i--){
			while(!s.empty()&&a[s.top()]<=a[i])s.pop();
			p[i]=s.empty()?0:s.top();
			s.push(i);
		}
		l=0,r=1e12;
		while(l<r){
			ll mid=(l+r)/2+1;
			if(chk(mid))l=mid;
			else r=mid-1;
		}
		cout<<l<<'\n';
	}
}
```