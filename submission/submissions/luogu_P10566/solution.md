# P10566 题解

[题目传送门](https://www.luogu.com.cn/problem/P10566)

### 题目大意
给定一个字符串 $s$，现在要将这个字符串变成只有大写字母的字符串。

设变换前的字符 `ASCII` 码为 $a$，变换后的 `ASCII` 码为 $b$。每一次变换的时间 $t$ 为 $|a-b|$。求 $t$ 的最小值。

### 题目分析
考虑暴力枚举。

我们可以先定义一个字符串的长度 $n$，然后再进行暴力枚举。

我们可以分成两类进行讨论：
- 当字符 $s_i \le 64$ 时，此时最小值为 $t = 65 - s_i$。
- 当字符 $s_i \ge 91$ 时，此时最小值为 $t = s_i - 90$。

所以即得最后答案 $t$。

### [代码](https://www.luogu.com.cn/record/161169767)
```cpp
#include <bits/stdc++.h>
using namespace std;
string s;
int n , t;
int main()
{
	cin >> s; 
	n = s.length();
	for(int i = 0;i < n;i++){
		if(s[i] > 'Z') t += s[i] - 'Z';
		if(s[i] < 'A') t += 'A' - s[i];
	}
	cout << t;
	return 0;
 } 
```