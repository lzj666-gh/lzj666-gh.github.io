# P11227 题解

欢迎报名[洛谷网校](https://class.luogu.com.cn/)，期待和大家一起进步！

本题要求出在给定的扑克牌的基础上，还需要多少张牌可以让扑克牌凑成一整套，而试题中读入的字符串每个都代表一张合法的扑克牌，从而可以使用 C++ STL 中的 set（集合）完成本题。这是因为，set 可以自动去重，去除重复的牌（字符串）后，剩下的字符串就是实际拥有的不同的牌。而一副扑克牌有 $52$ 张牌，使用 $52$ 减去该集合的大小即可求出答案。

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
	set <string> S;
	int n;cin >> n;
	for (int i=1;i<=n;i++) {
		string s;
		cin >> s;
		S.insert(s);
	}
	cout << 52-S.size() << endl;
	return 0;
}
```