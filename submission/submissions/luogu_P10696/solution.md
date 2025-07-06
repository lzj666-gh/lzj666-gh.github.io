# P10696 题解

[![](https://img.shields.io/badge/题目-P10696_[SNCPC2024]_写都写了，交一发吧-yellow)
![](https://img.shields.io/badge/难度-入门-red)
![](https://img.shields.io/badge/考点-二进制-blue)
![](https://img.shields.io/badge/题型-传统题-green)](https://www.luogu.com.cn/problem/P10696)
[![](https://img.shields.io/badge/作者-wangbinfeng(387009)-purple)](https://www.luogu.com.cn/user/387009)

------------
本题是比赛的签到题，线下赛共计 $118$ 个队伍通过。

- 定理 $1$：$\forall i,j\in\N^+,\;i\operatorname{\;and\;}j\le\min(i,j)$。
> 证明：对于任意一个正整数对其他正整数做按位与（且）运算，它在二进制下相应位的 $0$ 不可能变为 $1$，但相应位的 $1$ 存在变为 $0$ 的可能（只需与其按位与的数相应位为 $0$ 即可）。
- 定理 $2$：$\forall i\in\N^+,\;i\operatorname{\;and\;}i=i$。
> 证明：对于在二进制下的任意位，如果已经为 $1$ 则一定还为 $1$，为 $0$ 则一定也只能还为 $0$。

那么，总结一下两个定理，得出 $\forall i,j\in\N^+,\;i\operatorname{\;and\;}j\le\min(i,j)\le\max(i,j)=\max(i,j)\operatorname{\;and\;}\max(i,j)$。

从两个数拓展到 $n$ 个数可以显然证明结论不变。

代码：
```cpp
#include<bits/stdc++.h>
using namespace std;
#define int long long
const int maxn=159;
int t,ans,n;
signed main(){
	ios::sync_with_stdio(false),cin.tie(nullptr),cout.tie(nullptr);
	for(cin>>t;t--;ans=0){
		cin>>n;
		for(int i=1,x;i<=n;i++)cin>>x,ans=max(ans,x);
		cout<<ans<<'\n'; 
	}
}
```