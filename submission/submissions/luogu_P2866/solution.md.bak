# P2866 题解

[题目传送门](https://www.luogu.com.cn/problem/P2866)

本题考查对栈的应用

## 题目解法：
1. 每次输入一头牛的身高，找比这头牛矮的，出栈

1. 剩下的牛皆可以看到这只牛

1. ans值加等于栈中牛的个数

1. 这头牛入栈

# Code：
```cpp
#include<bits/stdc++.h>
using namespace std;
int n,t;
long long ans; //注意要开long long 
stack <int> a;
int main() {
	cin>>n;
	for (int i=1; i<=n; i++) {
		cin>>t;
		while (!a.empty()&&a.top()<=t)  
			a.pop();
		ans+=a.size();
		a.push(t);
	}
	cout<<ans;
	return 0;
}
```

都看到这了，点个赞呗QwQ