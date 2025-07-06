# CF730J 题解

# 简要思路

对于这一道题，很显然是一个动态规划 ~~（废话）~~ 。

那么我们考虑转移方程。

显然，在这一道题中，关键变量只有两个 $a$ , $b$ 。

第一问很好求，**很显然，根据贪心，先对瓶子的容量进行降序排序，求前若干个瓶子使他们的容量大于等于所有水的体积时的个数即可**。

### 代码如下

```cpp
	sort(c+1,c+n+1,cmp);
	ll temp=0;
	for(ll i=1;i<=n;i+=1){
		temp+=c[i].b;
		if(temp>=m){
			printf("%d ",i);
			break;
		}
	}
```


但是题目在选择瓶子最少的情况下，方案是不一定的。

这就导致在第二问，可能答案会不同。

通过观察得知， **第二问就是要在第一问的个数确定时，求出选择瓶子的水最多的方案** 。

为什么？ **因为选择了若干个瓶子，就意味着其他的瓶子的水要倒入其中，花费就为他们水的体积之和** 。

然后，我们开始考虑转移方程。

设 $f_i$ 表示当水的体积是 $i$ 时所需要的最少的瓶子数。

显然，根据一般的背包问题，有 $f_i = \max{f_{i-b_j} + 1}$ 。

同时，根据上面的分析，我们要求的是此时水体积最大的，所以附加上一个 $ans$ 数组， $ans_i$ **表示 $ans_i$ 表示当容积为 $i$ 时水体积的最大值** 。

由以上思路，就有了如下代码。

CODE
```cpp
#include <bits/stdc++.h>
using namespace std;
const int N = 1e2 + 20;
int n, m, f[10020], sum, ans[10020]; 
struct Node {
    int a, b;
} c[N];
inline int read() {//快读的板子，请自动忽略 
    char ch = getchar();
    int ans = 0, cf = 1;

    while (ch < '0' || ch > '9') {
        if (ch == '-')
            cf = -1;

        ch = getchar();
    }

    while (ch >= '0' && ch <= '9') {
        ans = (ans << 1) + (ans << 3) + (ch ^ 48);
        ch = getchar();
    }

    return ans * cf;
}
bool cmp1(Node a, Node b) {//对水的容积进行排序 
    if (a.a != b.a)
        return a.a > b.a;
    else
        return a.b > b.b;
}
int main() {
    n = read();

    for (int i = 1; i <= n; i += 1)
        c[i].a = read(), m += c[i].a;

    for (int i = 1; i <= n; i += 1)
        c[i].b = read(), sum += c[i].b;

    sort(c + 1, c + n + 1, cmp1);
    //初始化边界，当重量为 0  的时候选择 0 个瓶子 
    memset(f, 0x3f, sizeof(f));
    f[0] = 0;

    for (int i = 1; i <= n; i += 1) {//枚举每个瓶子 
        for (int j = sum; j >= c[i].b; j -= 1) {
            if (f[j - c[i].b] + 1 < f[j] || (f[j - c[i].b] + 1 == f[j] && (ans[j - c[i].b] + c[i].a) > ans[j])) {
               //经典的 01 背包模型，同时将 ans （水的体积） 作为第二关键字进行比较 
			   f[j] = f[j - c[i].b] + 1;
                ans[j] = ans[j - c[i].b] + c[i].a;
            }
            if (j > m) {
                if (f[m] > f[j] || (f[m] == f[j] && ans[j] > ans[m])) {
                    f[m] = f[j];
                    ans[m] = ans[j];
                }
            }//如果水的体积超出上界，同样更新答案。 
        }
    }

    printf("%d %d\n", f[m], m - ans[m]);
    return 0;
}
```

真的不点一个赞再走吗 QAQ 。