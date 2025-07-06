# P11228 题解

欢迎报名[洛谷网校](https://class.luogu.com.cn/)，期待和大家一起进步！

本题属于模拟题，为了解释清楚题意，题目长度偏长，放在这个位置可能对于年龄较低的参赛选手不太友好。

根据题目描述直接进行模拟，下面是几个要点：

- 在代码中可以设置两个位移数组 `const int dx[]={0,1,0,-1}, dy[]={1,0,-1,0};`，以简便地完成转向的移动。
- 需要注意在代码中所使用的横纵坐标，其中 `y1` 等变量名不应定义为全局变量（尤其是在有万能头文件的情况下），以免出现编译错误。
- 横纵坐标等用错可能会出现通过样例但是未 AC 的情况（例如说在一处 `y1` 错写为 `y0` 等情况）
- 多测不清空，爆零两行泪。

参考代码：

```cpp
#include <bits/stdc++.h>
using namespace std;
bool vis[1005][1005];
char ch[1005][1005];
const int dx[]={0,1,0,-1},dy[]={1,0,-1,0};
void solve() {
	int n,m,k,x0,y0,d0;
	memset(vis,0,sizeof(vis));
	cin >> n >> m >> k;
	cin >> x0 >> y0 >> d0;
	for (int i=1;i<=n;i++) {
		char s[1005];
		cin >> s;
		for (int j=1;j<=m;j++)
			ch[i][j]=s[j-1];
	}
	vis[x0][y0]=true;
	for (int i=1;i<=k;i++) {
		int x1=x0+dx[d0],y1=y0+dy[d0];
		if (1<=x1 && x1<=n && 1<=y1 && y1<=m && ch[x1][y1]=='.') {
			x0=x1;
			y0=y1;
		}
		else
			d0=(d0+1)%4;
		vis[x0][y0]=true;
	}
	int ans=0;
	for (int i=1;i<=n;i++) {
		for (int j=1;j<=m;j++)
			ans+=vis[i][j];
	}
	cout << ans << endl;
}
int main() {
	int T;
	cin >> T;
	while (T--) {
		solve();
	}
}
```