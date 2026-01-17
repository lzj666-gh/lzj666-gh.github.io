# P9913 题解

倒着阅读本题解，即可知道在 2023 激励计划中我给这题评分 10 的原因。

---

**注意到**

![](https://cdn.luogu.com.cn/upload/image_hosting/6c3yk0e0.png)  
（此图片来自[《怎样把一个立方体分成 54 个小立方体？》](http://www.matrix67.com/blog/archives/6513)，作者为顾森（Matrix67），此图片以 CC BY-NC-SA 协议进行许可）

由于通过将 $1$ 个小正方形分割为更小的 $4$ 个小正方形可以**增加 $\bm 3$ 个小正方形数量**，更大的 $n$ 均可被满足，例如：

- $n = 9$ 可由 $n = 6$ 的方案分割得到。
- $n = 10$ 可由 $n = 7$ 的方案分割得到。
- $n = 11$ 可由 $n = 8$ 的方案分割得到。
- ……

所以除了 $n \in \{ 2, 3, 5 \}$ 以外的 $n$ 均有方案。

通过**瞪眼法**不难发现 $n \in \{ 2, 3, 5 \}$ 时没有方案。

参考代码（Python）：

```python3
#这回只花了45min就打完了。
#真好。记得多手造几组。最好有暴力对拍。 
coach = 'water235'
for _ in range(int(input())):
  print('No' if input() in [*coach] else 'Yes')
```

参考代码（Python）：

题目背景中的小 H 昨天生日吗？也太巧了吧！今天是 CPhO 2019 报道日，昨天也是[我的生日](https://www.zhihu.com/question/353626585/answer/880220243)，祝我和小 H 昨天生日快乐！

比赛结束后听说这题是原题……？哎，water's problem，原来是教练出的题，[怪不得嘛](https://www.zhihu.com/question/531201223/answer/2468824563)。

不过，这样就直接 AC 了也太快了，所以最好要等个 [45 分钟](https://www.zhihu.com/question/527361777/answer/2472274087)左右再提交。

再联想教练的网名，正解呼之欲出：当 $n$ 被教练的网名中的数码包含时无解，否则有解。

通过样例可知，$n = 4$ 时答案是 `Yes` 而 $n = 3$ 时答案是 `No`。

注意到题目名：**water problem**。由于你的教练的网名就叫 **water**_235_，这一定是某种暗示。

泉州七中学生快速 AC 方法。