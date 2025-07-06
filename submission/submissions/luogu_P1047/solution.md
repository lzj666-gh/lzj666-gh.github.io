# P1047 题解

### 思路
我们可以用一个 $flag$ 数组来记录每个位置的树是否被移走，如果为 $1$ 说明这个位置的树被移走，否则为没有被移走。我们可以每次输入两个数 $a,b$ ，然后将 $flag_a\sim flag_b$ 全都标记 $1$ ，最后我们遍历一遍 $0\sim l$ ，如果当前位置的树没有被移走最终答案就加一，最后输出最终答案。
### 代码
```cpp
#include<bits/stdc++.h>
#define int long long
using namespace std;
int flag[114514];
int ans;//ans为最终答案
signed main(){
	int l,m;
	cin>>l>>m;
	for(int i=1;i<=m;i++){
		int a,b;
		cin>>a>>b;
		for(int j=a;j<=b;j++)//标记
			flag[j]=1;
	}
	for(int i=0;i<=l;i++)
		if(!flag[i])//判断当前位置上的树是否没有被移走
			ans++;//增加最终答案
	cout<<ans;
	return 0;
}

```