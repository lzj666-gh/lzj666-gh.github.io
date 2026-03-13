# P3368 题解

[树状数组 1](https://www.luogu.com.cn/problem/P3374) | [树状数组 2（本题）](https://www.luogu.com.cn/problem/P3368) | [修改记录](https://www.luogu.com.cn/paste/3i6jww3e)

### 前置知识

**lowbit**：

> $\operatorname{lowbit}(X)$ 表示 $X$ 在二进制下，最末尾的 $1$ 所代表的数字加上后面的 $0$ 组成的数字。
> 
> 对于数 $X$ 做 lowbit 操作，在代码中可以表示为 `X&(-X)`。例如当 $X=76$ 时，其二进制为 $\texttt{1001100}$，则 $-X$ 在计算机用反码表示，为 $\texttt{0110100}$，将其按位与操作之后得到 $\texttt{0000100}$，后面组成的数字为 $\texttt{100}$，也就是 $\operatorname{lowbit}(X)$ 的值。

**差分**：

> 一种简单的结构，可以实现 $\mathcal{O}(1)$ 区间修改和 $\mathcal{O}(N)$ 单点查询。
> 
> 令存储差分数组的数组为 $D$。修改操作，将 $[L,R]$ 增加 $K$，则需更改 $D_L\gets D_L+K$，$D_{R+1}\gets D_{R+1}-K$；查询操作需要统计前 $N$ 个数的前缀和。

### 算法介绍

[树状数组](https://oi-wiki.org/ds/fenwick/)，是一种可以实现**单点修改**和**区间查询**的数据结构。

而对于本题，变成了区间修改和单点查询，只需要改变原本的数组 $C$ 的含义变差分即可（与差分模板几乎相同）。
- 对于修改操作，将 $[L,R]$ 增加 $K$，则需更改 $C_L\gets C_L+K$，$C_{R+1}\gets C_{R+1}-K$；
- 对于查询操作，查询第 $X$ 个数的值，则需要求前 $X$ 个 $C_i$ 的和。

### 正确性证明

在这里讲一下树状数组。

![](https://cdn.luogu.com.cn/upload/image_hosting/b0cujsbk.png)

上图是一个树状数组的图示。对于每一个区间 $[L,R]$，代表的是这个区间的和。如果想要访问一个区间 $[L,R]$，那么就要从最大的区间开始，逐级划分，然后加和（类似于[线段树](https://oi-wiki.org/ds/seg/)的思想）。

不难发现，有些区间是没有用的。例如 $[2,2]$，可以用 $[1,2]$ 的值减去 $[1,1]$ 的值得到。图中画叉号的区间都是可以删掉的。

![](https://cdn.luogu.com.cn/upload/image_hosting/g43es59o.png)

删掉没有用的区间后，给每个区间做一个编号，每一个区间的编号为它的右端点的数字。令编号为 $i$ 的区间和为 $C_i$。

你会发现，编号为 $i$ 的区间应为 $[i-\operatorname{lowbit}(i),i]$。初始化十分好想，可以直接用 $A_i$ 的和来表示即可，为：

$$C_i=\sum_{j=i-\operatorname{lowbit}(i)+1}^iA_i$$

![](https://cdn.luogu.com.cn/upload/image_hosting/sczsoyy7.png)

现在想要查询区间 $[L,R]$ 的和，则需要用 $[1,R]$ 的和减去 $[1,L-1]$ 的和。想要查询区间 $[1,X]$ 的和，首先要让其加上 $C_X$，然后让 $X$ 向前移动 $\operatorname{lowbit}(X)$ 位，即 $X\gets X-\operatorname{lowbit}(X)$。然后再加上 $C_X$，再向前移动。循环至 $X$ 变为 $0$ 为止，可以保证包含 $[1,X]$ 中的每一个数都被查询，就完成了统计区间 $[1,X]$ 的问题。

由于单次查询，每一次都会去掉二进制末尾的一个 $1$，在最差情况下会移动 $\log X$ 次，故查询的时间复杂度为 $\mathcal{O}(\log X)$。

现在想要修改点 $X$ 的值，使其增加 $K$。那么相反，$X$ 每次需要向后移动 $\operatorname{lowbit}(X)$ 位，即 $X\gets\operatorname{lowbit}(X)$，然后修改 $C_X\gets C_X+K$。一直向右移动直到移动到大于或等于 $N$ 的点停止，保证每个包含该点的区间都被修改。

同理，单点修改的时间复杂度亦为 $\mathcal{O}(\log X)$。

整体时间复杂度为 $\mathcal{O}(N\log N)$，空间复杂度 $\mathcal{O}(N)$。

### 注意事项

- 需要开 `long long`。

### 代码实现

```cpp
#include<bits/stdc++.h>
using namespace std;
const int N=5e5+10;
int n,m,a[N];
long long c[N]; // 注意 c 中的值可能超过 int 范围
int lowbit(int x){
	return x&(-x);
}
void add(int x,int k){ // 修改操作
	while(x<=n){
		c[x]+=k;
		x+=lowbit(x);
	}
	return;
}
long long sum(int x){ // 查询操作
	int res=0;
	while(x){
		res+=c[x];
		x-=lowbit(x);
	}
	return res;
}
int main(){
	cin>>n>>m;
	for(int i=1;i<=n;++i){
		cin>>a[i];
		add(i,a[i]-a[i-1]); // 按照差分含义初始化
	}
	while(m--){
		int op;cin>>op;
		if(op==1){
			int l,r,k;cin>>l>>r>>k;
			add(l,k),add(r+1,-k); // 差分操作
		}
		else{
			int x;cin>>x;
			cout<<sum(x)<<"\n"; // 前 x 个数的和
		}
	}
	return 0;
}
```