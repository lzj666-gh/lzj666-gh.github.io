# P3065 题解

## Description

给定 $n\ (1 \leq n \leq 3 \times 10^4)$ 个总长不超过 $m\ (1 \leq m \leq 3 \times 10^5)$ 的互不相同的字符串，现在你可以任意指定字符之间的大小关系。问有多少个串可能成为字典序最小的串，并输出这些串。

## Solution

看到与字典序有关的问题，很容易想到建一棵 **Trie(字典树)** 。

对于每一个字符串，我们可以设它的字典序是所有字符串中最小的。

也就是说，这个字符串的第 $i$ 个字母 在 **Trie** 的第 $i$ 层（根节点算第 $0$ 层）的所有字母中 字典序最小。

设这个字符串的第 $i$ 个字母为 $u$，我们可以连单向边 $u \to v$，表示我们指定了 $u$ 的字典序比 $v$ 小，其中 $v$ 是第 $i$ 层的其它字母。若这个字符串是其它某个字符串的前缀，则这个字符串不可能成为字典序最小的串，比如说 $abba$ 的字典序一定比 $ab$ 大。当 $26$ 个字母间的关系形成环时，也一定不能成为字典序最小的串。

怎么判断是否形成环呢？可以用 $\rm tarjan$ 或者 **拓扑排序** 。

这里我采用了 **拓扑排序**  。我们从入度为 $0$ 的点开始，不断删去与它相连的边，并修改其它点的入度，将新的入度为 $0$ 的点加入队列。若队列已空，但还存在入度不为 $0$ 的点，则说明图存在环，反之则有解。

时间复杂度为 $O(26m)$ 。

## Code

```cpp
#include <bits/stdc++.h>
using namespace std;
typedef long long LL;

template <class T>
inline void read(T &x) {
    x = 0;
    char c = getchar();
    bool f = 0;
    for (; !isdigit(c); c = getchar()) f ^= c == '-';
    for (; isdigit(c); c = getchar()) x = x * 10 + (c ^ 48);
    x = f ? -x : x;
}

template <class T>
inline void write(T x) {
    if (x < 0) {
        putchar('-');
        x = -x;
    }
    T y = 1;
    int len = 1;
    for (; y <= x / 10; y *= 10) ++len;
    for (; len; --len, x %= y, y /= 10) putchar(x / y + 48);
}

const int MAXN = 3e4, MAXM = 3e5;
int n, ans;
string s[MAXN + 5];
bool ok[MAXN + 5];
struct Trie {
    int tot, in[26], e[26][26], ch[MAXM + 5][26];
    bool ed[MAXM + 5];
    queue<int> q;
    
    inline void insert(string x) {
        int u = 1, len = x.size();
        for (int i = 0; i < len; ++i) {
            int v = x[i] - 'a';
            if (!ch[u][v]) ch[u][v] = ++tot;
            u = ch[u][v];
        }
        ed[u] = 1;
    }//插入 
    inline void topoSort() {
        for (; !q.empty(); q.pop());
        for (int i = 0; i < 26; ++i)
            if (!in[i]) q.push(i);
        for (; !q.empty(); ) {
            int u = q.front();
            q.pop();
            for (int v = 0; v < 26; ++v)
                if (e[u][v]) {
                    --in[v];
                    if (!in[v]) q.push(v);
                }
        }
    }//拓扑排序 
    inline bool find(string x) {
        int u = 1, len = x.size();
        memset(e, 0, sizeof (e));
        memset(in, 0, sizeof (in));
        for (int i = 0; i < len; ++i) {
            if (ed[u]) return 0;//是其它字符串的前缀，无解
            int v = x[i] - 'a';
            for (int j = 0; j < 26; ++j)
                if (v != j && ch[u][j] && !e[v][j]) {
                    e[v][j] = 1;//与同一层其它字母连边 
                    ++in[j];//统计入度 
                }
            u = ch[u][v];
        }
        topoSort();
        for (int i = 0; i < 26; ++i)
            if (in[i]) return 0;//存在环，无解 
        return 1;
    }//检验字符串 
} tr;

int main() {
    read(n);
    tr.tot = 1;
    for (int i = 1; i <= n; ++i) {
        cin >> s[i];
        tr.insert(s[i]);//插入到 Trie 中 
    }
    for (int i = 1; i <= n; ++i)
        if (tr.find(s[i])) {
            ++ans;//统计个数 
            ok[i] = 1;//标记合法字符串 
        }
    write(ans);
    putchar('\n');
    for (int i = 1; i <= n; ++i)
        if (ok[i]) cout << s[i] << '\n';
    return 0;
}
```

