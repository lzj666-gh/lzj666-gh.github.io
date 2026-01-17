# P5595 题解

## Solution

拿到这个题，不要被它吓到了。仔细分析一下，你就知道如何处理了。

第一种情况：只有X,Y。

那么如果是X,就输出1,Y则为0。

```cpp
sample input: XY
sample output: 10 01
```

如果有解且有Z,则有Z的位置为1。

```cpp
sample input: XYZ
sample output: 101 011
```

如果无解,那么就是说Z和XY冲突了。

首先，如果其中一位是Z，则Z后的所有位置都为Z。

```cpp
sample input: XYZZ
sample output: 1011 0111
```

如果不是Z,比如下面这个：

```cpp
sample input: XYZXZ
sample output: -1
```

直接输出"-1"。

那么这个题就解决了。

code:

```cpp
#include<bits/stdc++.h>
#define N 1000006
using namespace std;

string s;
int a[N],b[N];

bool pd(string s){
	bool flag=0;
	for(int i=0;i<s.size();i++){
		if(s[i]=='Z') flag=1;
		if(flag==1 && s[i]!='Z') return 1; 
	}
	return 0;
} //一位一位判断Z

int main(){
	cin>>s;
	if(pd(s)) return puts("-1"), 0; //无解输出-1
	for(int i=0;i<s.size();i++)
		if(s[i]=='X') a[i]=1,b[i]=0;
		else if(s[i]=='Y') a[i]=0,b[i]=1;
		else if(s[i]=='Z') a[i]=1,b[i]=1;
	for(int i=0;i<s.size();i++) cout<<a[i]; cout<<endl; //输出是有换行的
	for(int i=0;i<s.size();i++) cout<<b[i]; cout<<endl;
	return 0;
}
```