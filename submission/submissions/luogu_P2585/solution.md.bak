# P2585 题解

介绍一个无建树做法

#### 个人认为我的代码比较易懂(~~简直不需要注释~~)

定义dp\[x][0/1/2] 分别为x节点染绿 /红 /蓝 情况下子树中最多有几个点被染成绿色

类似的 f\[x][0/1/2] 为最少有几个点

见代码:

```c++
#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
const int N = 500050;
char s[N];
int dp[N][4], f[N][4], cnt;
int ans1 = 1;
void dfs(int x) {
	if (s[x] == '0') {//叶节点
		f[x][0] = dp[x][0] = 1;
		return;
	}
	dfs(++cnt);
    //左儿子编号为x+1
	if (s[x] == '1') { //一个儿子
		dp[x][0] = max(dp[x+1][1], dp[x+1][2])+1;
		dp[x][1] = max(dp[x+1][0], dp[x+1][2]);
		dp[x][2] = max(dp[x+1][0], dp[x+1][1]);
        	//儿子染另外一种颜色
		// 上方代码完全是复制一遍到下面
		f[x][0] = min(f[x+1][1], f[x+1][2])+1;
		f[x][1] = min(f[x+1][0], f[x+1][2]);
		f[x][2] = min(f[x+1][0], f[x+1][1]);
	}
	else {
        //右儿子编号为k
		int k = ++cnt;
		dfs(k);
		dp[x][0] = max(dp[x+1][1] + dp[k][2], dp[x+1][2] + dp[k][1]) + 1;
		dp[x][1] = max(dp[x+1][0] + dp[k][2], dp[x+1][2] + dp[k][0]);
		dp[x][2] = max(dp[x+1][0] + dp[k][1], dp[x+1][1] + dp[k][0]);
		
		f[x][0] = min(f[x+1][1] + f[k][2], f[x+1][2] + f[k][1]) + 1;
		f[x][1] = min(f[x+1][0] + f[k][2], f[x+1][2] + f[k][0]);
		f[x][2] = min(f[x+1][0] + f[k][1], f[x+1][1] + f[k][0]);
	}
	ans1 = max(ans1, dp[x][0]);
}
int main() {
	scanf ("%s", s + 1);
	dfs(++cnt);
	cout << ans1 << ' ' << min(f[1][0], min(f[1][1], f[1][2])) << endl;
	return 0;
}
```

