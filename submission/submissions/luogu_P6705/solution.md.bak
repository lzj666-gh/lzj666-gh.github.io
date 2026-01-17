# P6705 题解

这个题确实不太简单，因为在二分的时候dfs和check的次数惊人。

这个题如果你做出来了，那么说明你的dfs和二分答案已经炉火纯青了。

所以，如果你是想了一会不会写来看题解，希望你看到这里再回去想想，毕竟这个题对你我觉得会很有启发吧。~~（等下，先把点赞留下啊喂！）~~

#### 算法：DFS+二分答案+暴力枚举

我们可以二分从1到当前的的高度。

需要一个方向数组。

还有就是，不要被32MB给吓到，放心去定义吧。

具体看代码：
```cpp
#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
#define rint register int//稍微快一点
const int maxn = 55;
int n, h[maxn][maxn], ji, s, t, ans = 214748364, now;
bool v1[maxn][maxn], v2[maxn][maxn];
//v1存是否是村庄，v2存是否遍历
int d[10][2] = {{0, 0},{1,0}, {0,1}, {-1, 0}, {0, -1}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}};

void dfs(int x, int y, int q, int z)
{
    if (x < 1||x > n|| y < 1 || y > n||v2[x][y]||h[x][y] < q||h[x][y] > z)
      return ;//看看能不能走
    v2[x][y] = 1;
    now += v1[x][y];//若有村加1，没有就加0
    for(rint i = 1;i <= 8; ++i)
      dfs(x + d[i][0], y + d[i][1], q, z);
}

bool check(int mid, int q)
{
	memset(v2, 0, sizeof(v2));//每次都要把v2清空
	
	now = 0;
	dfs(s, t, mid, q);
	
	return now == ji;//看看所有的村庄是否都被遍历过
}

void cini()
{
    cin >> n;
    for(rint i = 1;i <= n; ++i)
        for(rint j = 1;j <= n; ++j)
        {
            char c;
            cin >> c;
            if(c == 'K')
            {
                ++ji;//村庄数量
                v1[i][j] = 1;
            }
            else if(c == 'P')
              s = i, t = j;//起点
        }
    
    for(rint i = 1;i <= n; ++i)
      for(rint j = 1;j <= n; ++j)
          cin >> h[i][j];
}

void work()
{
    int l, r, mid;
    for(rint i = 1;i <= n; ++i)
      for(rint j = 1;j <= n; ++j)
      {
        if(h[i][j] < h[s][t])
          continue;//我们只要比起点高的村
        l = 1; r = h[i][j];
        while(l <= r)
        {
            mid = (l + r) >> 1;
            if(check(mid, h[i][j]))
            {
                ans = min(ans, h[i][j] - mid);
                l = mid + 1;
            }else r= mid - 1;
        }
      }
    printf("%d", ans);
}

int main()
{
    cini();
    work();//这样看起来是否会简洁一点呢
    return 0;
}
```
