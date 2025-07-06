# P11143 题解

## 题目大意

有一家蛋糕店被 $\mathcal W$ 帮和 $\mathcal M$ 帮俩群土匪抢劫了，但是蛋糕只有一个，于是他们决定瓜分这块蛋糕。

已知在蛋糕大小为 $n \times m$，上方有 $k$ 块巧克力，它们分别位于 $( x_i - 0.5 , y_i - 0.5 )$, 并且同一个位置可以有两块巧克力，因为这些巧克力太美味了，所以双方都想要分到尽可能多的巧克力。

蛋糕刀起初在坐标 $( 0 , 0 )$ 的位置，由双方轮流移动，经过猜拳，由 $\mathcal W$ 帮先手，每次可以使刀移动到 $(x+1,y)$ 或 $(x,y+1)$ 处，并且右上角部分分给 $\mathcal W$ 帮，左下角部分分给 $\mathcal M$ 帮，双方都采用最优策略，求 $\mathcal W$ 帮最多可分到多少巧克力？

---

## 思路

容易发现，$\mathcal W$ 帮为了获得更多的巧克力会尽量向下移动，而 $\mathcal M$ 帮会尽力向右方移动，就像下图，而题面的图是来扰乱我们思路的。

![](https://cdn.luogu.com.cn/upload/image_hosting/8kqcnwk7.png)因为 $( n , m \leq 10^{18})$，所以我们不能够进行暴力判断，只得寻找规律。

用一眼发现 $(1,1)$,$(2,2)$ 等点上的巧克力属于 $\mathcal W$ 方，则发现 $x_i$ 和 $y_i$ 可以取等号。而当 $x_i > y_i$ 时，属于倒霉蛋 $\mathcal M$ 帮，便可得出通解，当 $x_i \leq y_i$ 时，属于 $\mathcal W$。

---

## 代码

我马蜂有点难看，别介意。

```cpp
#include<bits/stdc++.h>
using namespace std;
#define int long long
int x[200111],y[200111],k,w,n,m;
signed main(){
	cin>>n>>m>>k;
	for(int i=1;i<=k;i++){
		cin>>x[i]>>y[i];
		if(x[i]<=y[i])w++;
	}
	cout<<w;
	return 0;
}
```