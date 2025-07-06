# P11008 题解

# P11008 解题报告

## 前言

$n^2$ 过百万，暴力踩标算。

## 思路分析

我们要充分发扬人类智慧。

考虑乱搞。

首先我们可以枚举 $a_1$ 的取值，然后递推得到序列 $a$，再判断 $a$ 是否合法。这样时间复杂度为 $O(n^2)$。

考虑对这个暴力做法剪枝。

对序列 $b$ 求异或前缀和，得到序列 $c$。不难发现，$c_i = a_1 \oplus a_{i+1}$。

考虑 $a_1$ 有什么限制。

因为 $a$ 是 $[1,n]$ 的排列，所以 $\forall i \in [1,n-1],c_i \ne a_1$。否则一定 $\exist i \in [1,n],a_i = 0$，而这样是不合法的。

因为 $c_i \in [1,2^{\left \lceil \log a_j \right \rceil }],i \in [1,n-1],j \in [1,n]$，所以这个剪枝帮我们去掉了至少一半的不合法情况。

然后就可以枚举 $a_1$，判断序列 $a$ 是否是一个排列了。因为题目保证有解，所以序列 $c$ 中元素互不相同。这样，我们只需要保证 $a_i \le n$ 即可。显然，从小到大枚举 $a_1$ 是更优的。

这样做跑的飞快，甚至挤到了最优解第二页。

## 代码实现

最好写的一集。

```cpp
#include<bits/stdc++.h>
using namespace std;
int t,n,a[2000005],b[2000005],vis[2000005];
bool check(int x){
	if(vis[x]) return false;
	for(int i=2;i<=n;i++){
		if((x^b[i])>n) return false;
	}
	return true;
}
int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin>>t;
	while(t--){
		cin>>n;
		for(int i=2;i<=n;i++){
			cin>>a[i];
			b[i]=b[i-1]^a[i]; 
			vis[b[i]]=1;
		}
		for(int i=1;i<=n;i++){
			if(check(i)){
				a[1]=i;
				for(int j=2;j<=n;j++){
					vis[b[j]]=0;
					a[j]^=a[j-1];
				}
				for(int j=1;j<=n;j++){
					cout<<a[j]<<' ';
				} 
				cout<<'\n'; 
				break;
			}
		}
	}
    return 0;
}
```

[AC 记录](https://www.luogu.com.cn/record/174815903)

## 后记

欢迎 hack / 复杂度分析。

感觉 hack 的构造思路是让 $a_1$ 尽可能大，同时让 $c$ 尽可能大，但是我并不会卡。

祝点赞的各位 $CSP / NOIP$ $rp++$ 。