# P1149 题解

## [P1149 [NOIP 2008 提高组] 火柴棒等式 题解](https://www.luogu.com.cn/problem/P1149)
## 题目简述
一共有 $n$ 根火柴，求能拼出多少个 $A + B = C$，且 $A \neq B$。
## 思路讲解
刚刚看到这道题，毫不犹豫地打气暴力枚举，毕竟，暴力出奇迹吗。

首先，先把 $0 \sim 9$ 所以数字所需要的火柴数记录到一个数组中。如何三重循环 $1 \sim 10$，火柴数相加等于 $n$，并且 $A + B = C$。

暴力代码如下：
```cpp
#include <bits/stdc++.h>
using namespace std;
#define int long long
const int maxn = 2e4;
const int num[] = {0,6,2,5,5,4,5,6,3,7,6};
int n,ans;
signed main(){
	ios::sync_with_stdio(false);
	cin.tie(0),cout.tie(0);
	cin >> n;
	for(int i = 1;i <= 10;i++){
		for(int j = 1;j <= 10;j++){
			for(int k = 1;k <= 10;k++){
				if(i + j == k && num[i] + num[j] + num[k] + 4 == n && i != j){
					ans++;
				}
			}
		}
	}
	cout << ans << endl;
	return 0;
}
```
[20 分提交记录。](https://www.luogu.com.cn/record/201303319)

这是为什么呢。很简单，这个操作只能进行 $10$ 以内的加法计算。我们需要再建立一个数组，存下 $1 \sim 2000$ 的数字火柴数，然后暴力。

注意点：

1. 第 $12$ 行记得 $j$ 一定要大于 $0$.
2. 第 $16$ 和 $17$ 两行 $i$ 和 $j$ 只能循环到 $1000$，不然报错。
3. 第四行，我一不小心在 $6$ 之前 加了个 $0$。
```cpp
#include <bits/stdc++.h>
using namespace std;
const int maxn = 2000;
const int num[] = {6,2,5,5,4,5,6,3,7,6};
int n,ans,a[maxn + 5];
signed main(){
	ios::sync_with_stdio(false);
	cin.tie(0),cout.tie(0);
	cin >> n;
	a[0] = 6;                                         //数字 0 有 6 个火柴
    for (int i = 1;i <= 2000;i++){
        for (int j = i;j;j /= 10){                    //从最高位开始，一个数位一个数位地加上火柴数
            a[i] += num[j % 10];
        }
    }
    for (int i = 0;i <= 1000;i++){
        for (int j = 0;j <= 1000;j++){
            if (a[i] + a[j] + a[i + j] + 4 == n){    //a[i] 就是第一个数，a[j] 就是第二个数。
                ans++;                               //a[i + j]就是第三个数。加上的 4 就是 + 和 =。
            }
        }
    }
	cout << ans << endl;
	return 0;
}
```
[提交记录。](https://www.luogu.com.cn/record/201307646)

感谢观看，求赞。