# CF1842B 题解

## 题目大意

给定 $a$，$b$，$c$ 三个大小为 $n$ 栈，把 $u$ 初始化为 $0$，接下来可以挑选三个栈顶的的一个数 $v$，每次进行一次操作，使得 $u=u \operatorname{or} v$，最终问你 $u$ 能不能变为 $x$（不懂位运算的[戳这里](https://oi-wiki.org/math/bit/#%E4%B8%8E%E6%88%96%E5%BC%82%E6%88%96)）。

## 题目思路

比较暴力的贪心，尽量的多看一些书，到最后如果和 $x$ 相同就出 `yes`，这里提一嘴 `yEs`、`yes`、`Yes`、`YES` 都是可以的否则栈空的话的话就 `no`。

## 代码

本人不打空格还压行，码风太丑请见谅。

```cpp
#include<bits/stdc++.h>
using namespace std;
#define P
#define R read()
#define int long long
const int N=1e5+5;
int a[N],b[N],c[N],t,n,x;
inline int read(){//快读
	int x=0,f=1;char ch=getchar();
	while(ch<'0'||ch>'9'){if(ch=='-') f=-1;ch=getchar();}
	while(ch>='0'&&ch<='9'){x=(x<<1)+(x<<3)+ch-'0';ch=getchar();} 
	return x*f;
}
signed main(){
	t=R;
	while(t--){
		n=R;x=R;
		int xa=1,xb=1,xc=1,now=0;//多组数据初始化，直接开在循环里
		for(int i=1;i<=n;i++) cin>>a[i];
		for(int i=1;i<=n;i++) cin>>b[i];
		for(int i=1;i<=n;i++) cin>>c[i];
		while(xa<=n&&(a[xa]|x)==x) now|=a[xa++];//判断是否栈顶是否合法，不合法退出
		while(xb<=n&&(b[xb]|x)==x) now|=b[xb++];//同理
		while(xc<=n&&(c[xc]|x)==x) now|=c[xc++];
		if(now==x) P("Yes\n");
		else P("No\n");
	}
	return 0;//结束
}
```