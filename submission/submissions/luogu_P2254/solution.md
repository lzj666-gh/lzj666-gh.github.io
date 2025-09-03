# P2254 题解

```
/*首先考虑对于时间t来dp：
f[t][i][j]表示在第t时刻在第i行第j列所能获得的最长距离。 
转移方程：f[t][i][j]=max(f[t-1][i][j],f[t][i*][j*]+1)(i*,j*为上一个合理的位置) 
这样时间复杂度为O(TNM)，可以过50%,但对于100%TLE且MLE。
所以必须优化，首先把时间t换成区间k，
令f[k][i][j]表示在第k段滑行区间中在位置i，j所能获得最长距离
注意到在第k段时间内只能向某个方向最多走x步（x为区间长度），得到转移方程
f[k][i][j]=max(f[k-1][i][j],f[k][i*][j*]+dis(i,j,i*,j*))(i*,j*为上一个合理的位置)
这个做法的时间复杂度是O(kn^3)，会超时，需要进一步优化
用单调队列优化掉内层的一个n，就可以做到O(kn^2)，可以AC，本代码中还使用了滚动数组优化 
用单调递减队列求最大值时，遇到障碍清空整个队列即可，另外队列比较时需要加上偏移量dis*/
#include<cstdio>
#include<cstring>
#include<iostream>
#define MAXN 205
using namespace std;
int n, m, sx, sy, K, ans, dp[MAXN][MAXN];
int dx[5] = {0, -1, 1, 0, 0}, dy[5] = {0, 0, 0, -1, 1}; 
struct node{int dp, pos;}q[MAXN]; //q为单调递减队列，要存位置信息用来计算共走了几步 
char map[MAXN][MAXN];
void work(int x, int y, int len, int d) //第k个区间的时长为len，方向为d，起点坐标x,y 
{
	int head = 1, tail = 0;
	for(int i = 1; x >= 1 && x <= n && y >= 1 && y <= m; i++, x += dx[d], y += dy[d])
		if(map[x][y] == 'x') head = 1, tail = 0; //遇到障碍，清空队列 
		else
		{
			while(head <= tail && q[tail].dp + i - q[tail].pos < dp[x][y]) tail--;
			q[++tail] = node{dp[x][y], i}; //当前值入队列 
			if(q[tail].pos - q[head].pos > len) head++; //队列长度超过len时队首弹出 
			dp[x][y] = q[head].dp + i - q[head].pos; //最优解是队首元素+移动距离 
			ans = max(ans, dp[x][y]); //记录结果 
		}
}
int main()
{
	scanf("%d%d%d%d%d", &n, &m, &sx, &sy, &K);
	for(int i = 1; i <= n; i++) scanf("%s", map[i] + 1);
	memset(dp, 0xf3, sizeof(dp));
	dp[sx][sy] = 0; //初始化，只有初始位置是0，其他都是负无穷 
	for(int k = 1, s, t, d, len; k <= K; k++)
	{
		scanf("%d%d%d", &s, &t, &d);
		len = t - s + 1;
		if(d == 1) for(int i = 1; i <= m; i++) work(n, i, len, d);
		if(d == 2) for(int i = 1; i <= m; i++) work(1, i, len, d);
		if(d == 3) for(int i = 1; i <= n; i++) work(i, m, len, d);
		if(d == 4) for(int i = 1; i <= n; i++) work(i, 1, len, d);
	}
	printf("%d", ans);
	return 0;
}
```