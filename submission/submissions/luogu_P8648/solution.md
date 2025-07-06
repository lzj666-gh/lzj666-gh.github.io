# P8648 题解

怎么题解区全是扫描线，还有个 $O(n^3)$ 暴力老哥。

为防止误导新人，给个理论上稳过的 $O(n^2)$ 解法。

二维前缀和可以处理若干次单点加，最后若干次矩形查的问题。

将其差分，即可处理若干次矩形加，最后若干次单点查的问题。

于是我们使用差分将所有矩形加上，然后做一遍二维前缀和，即可求出每个格子被几个矩形覆盖。统计有多少格子被至少一个矩形覆盖，输出即可。

注意本题卡空间，但注意到差分阶段每个格子只会被每个矩形 $\pm 1$，每个格子的值不超过 $10^4$，最终求前缀和后每个格子只会被每个矩形覆盖至多一次，值也不超过 $10^4$，因此开 short 即可。

时间复杂度 $O(n^2)$。

```cpp
//By: OIer rui_er
#include <bits/stdc++.h>
#define rep(x,y,z) for(int x=(y);x<=(z);x++)
#define per(x,y,z) for(int x=(y);x>=(z);x--)
#define debug(format...) fprintf(stderr, format)
#define fileIO(s) do{freopen(s".in","r",stdin);freopen(s".out","w",stdout);}while(false)
using namespace std;
typedef long long ll;

mt19937 rnd(std::chrono::duration_cast<std::chrono::nanoseconds>(std::chrono::system_clock::now().time_since_epoch()).count());
int randint(int L, int R) {
    uniform_int_distribution<int> dist(L, R);
    return dist(rnd);
}

template<typename T> void chkmin(T& x, T y) {if(x > y) x = y;}
template<typename T> void chkmax(T& x, T y) {if(x < y) x = y;}

const int N = 1e4+5;

int n, ans;
short a[N][N];

int main() {
    scanf("%d", &n);
    rep(i, 1, n) {
        int x1, y1, x2, y2;
        scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
        ++a[x1][y1];
        --a[x1][y2];
        --a[x2][y1];
        ++a[x2][y2];
    }
    rep(i, 0, 10000) {
        rep(j, 0, 10000) {
            a[i][j] = int(i > 0 ? a[i-1][j] : 0) + (j > 0 ? a[i][j-1] : 0) - (i > 0 && j > 0 ? a[i-1][j-1] : 0) + a[i][j];
            if(a[i][j]) ++ans;
        }
    }
    printf("%d\n", ans);
    return 0;
}
```