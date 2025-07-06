# P1051 题解

## solution

小模拟。

按题意读入后，求这个人的奖金，这里判断这个人能否获得某项奖金，可以用逻辑表达式减少代码量，即若表达式成立返回 $1$ 否则返回 $0$，用逻辑表达式的结果乘上某项的奖金，就是这个人在某项上获得的奖金。最后别忘了计算总奖金。

## code

```cpp
#include<bits/stdc++.h>
using namespace std;
int n, a, b, e, sum, Sum, mx;
string s, ans;
int main () {
	cin >> n;
	for (char c, d; n--; Sum+=sum) {
		cin >> s >> a >> b >> c >> d >> e;
		sum=(a>80&&e)*8000+
			(a>85&&b>80)*4000+
			(a>90)*2000+
			(a>85&&d=='Y')*1000+
			(b>80&&c=='Y')*850;
		if (sum>mx)
			mx=sum,
			ans=s;
	} 
	cout << ans << '\n' << mx << '\n' << Sum;
	return 0;
}
```