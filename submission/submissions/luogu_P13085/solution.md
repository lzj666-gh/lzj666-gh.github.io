# P13085 题解

~~来水题解了。~~

由于 $a,b$ 范围较大，直接搜索肯定是不行的，考虑数位 dp。为方便，以下“第 $i$ 位”均表示从高位开始的第 $i$ 位（如最高位为“第一位”）。

令 $f[i][j]$ 表示 $i$ 位且以最高位为数字 $j$ 的 windy 数的个数。显然 $f[i][j]$ 可以通过枚举第二位的数字得到：$\displaystyle f[i][j]=\sum_{k=\max(j-2,0)}^{\min(j+2,9)} f[i-1][k]$，初始状态为 $f[1][i]=1(1 \leq i \leq 9)$。

接下来考虑如何计算 $a$ 到 $b$ 之间的 windy 数的个数。我们可以把答案拆成两个部分：**小于等于 $b$ 的 windy 数个数**与**小于 $a$ 的 windy 数个数**之差。我们发现这两部分是相似的（小于 $a$ 即为小于等于 $a-1$），只需要考虑如何计算小于等于某个数的 windy 数个数。

假设我们要求小于等于一个数 $a$ 的 windy 数个数，设其为 $m$ 位，其第 $i$ 位表示为 $r_i$。首先考虑位数比 $m$ 小的数中有多少个 windy 数：$\displaystyle \sum_{i=1}^{m-1}\sum_{j=1}^9 f[i][j]$。接着我们考虑有 $m$ 位但首位小于 $r_1$ 的 windy 数：$\displaystyle \sum_{j=1}^{r_1-1}f[m][j]$。

最后考虑 $m$ 位且首位为 $r_1$ 的 windy 数,这时我们需要考虑第二位的取值（因为第二位不能随便取，不能使用 $f[m][r_1]$ 来计算个数）。类似上面的，枚举第二位小于 $r_2$ 的（且小于等于 $r_1-2$）：$\displaystyle \sum_{j=1}^{\min(r_2-1,r_1-2)} f[m-1][j]$，然后考虑第二位为 $r_2$（如果 $r_1$ 和 $r_2$ 满足 windy 数的标准），枚举第三位的取值……

总的来说，如果 $a$ 的前 $l$ 位均满足 windy 数的性质（相邻两位之差大于等于 $r$），那么小于等于 $a$ 的 windy 数个数为：

$$\displaystyle \sum_{i=1}^{m-1}\sum_{j=1}^9 f[i][j]+\sum_{i=1}^{l+1}\sum_{j=1}^{\min(r_i-1,r_{i-1}-2)}f[i][j]$$

计算 $f$ 的时间复杂度为 $\mathcal{O}(n^2m)$，计算小于等于某个数的 windy 数个数的时间复杂度为 $\mathcal{O}(nm)$（其中 $n$ 为数字个数即 $10$，$m$ 为数字位数），空间复杂度为 $\mathcal{O}(nm)$。

代码如下，仅供参考：

```cpp
#include<bits/stdc++.h>
using namespace std;

typedef unsigned long long ull;

ull f[20][10],power[20];
void init() {
	power[0]=1;
	for(int i=1;i<=19;i++) power[i]=power[i-1]*10;
	for(int i=0;i<=9;i++) f[1][i]=1;
	for(int i=2;i<=19;i++)
		for(int j=0;j<=9;j++)
			for(int k=0;k<=9;k++)
				if(abs(j-k)>=2)
					f[i][j]+=f[i-1][k];
	return ;
}
ull solve(ull x) {
	int w=0,y,pre;
	ull ans=0;
	while(power[w]<=x) w++;
	for(int i=1;i<w;i++)
		for(int j=1;j<=9;j++)
			ans+=f[i][j];
	y=x/power[w-1];
	for(int j=1;j<y;j++) ans+=f[w][j];
	pre=y,x%=power[w-1];
	for(int i=w-1;i>=1;i--) {
		y=x/power[i-1];
		for(int j=0;j<y;j++)
			if(abs(j-pre)>=2)
				ans+=f[i][j];
		if(abs(pre-y)<2) break;
		pre=y,x%=power[i-1];
	}
	return ans;
}

int main() {
	ull a,b;
	cin>>a>>b;
	init();
	cout<<solve(b+1)-solve(a)<<endl;
	return 0;
}
```