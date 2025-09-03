# P6525 题解

> [题面传送门](https://www.luogu.com.cn/problem/P6525)。

> 题意简述：从给出的 $n$ 个数中选出若干个数 $b_1,b_2,\cdots,b_m$，其分值为 $m\times \max b_i$。求所有满足存在 $i,j,k$ 使得 $b_i,b_j,b_k$ 能组成一个三角形的方案的分值之和。

题目还是挺不错的，如果模数是质数 / 不卡空间就更棒了。

---

正着算不方便，考虑用所有方案减去不满足的方案。

首先将给定的数从小到大排序，然后从左往右 DP：设 $l_{i,j},c_{i,j}$ 分别为倒数第二个数是 $a_i$，倒数第一个数是 $a_j$ 且不能构成三角形的方案**长度之和 / 个数**。

考虑一个状态能扩展到哪些状态，显然有：

$$(i,j)\to (j,p)\quad(a_i+a_j\leq a_p)$$

即 $l_{j,p}\gets l_{j,p}+l_{i,j}+c_{i,j},\ c_{j,p}\gets c_{j,p}+c_{i,j}\quad(a_i+a_j\leq a_p)$。

初值：$l_{0,i}=c_{0,i}=1$。目标：$\sum a_j\times l_{i,j}$。

直接三重循环枚举显然不行，接下来是一些优化：

- **每一次内层循环** $j$ 的时候，决策 $p$ 是单调的，可以用一个变量维护，均摊复杂度 $O(n)$。
- 可以发现每次转移的是一段区间（准确来说是 $a$ 的一个后缀），用~~树状数组~~前缀和维护即可做到 $O(1)$ 转移。

易知所有方案分值之和为：$\sum_{i=1}^{i\leq n}\sum_{j=1}^{j\leq i}a_i\times j\times \binom{i-1}{j-1}$，其中 $i$ 表示倒数第一个数为 $a_i$，$j$ 表示选出的数的个数为 $j$。

因为本题模数不是质数（毒瘤），所以需要时空 $O(n^2)$ 预处理组合数（毒瘤）。

时间复杂度 $O(n^2)$，空间复杂度 $O(n^2)$。

```cpp
int n,tot,sub,a[N],l[N][N],c[N][N],C[N][N];

int main(){
	n=read(); for(int i=1;i<=n;i++)a[i]=read(),l[0][i]=c[0][i]=1; sort(a+1,a+n+1);
	C[0][0]=1; for(int i=1;i<=n;i++)for(int j=0;j<=i;j++)C[i][j]=!j?1:(C[i-1][j-1]+C[i-1][j])%P;
	for(int i=1;i<=n;i++){
		int p=i+1; for(int j=0;j<i;j++){
			if(j)l[j][i]=(l[j][i-1]+l[j][i])%P,c[j][i]=(c[j][i-1]+c[j][i])%P;
			while(p<=n&&a[j]+a[i]>a[p])p++;
			if(p<=n)l[i][p]=(l[i][p]+l[j][i]+c[j][i])%P,c[i][p]=(c[i][p]+c[j][i])%P;
			sub=(sub+1ll*l[j][i]*a[i])%P;
		}
	}
	for(int i=1;i<=n;i++)for(int j=1;j<=i;j++)tot=(tot+1ll*C[i-1][j-1]*j%P*a[i])%P;
	cout<<(tot-sub+P)%P;
	return 0;
}
```
