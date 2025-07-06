# P1067 题解

### 思路

这一题我们要分情况讨论。

情况分为以下几种：

- 当前 $i\not= n$ 并且输入的数是正数，输出 `+`。
- 当前 $i\not= 0$ 并且输入的数是 $-1$，输出 `-`。
- 输入的数的绝对值大于 $1$ 或者当前 $i=0$，输出输入的数。
- 当前 $i>1$，输出 `x^` 和 $i$。
- 当前 $i=1$，输出 `x`。

注意，以上情况当且仅当输入的数不为 $0$ 时才成立。

### 代码

```cpp
#include<bits/stdc++.h>
#define int long long
using namespace std;
signed main(){
	int n;
	cin>>n;
	for(int i=n;i>=0;i--){//注意，循环要从大到小
		int x;
		cin>>x;
		if(x){
			if(i!=n&&x>0)
				cout<<'+';
			if(i!=0&&x==-1)
				cout<<'-';
			if(abs(x)>1||i==0)
				cout<<x;
			if(i>1)
				cout<<"x^"<<i;
			if(i==1)
				cout<<'x';
		}
	}
	return 0;
}
```