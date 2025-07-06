# P4170 题解

题意：给个没有任何颜色的序列，你每次可以选一段区间覆盖上一种颜色，给个目标状态，求达到它的最小步数。

我断言一定存在一种最优的方案满足对于任意两次染色：它们的区间要么不交，要么靠后的那次被靠前的那次包含并且不共端点。

证明只是反证法然后做一些分类讨论。比如，如果两次染色的区间相交但不包含，你可以缩短靠前的那次的区间使它们变得不相交，但不改变最终的结果。接下来我们只讨论满足上面条件的染色方案

设 $f_{l,r}$ 为给区间 $[l,r]$ 染色的最小步数。边界显然是 $f_{i,i}=1$。若 $l<r$ 则考虑两种情况：
- $s_l=s_r$。首先显然有 $f_{l,r}\ge f_{l,r-1}$。然后考虑对 $[l,r-1]$ 染色的方案，设覆盖了 $l$ 的唯一一次染色的右端点是 $x$。我们把这次染色的右端点改成 $r$，并且把所有在 $[x+1,r]$ 上进行的染色保持原来的顺序挪到这次染色之后，这样我们在不改变步数的情况下从一个对 $[l,r-1]$ 染色的方案得到了一个对 $[l,r]$ 染色的方案。故 $f_{l,r}=f_{l,r-1}$。
- $s_l\ne s_r$。此时不存在一次覆盖了 $[l,r]$ 的染色，故必然存在一个位置 $l\le x<r$ 使得不存在一次左端点小于等于 $x$ 且右端点大于 $x$ 的染色，枚举这个 $x$ 即可。即 $f_{l,r}=\min\limits_{i=l}^{r-1}f_{l,i}+f_{i+1,r}$。

于是我们在 $O(n^3)$ 时间和 $O(n^2)$ 空间内完整解决了问题。
```cpp
#include<bits/stdc++.h>
using namespace std;
using ll=long long;
inline ll read(){
	ll x=0;
	bool f=0;
	char c=getchar();
	while(!isdigit(c)){
		if(c=='-') f=1;
		c=getchar();
	}
	while(isdigit(c)){
		x=x*10+c-'0';
		c=getchar();
	}
	return f?-x:x;
}
const int maxn=50+5;
int n;
char s[maxn];
int f[maxn][maxn];
int main(){
#ifdef LOCAL
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
#endif
	scanf("%s",s+1);
	n=strlen(s+1);
	for(int i=n;i>0;i--) for(int j=i;j<=n;j++){
		if(i==j) f[i][j]=1;
		else if(s[i]==s[j]) f[i][j]=f[i][j-1];
		else{
			f[i][j]=n;
			for(int k=i;k<j;k++)
				f[i][j]=min(f[i][j],f[i][k]+f[k+1][j]);
		}
	}
	printf("%d\n",f[1][n]);
#ifdef LOCAL
	fprintf(stderr,"%f\n",1.0*clock()/CLOCKS_PER_SEC);
#endif
	return 0;
}
```