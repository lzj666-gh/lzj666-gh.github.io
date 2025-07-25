# B3984 题解

## Source & Knowledge

2024 年 6 月语言月赛，由洛谷网校入门计划/基础计划提供。

## 题目大意

目前已经做了 $x$ 题。每天可以做 $1$ 题或者 $2$ 题，询问至少再做多少天才能做到 $y$ 题。
	
## 题目分析

题目即求至少做题多少天才可做 $y - x$ 题。由于每天至多做两题，所以答案是 $\cfrac{y - x}{2}$ 上取整。

这里的「上取整」可以考虑使用 `ceil` 函数，但是一般情况下 `ceil` 做的是小数运算，对于本题而言可能精度不太够，无法通过。

因此建议这样一种方法：
1. 首先计算 $\cfrac{y - x}{2}$ 下取整的结果（整数运算）；
1.  其次如果 $y - x$ 是奇数，那么代表 $\cfrac{y - x}{2}$ 不取整的结果里带一个 $0.5$，上取整后是 $1$，令第一步的结果 $+ 1$。
1. 最后输出结果即可。

```cpp
long long x, y;
cin >> x >> y;
long long ans = (y - x) / 2;
if ((y - x) % 2 == 1) {
    ++ans;
}
cout << ans << endl;
```

## 视频讲解

![](bilibili:BV19E421P7KQ?page=1)