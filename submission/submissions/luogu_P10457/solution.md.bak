# P10457 题解

### 题意

- 从生命牌中抽取的最上面一张。
- 把这张牌放到对应编号的堆的最上边。
- 从刚放了牌的那一堆最底下抽取一张牌，重复第 $2$ 步。
- 在抽牌过程中如果抽到 $K$，则称死了一条命，就扔掉 $K$ 再从第 $1$ 步开始。

总共有 $4$ 条命，当 $4$ 条命头没了，就输出总对数。

### 思路

使用`deque`解决。

先输入，将字母改为数字并放入数组。

再模拟步骤，一边判断，一边模拟。

最后找有几个总对数。

### 注意

需要将以下的字母与数字修改：

`0`变为`10`。

`A`变为`1`。

`J`变为`11`。

`Q`变为`12`。

`K`变为`13`。

### 代码

输入，如下。

```cpp
for(int i=1;i<=13;i++){
		for(int j=1;j<=4;j++){
			cin>>x;
			if(x<='9'&&x>='1')a[i].push_back(x-'0');
			else if(x=='0')a[i].push_back(10);
			else if(x=='J')a[i].push_back(11);
			else if(x=='Q')a[i].push_back(12);
			else if(x=='K')a[i].push_back(13);
			else if(x=='A')a[i].push_back(1);
	}
}
```

模拟，如下。

在这里我用了点优化，边循环，边统计对数。

```cpp
while(!a[13].empty()) {
        int t=a[13].front();
		a[13].pop_front();
        while(t!=13) {
            b[t]++;
            if(b[t]>=4)sum++;
            int p=a[t].back();
			a[t].pop_back();
			t=p;
        }
    }
```

整体代码，如下。

```cpp
#include<bits/stdc++.h>
#define int long long
using namespace std;
deque<int> a[20];
int b[20],sum;
char x;
signed main(){
	for(int i=1;i<=13;i++)
		for(int j=1;j<=4;j++){
			cin>>x;
			if(x<='9'&&x>='1')a[i].push_back(x-'0');
			else if(x=='0')a[i].push_back(10);
			else if(x=='J')a[i].push_back(11);
			else if(x=='Q')a[i].push_back(12);
			else if(x=='K')a[i].push_back(13);
			else if(x=='A')a[i].push_back(1);
	}
	while(!a[13].empty()) {
        int t=a[13].front();
		a[13].pop_front();
        while(t!=13) {
            b[t]++;
            if(b[t]>=4)sum++;
            int p=a[t].back();
			a[t].pop_back();
			t=p;
        }
    }
	cout<<sum;
	return 0;
}
```