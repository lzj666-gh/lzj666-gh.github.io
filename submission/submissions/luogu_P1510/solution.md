# P1510 题解

## QAQ蒟蒻红名后第一篇题解吼吼吼
（以前的都没有过）

 哭辽
 
 
 身为蒟蒻的我 看到这道题就笑了 这不就是个01背包吗 哈哈哈  又可以水题了
 
 十分钟后。。。算了 先玩会吧 这题不简单
 
 对 就是 这题不简单 乍一看是一道水题 实际上暗藏杀气QAQ
 
 
 # 不扯了 进入正题
 
####  这道的的确确是一道01背包 还是道不错的练手题
 
 首先 此题有三个量 我们需要先理清他们之间的关系
 
 ```cpp
int vn,n,c,sum;//vn：need—v（所需总体积） n：石子个数 c：总体力 
int v[MAXN],w[MAXN],f[MAXN];//v：石子体积 w：所需体力 
```

大致的都写出来了 然后看数据范围 <=10000  QAQ 有点大
来波快读

```
inline int read(){//（推销一波）如老衲所见 必有大数据 所以还是有必要来个快读优化的QAQ 
    int x=0,f=1;char ch=getchar();
    while (ch<'0'||ch>'9') {if(ch=='-')f=-1; ch=getchar();}
    while (ch>='0'&&ch<='9'){x=(x<<3)+(x<<1)+ch-'0'; ch=getchar();}
    return x*f;
}
```

然后就该开始无尽的思索了 这题的状态转移方程是什么？

本蒟蒻的思路是将体力看做背包 将石子看做物品 然后就很自然地得出了本题的状态转移方程：

## f[j]=max(f[j],f[j-w[i]]+v[i])

然后就是蒟蒻的代码了（码丑勿批QAQ）

```cpp
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#define int long long
#define MAXN 10000+3
using namespace std;

inline int read(){//（推销一波）如老衲所见 必有大数据 所以还是有必要来个快读优化的QAQ 
    int x=0,f=1;char ch=getchar();
    while (ch<'0'||ch>'9') {if(ch=='-')f=-1; ch=getchar();}
    while (ch>='0'&&ch<='9'){x=(x<<3)+(x<<1)+ch-'0'; ch=getchar();}
    return x*f;
}

int vn,n,c,sum;//vn：need—v（所需总体积） n：石子个数 c：总体力 
int v[MAXN],w[MAXN],f[MAXN];//v：石子体积 w：所需体力  

signed main()
{
	vn=read(),n=read(),c=read();
	for(int i=1;i<=n;i++){
		v[i]=read(),w[i]=read();
//		cout<<v[i]<<" "<<w[i]<<endl;
		sum+=v[i];
//		cout<<sum<<endl;
	}
	if(sum<vn){//若石子总体积<vn，直接输出Impossible （特判一波）
		cout<<"Impossible"<<endl;
		return 0;
	}
//	cout<<"ha"<<endl;静态测试 检查代码在哪里出的锅QAQ 
	for(int i=1;i<=n;i++){
		for(int j=c;j>=w[i];j--){
			f[j]=max(f[j],f[j-w[i]]+v[i]);
		}
	}
	for(int i=0;i<=vn;i++){//从小到大搜 第一个大于vn的直接输出
		if(f[i]>=vn){
			cout<<c-i<<endl;
			return 0;
		}
	}
	cout<<"Impossible"<<endl;
	return 0;
}
```

# 码字不易 求过 求各位大爷赏个赞