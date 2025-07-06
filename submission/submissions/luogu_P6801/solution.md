# P6801 题解

> [题面传送门](https://www.luogu.com.cn/problem/P6801)。

> 题意简述：$n$ 个 $h_i\times w_i$ 的矩形从左往右排成一排，求出整个图形中共包含多少个小矩形。

---

看到题目，考虑维护一个**高度单调递增**的单调栈。

不妨设：
- 将当前要加入的矩形为 $a$，高度为 $h$。
- 单调栈栈顶矩形为 $x$，高度为 $h_1$，宽为 $w_1$。
- 单调栈栈顶前一个矩形为 $y$，高度为 $h_2$。

如果 $h_1\ge h$，那么将 $x$ 多余的高度 “削去”。具体而言，我们要将 $x$ 削到和「**$a,y$ 中高度较高的那个矩形**」一样高，即高度变为 $\max(h,h_2)$。

我们需要求出削去该矩形对答案的贡献，即求出「四边都落在 $x\ (h_1\times w_1)$ 内部（包括边界）且至少有一边落在被削去矩形 $((h_1-\max(h,h_2))\times w_1)$ 内部（**仅包括左，上，右边界**）」的矩形个数。

根据容斥原理，也就是求出「四边都落在 $x\ (h_1\times w_1)$ 内部（包括边界）」的矩形个数减去「四边都落在 $x$ 削去后剩下的矩形 $(\max(h,h_2)\times w_1)$ 内部（包括边界）」的矩形个数。

对于一个 $h\times w$ 的矩形，如何求出它包含了多少小矩形：因为任选两条横着的边，任选两条竖着的边，都能围成一个独一无二的小矩形，且一共有 $w+1$ 条横着的边，$h+1$ 条竖着的边，所以小矩形的个数为 $\binom{w+1}{2}\times\binom{h+1}{2}$。

需要注意考虑边界条件，可以适当在单调栈内添加矩形以避免特判。

根据上述思路，不难写出代码如下：

```cpp
stack <int> a,b;
int n,w[N],h[N],ans;

int calc(int x){return 1ll*x*(x+1)/2%mod;}
int main(){
	n=read(),a.push(-1);
	for(int i=1;i<=n;i++)h[i]=read(); 
	for(int i=1;i<=n;i++)w[i]=read();
	for(int i=1,s=0;i<=n+1;i++,s=0){
		while(h[i]<=a.top()){
			int hh=a.top(),ww=b.top(); a.pop(),b.pop(),s=(s+ww)%mod;
			ans=(ans+1ll*(calc(hh)-calc(max(h[i],a.top()))+mod)*calc(s))%mod;
		} a.push(h[i]),b.push((w[i]+s)%mod);
	} cout<<ans<<endl;
	return 0;
}
```

求赞 qwq。