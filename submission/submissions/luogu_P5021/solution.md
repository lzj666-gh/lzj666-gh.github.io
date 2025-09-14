# P5021 题解

### [开头小广告：自己做的一个模板库OwO](https://www.luogu.org/blog/29354/Templet)

------------
# Solution

## 只讲满分解法：

### 看题目描述肯定一下就能想到二分答案。

也很容易想到二分m条赛道中最小的那一个，也可以理解为画一条分界线mid，看看比mid大或者等于的赛道能不能有m个。

对于一个点，从它子树发源的赛道，最多只能有一条穿过它并向上贡献，因为父亲边是唯一的，多一条赛道肯定会在边上重复。

### 我们考虑一下贪心：

如果现在树只有两层（一个树根和一堆儿子），我们的肯定希望这个子树多出现赛道。我们把边全部排序，然后从最小的边开始，用分界线mid减去这个边的边权，设为x。显然，给这个边找一条比**x大一点或者等于**的边即可，因为比x长的边虽然也能和当前匹配，但是后面我们其他的匹配或者是要向上贡献的机会可能就少了，因此可能会不优。

我们现在已经完成子树内的最大匹配了，我们找出链中没有用过的最长链（可以是空链，也就是0），作为向上的贡献（具体做法也就是记一个点权，点权也就是那个最长链的长度）。

这个时候，我们最下面那一层已经没有意义了，因为我们已经匹配好了，并且找出了最长链，其他已经匹配的赛道或者比最长链小的链已经没有用处了。那么我们可以看作把这一层全部消掉，显然是没有问题的（这时候的最长链已经被当作点权了）。

这样我们可以用DFS的方式，从下往上把树不停的“消层”，直至没有。

需要注意的是，最下层解决完毕以后，后面的层的链是**边权+点权**，这才是我们的链。当然也可以看作最下层的点权是0。

在全局的设个变量res记录还需要找到几条赛道。先让res等于m，每次在子树匹配成功，就res--，DFS全部结束的时候只要判断res是不是小于等于0就知道是否成功了。

一些细节建议看一下代码的注释qwq

------------


# CODE

```cpp
#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN = 5e4 + 5, MAXM = MAXN << 1;
const int INF = 0x7fffffff;

int head[MAXM], nxt[MAXM], v[MAXM], w[MAXM], cnt;

int n, m;
int root;

inline void Addline(int x, int y, int z)
{
    v[cnt] = y, w[cnt] = z;
    nxt[cnt] = head[x], head[x] = cnt++;

    return;
}

int dp[MAXN], tag[MAXN];//dp是向上贡献的最长链长度，也就是上面说的点权
int que[MAXN], tail;
int res;//还需要的赛道数

inline void DFS(int x, int from, int lim)
{
    for (int i = head[x]; ~i; i = nxt[i])
        if (v[i] != from)
            DFS(v[i], x, lim);//先下去DP一边，这样就不需要多开数组做后面的贪心了

    tail = 0;
    for (int i = head[x]; ~i; i = nxt[i])
        if (v[i] != from)
            que[++tail] = dp[v[i]] + w[i];//把几条链加进队列

    sort(que + 1, que + tail + 1);//排序

    for (int i = tail; i >= 1 && que[i] >= lim; i--)
        tail--, res--;//先把已经能变成赛道的边直接去掉，他们不需要两两匹配

    for (int i = 1; i <= tail; i++)
        if (tag[i] != x)//这个链没有被选过
		//这里的tag不再存True和False，而是存当前点的编号，这样就不用多次清空数组，而且可以保证不会重复（每个点只访问一次）
        {
            int l = i + 1, r = tail, pst = tail + 1;//二分另外一条链使得能刚好组成赛道
            while (l <= r)
            {
                int mid = ((l + r) >> 1);
                if (que[i] + que[mid] >= lim)
                    pst = mid, r = mid - 1;
                else
                    l = mid + 1;
            }

            while (tag[pst] == x && pst <= tail)//因为有可能当前二分到的是已经被选过的链，那么我们贪心往后找一条链，可以证明这样是最优的
                pst++;

            if (pst <= tail)//如果有观察上面的代码，可以发现tail+1是我们的溢出区，这里判断一下
                tag[i] = tag[pst] = x, res--;
        }

    dp[x] = 0;
    for (int i = tail; i >= 1; i--)//找到当前没有选过的最长链，向上传递（其实也就是把链看成是当前点对上面点的贡献）
        if (tag[i] != x)
        {
            dp[x] = que[i];
            break;
        }

    return;
}

signed main(void)
{
    memset(head, -1, sizeof head);

    cin >> n >> m;
    for (int i = 1, x, y, z; i < n; i++)
    {
        scanf("%d %d %d", &x, &y, &z);
        Addline(x, y, z), Addline(y, x, z);
    }

    root = rand() % n + 1;//随机选根

    int l = 0, r = INF, ans = 0;
    while (l <= r)//二分答案
    {
        int mid = ((l + r) >> 1);
        res = m;

        memset(tag, false, sizeof tag);

        DFS(root, 0, mid);
        if (res <= 0)
            ans = mid, l = mid + 1;
        else
            r = mid - 1;
    }

    cout << ans << endl;

    return 0;
}
```