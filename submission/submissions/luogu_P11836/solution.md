# P11836 题解

## [题目传送门](https://www.luogu.com.cn/problem/P11836)
一道简单的二维数组加调整题目。  
## 解题思路
先将面布输入，判断是否涂色，进行第一次计算。  

对于 $U$ 次修改，说明如下：  
是将画布变成一种在水平、垂直中都对称的状态，并确定修改后变成对称所需的最小的操作数。  

对于每次修改，仅需修改一个点，变化也只和这一个点有关，只计算这一个点的变化即可。  
具体来说，原答案先减去这个点没修改时的值，在加上这个点修改后的值，就是当前的答案。

再将这些答案一并输出，即可 AC。  
## AC CODE
```cpp
#include <bits/stdc++.h>
using namespace std;
bool maP[2010][2010];
int ans[100010];
int main() {
	int n, u;
	cin >> n >> u;
	int sum = 0;
	int cnt1 = 0, cnt2 = 0;
	for (int i = 1; i <= n; i++) { //输入面布
		for (int j = 1; j <= n; j++) {
			char c;
			cin >> c;
			if (c == '#') { //判断是否被涂色
				maP[i][j] = 1;
			} else {
				maP[i][j] = 0;
			}
		}
	}
	for (int i = 1; i <= n / 2; i++) { //根据输入的面布进行计算
		for (int j = 1; j <= n / 2; j++) {
			cnt1 = 0;
			if (maP[n - i + 1][n - j + 1] != maP[i][j]) {
				cnt1++;
			}
			if (maP[n - i + 1][j] != maP[i][j]) {
				cnt1++;
			}
			if (maP[i][n - j + 1] != maP[i][j]) {
				cnt1++;
			}
			sum += min(cnt1, 4 - cnt1);
		}
	}
	cout << sum << endl;
	int r, c;
	int out = 0;
	for (int i = 1; i <= u; i++) { //通过更新次数进行翻转并记录最小操作量
		cnt1 = cnt2 = 0;
		cin >> r >> c;
		if (maP[r][c] != maP[n - r + 1][n - c + 1]) {
			cnt1++;
		}
		if (maP[r][c] != maP[n - r + 1][c]) {
			cnt1++;
		}
		if (maP[r][c] != maP[r][n - c + 1]) {
			cnt1++;
		}
		cnt1 = min(cnt1, 4 - cnt1);
		if (maP[r][c] == 0) {
			maP[r][c] = 1;
		} else {
			maP[r][c] = 0;
		}
		if (maP[r][c] != maP[n - r + 1][n - c + 1]) {
			cnt2++;
		}
		if (maP[r][c] != maP[n - r + 1][c]) {
			cnt2++;
		}
		if (maP[r][c] != maP[r][n - c + 1]) {
			cnt2++;
		}
		cnt2 = min(cnt2, 4 - cnt2);
		sum += cnt2 - cnt1;
		ans[out] = sum;
		out++;
	}
	for (int i = 0; i < out; i++) {
		cout << ans[i] << endl; //输出答案
	}
}
```
为保持洛谷的良好学习习惯，请勿抄袭。  
**千万别抄袭哦。**  
管理大大辛苦了，各位大佬给蒟蒻点个赞呗。