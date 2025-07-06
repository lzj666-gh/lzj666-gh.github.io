# P7076 题解

upd on 2020.11.17：修正一个错误。

[题目传送门](https://www.luogu.com.cn/problem/P7076)。

先开一个数组 $buc_j$ 表示是否有 $a_i$ 的第 $j$ 位上是 $1$。

又看到题目中保证 $q_i$ 互不相同，所以一旦出现 $p_i,q_i$ 满足 $buc_{p_i}=0$，那么这一位就不能选，因为当前买的饲料中必定没有 $q_i$。

不妨设剩下来 $bit$ 位，那么这 $bit$ 位既可以是 $0$ 也可以是 $1$，共有 $2^{bit}$ 种动物，减去现有的 $n$ 种动物即可。

注意要特判 $bit=64,n=0$ 的情况。读入量较大，建议写快读。

此外 $buc$ 数组可以用 unsigned long long 变量代替，这样就做到了时间 $O(n+m)$，空间 $O(1)$。

非考场代码：

```cpp
#include <bits/stdc++.h>
using namespace std;

#define ull unsigned long long
#define gc getchar()

inline ull rd(){
	ull x=0; char s=gc;
	while(!isdigit(s))s=gc;
	while(isdigit(s))x=(x<<1)+(x<<3)+s-'0',s=gc;
	return x;
} ull n,m,c,k,ans,lim,hv;

int main(){
	n=rd(),m=rd(),c=rd(),k=rd();
	for(int i=1;i<=n;i++)hv|=rd(); // 统计每个位是否有 1
	for(int i=1;i<=m;i++)lim|=1ull<<rd(),rd(); // 统计有限制的位
	for(int i=0;i<k;i++)ans+=!((lim>>i)&1)||((hv>>i)&1); // 如果当前位有 1, 或者没有限制，那么都可以选
	if(ans==64&&!n)puts("18446744073709551616");
	else cout<<(ans==64?-n:(1ull<<ans)-n)<<endl;
	return 0;
}
```