# P1115 题解

> 几年就这么过去了，曾经并不注意格式规范导致现在题解不太美观。这里重新修正一下。这篇题解赞数不低，这里也只是修改 markdown 格式和分段排版，希望管理能给过。

---

~~又来水题解了~~。

题目传送门：[Link](https://www.luogu.org/problem/P1115)。

大家不要把这题想得很复杂，能做出一个题首先要有做题的信念。这题的实际难度没有大家想得那么高。

直接枚举 $l,r$，求所有区间的和然后取最大值的时间开销很大，不能通过本题，我们来思考更优秀的做法。

首先，我们现在纸上手算一下样例是怎么来的：

```
2 -4 3 -1 2 -4 3
ans:4
```

可以发现选 `3 -1 2` 是一种合法的方案。那么是怎么推出来的呢？

首先看到第一个数，是 $\color{green}\text{2}$。而 $\color{green}\text{2}$ 后面是 $\color{green}\text{-4}$，所以如果 $\color{green}\text{-4}$ 是答案的一部分，那么 $\color{green}\text{2}$ 一定也要加上去（这样答案就增加了，会比原来优）。

随后是 $\color{green}\text{3}$。如果 $\color{green}\text{3}$ 把前面的 $\color{green}\text{2}$ 和 $\color{green}\text{-4}$ 加上去，结果是 $\color{brown}\text{1}$。这个时候反而比原来的单独一个 $\color{green}\text{3}$ 要小。所以如果答案含有 $\color{green}\text{3}$，就一定不会加上前面的 $\color{green}\text{2}$ 和 $\color{green}\text{-4}$（加上前面的部分答案变小，不如到这里为止）。

下一个数是 $\color{green}\text{-1}$。这个数加上前面的 $\color{green}\text{3}$ 之后答案增加了（变成了 $\color{brown}\text{2}$），所以如果答案有 $\color{green}\text{-1}$，辣么绝对还有前面的 $\color{green}\text{3}$。

接下来是 $\color{green}\text{2}$，如果 $\color{green}\text{2}$ 加上前面的序列 $\color{green}\text{(3,-1)}$，辣么它的值变为 $\color{brown}\text{4}$。比原先增加了。

然后是 $\color{green}\text{-4}$，如果把 $\color{green}\text{-4}$ 加上前面的序列 $\color{green}\text{(3,-1,2)}$，结果会变成 $\color{brown}\text{0}$，比原先的 $\color{green}\text{-4}$ 大，所以如果 $\color{green}\text{-4}$ 是答案的一部分，那么前面的三个数也一定是答案的一部分。

最后一个数 $\color{green}\text{3}$，如果将 $\color{green}\text{3}$ 加上前面的序列，结果变成了 $\color{brown}\text{3}$，没有变，所以这个可加可不加。

最后我们来看一看刚推导的结果，发现 $\color{brown}\text{4}$ 是我们可以得出的最大和。

所以说了这么多，最终的结果是什么呢？

- 第一个数为一个有效序列
- 如果一个数加上上一个有效序列得到的结果比这个数大，那么该数也属于这个有效序列。
- 如果一个数加上上一个有效序列得到的结果比这个数小，那么这个数单独成为一个新的有效序列
- 在执行上述处理的过程中实时更新当前有效序列的所有元素之和并取最大值。

然后就可能有人问了：考虑上面样例推导中，出现了一个可加可不加的 $\color{green}\text{3}$。如何处理？

结论是：对于可加可不加的数，不如加上。因为加上对答案没有坏处，而如果这个数后面还有一部分能让答案变多，因为本题求的子段是连续子段，不加上的话这两边就连不起来了。所以无脑加就行了。

最后取最大值即可。

 ```cpp
#include<bits/stdc++.h>
using namespace std;
int n,a[200020],b[200020],i,ans=-2147483647;

// b[i] 表示截止到 i 时，第 i 个数所在的有效序列的元素和。

int main(){
    cin>>n;
    for(i=1;i<=n;i++){
        cin>>a[i];
        if(i==1) b[i]=a[i];
        else b[i]=max(a[i],b[i-1]+a[i]);
        ans=max(ans,b[i]);
    }
    cout<<ans;
    return 0;
}
```

然而对比这份代码的时空消耗，我们还可以做得更好。

我们来看一眼代码：

1. 输入 $a_i$。
2. 用 $b_{i-1}$ 和当前输入的 $a_i$ 给 $b_i$ 赋值。
3. 用 $b_i$ 给 $ans$ 更新答案。

首先发现全程中 $a$ 数组是没有意义的。我们每次只用到了当前使用的 $a_i$。也就是说，它可以被一个变量代替。

其次考虑 $b$ 数组，每次对 $b_i$ 更新只用到 $a_i$ 和 $b_{i-1}$。前者已经变成一个变量了，而后者，我们把 $b_{i-1}$ 看成“上一个 $b_i$”，于是就相当于 $b_i$ 是由上一个 $b_i$ 和变量 $a$ 更新的。这也可以缩减成一个变量。

最终我们就得出了空间消耗大优化后的代码：

 ```cpp
#include<bits/stdc++.h>
using namespace std;
int n,a,b,i,ans=-2147483647;
int main(){
	cin>>n;
	for(i=1;i<=n;i++){
		cin>>a;
		if(i==1) b=a;
		else b=max(a,a+b);
		ans=max(ans,b);
	}
	cout<<ans;
	return 0;
}
```

空间优化的效果还是很明显的，从 2.13MB 变成了 688KB。

-----------------