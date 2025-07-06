# P2615 题解

### 思路：
这题很简单，就是根据题目意思写就行了。

首先得把幻方的中间写上一。

然后再来看条件

条件一：若 $(K-1)$ 在第一行但不在最后一列，则将 $K$ 填在最后一行， $(K-1)$ 所在列的右一列。
```cpp
if (x == 1) {
    x = n;
    y++;
} 
```
条件二：若 $(K-1)$ 在最后一列但不在第一行，则将 $K$ 填在第一列， $(K-1)$ 所在行的上一行。
```cpp
if (y == n) {
    x--;
    y = 1;
} 
```
条件三：若 $(K-1)$ 在第一行最后一列，则将 $K$ 填在 $(K-1)$ 的正下方。
```cpp
if ((x == 1 && y == n) || a[x - 1][y + 1]) x++;
```
否则，就是：
```cpp
else {
    x--;
    y++;
}
```

最后，将这几个串在一起，就有了最终的代码了。

---

### code：
```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAXN = 40;
int a[MAXN][MAXN], n, x = 1, y = 0;

int main() {
	cin >> n;
	y = n / 2 + 1;
	for (int i = 1; i <= n * n; i++) {
		a[x][y] = i;
		if ((x == 1 && y == n) || a[x - 1][y + 1]) x++;
		else if (x == 1) {
			x = n;
			y++;
		} else if (y == n) {
			x--;
			y = 1;
		} else {
			x--;
			y++;
		}
	}
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) cout << a[i][j] << ' ';
		cout << endl;
	}
	return 0;
}
```