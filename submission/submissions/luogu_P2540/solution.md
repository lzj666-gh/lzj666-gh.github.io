# P2540 题解

[（可能）更好的阅读体验？](https://starrykiller.blog.luogu.org/solution-p2540-p2668)

和 [@luchuhan](https://www.luogu.com.cn/user/764603) 共同想出来的做法~

关于如何搜索和怎么强剪枝其他题解已经说得很清楚了（如果不清楚请参阅其他题解）。那么这里提供另外一个优化的方法（似乎题解里面没有人这么写）

在写 dfs 的时候，我们会加上这样一条剪枝：

```cpp
void dfs(int step, int cnt) { // 打了 step 手牌，用了 cnt 张
    if (step>=ans) return;
    // do something
}
```

这样剪枝的正确性是显然的。但是这样剪枝针对的情况只有一种：$step\geq ans$。

我们不妨记 $card_i$ 表示第 $i$ 种牌有 $card_i$ 张。

显然一个状态就是这样的一个集合：$S=\{card_1,card_2,\cdots,card_n\}$，我们考虑对于不同的 $S$，维护一个 $ans_s$ 表示到状态 $s$ 需要的最少步数。于是若访问到状态 $S$，当前的 $step_S\geq ans_S$，则可以立即回溯。

如果简单地用一个 $15$ 维数组记录，不仅写起来麻烦，空间上恐怕也不太承受得住。于是我们可以设计一个哈希函数

$$h(S)=\sum_{i=1}^n card_i\cdot p^i$$

其中 $p$ 是一个素数，我的程序中使用的是 $13331$。我们可以利用 `unsigned long long` 的自然溢出（$\bmod 2^{64}$）+ `map<unsigned long long, int>` 或者 对素数取模+数组 来进行记录。

其实用结构体之类的东西记录下状态也可以。

于是就能得到极大的优化。

```cpp
// 这里把牌映射到了[13,17]
unsigned long long hsh() {
    unsigned long long res=0;
    for (int i=3; i<=17; ++i) {
        res=res*p+card[i];
    }
    return res;
}

map<unsigned long long, int> m;

void dfs(int step, int cnt) { // 打了 step 手牌，用了 cnt 张
    if (cnt>=n || step>=ans) {
        ans=min(ans, step);
        return;
    }
    auto h=hsh();
    if (m.find(h)!=m.end() && step>=m[h])
        return;
    m[h]=step;
    
    // do something
}
```

完整代码见[此处](https://www.luogu.com.cn/paste/elgpjqv7)。

AC 记录见[此处](https://www.luogu.com.cn/record/127023045)。