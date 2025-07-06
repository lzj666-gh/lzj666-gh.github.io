# P6974 题解

**思路**

由于 $n$ 有 $10^6$，所以不能直接模拟，要用数学来做。

思考：删除行会影响列，删除列会影响行。

如果没有删除任何行，那么第 $i$ 列的和为 $\frac{(n+1)\!\times\!n}{2}\!+\!n\!\times\!i$。

如果删除了一些行，剩余 $cr$ 行，这些行的行号之和为 $sr$，那么第 $i$ 列的和就为剩余行号之和加上剩余行数乘列号，转换为数学公式就是 $sr\!+\!cr\!\times\!i$。对于行同理。于是这道题就做出来了。

要注意一点，$n\!\times\!n$ 会超出 `int` 的范围。

**代码**

```cpp
#include<iostream>
using namespace std;
typedef long long ll;
const int N=1e6+5;
bool vr[N],vc[N];
/* (vr[i],vc[i])分别为第i（行，列）是否被删除 */
int main(){
	ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
	int n,q,m;
	ll cr,cc,sr,sc;
	char c;
	/* (cr,cc)分别为剩余的（行，列）数  (sr,sc)分别为剩余的（行号，列号）之和 */
	
	cin>>n>>q;
	cr=cc=n;sr=sc=cc*(n+1)/2;
	while(q--){
		cin>>c>>m;
		if(c=='R'){
			if(vr[m]){
				cout<<"0\n";
			}else{
				cout<<sc+m*cc<<'\n';
				/* 思路中有解释 */
				sr-=m;cr--;vr[m]=1;
			}
		}else{
			if(vc[m]){
				cout<<"0\n";
			}else{
				cout<<sr+m*cr<<'\n';
				sc-=m;cc--;vc[m]=1;
			}
		}
	}
	return 0;
}
```