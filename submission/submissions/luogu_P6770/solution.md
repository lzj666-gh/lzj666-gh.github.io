# P6770 题解

#### Description

> 给定一个 $N$ 点 $M$ 边的图，有 $C$ 个有奶牛的点，如果他们到达点 $1$ 的最短时间在 $\rm limit$ 内，那么就算这只奶牛犯罪。求有哪些奶牛犯罪。

#### Solution

这题其实可以简化为最短路。

因为我们要求的是每只奶牛到达点 $1$ 的 **最短时间**，所以我们每次计算$1$ 到奶牛所在的点的最短路即可。

为了更简便一点，我们可以使用 SPFA，进行一次 SPFA，然后调用 ${\rm dist}_i$ 即可。

在最后统计答案的时候容易错，放一下统计答案的代码。

```cpp
for (int i = 1, x; i <= c; i++) {
	scanf("%d", &x);
	if (dist[x] <= limit)
		ans[++pnt] = i;
}
printf("%d\n", pnt);
sort(ans + 1, ans + pnt + 1);
for (int i = 1; i <= pnt; i++)
	printf("%d\n", ans[i]);
```

By Shuchong     
2020.8.18