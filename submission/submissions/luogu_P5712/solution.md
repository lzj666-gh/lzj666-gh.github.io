# P5712 题解

**[题目传送门](https://www.luogu.com.cn/problem/P5712)**


**思路**

1. 仔细读题后，我们可以发现，输出可以分成$2$种情况，`apple`加`s`与`apple`不加`s`，所以我们可以使用`if/else`来实现。

2. 接着，我们读入`n`。
```cpp
	int n;
	cin>>n;
```

3. 进行判断，是否需要加`s`
```cpp
	if(n==1 || n==0) cout<<"Today, I ate "<<n<<" apple.";
	else cout<<"Today, I ate "<<n<<" apples.";
```

**参考代码**
```cpp
#include <bits/stdc++.h>
using namespace std;
int main()
{
	int n;
	cin>>n;
	if(n==1 || n==0) cout<<"Today, I ate "<<n<<" apple.";
	else cout<<"Today, I ate "<<n<<" apples.";
	return 0;
}
```