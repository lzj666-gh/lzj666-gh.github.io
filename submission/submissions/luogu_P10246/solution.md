# P10246 题解

# C. Exciting Days 官方题解

本题涉及的主要知识点：

- 【1】模拟法
- 【3】排序
- （推荐）【4】`vector` 容器

---

记 $V$ 为特征值；$k=1$ 时应该什么都不输出，所以下面的讨论中默认 $k>1$。

## 前 $24\sim 44$ 分

枚举每个日期，然后判断其是否为 $k$ 的整数次幂。

若依次计算 $k^1,k^2,\ldots$ 判断是否相等，单次时间复杂度 $O(\log V)$，可得 $24$ 分。

但是如果把特征值除以 $k$，直到不能整除，再判断剩下的数是不是 $1$，时间复杂度就是平均 $O(1)$ 的了，可以拿到 $50$ 分。

测试点 $1$ 中 $k=6$ 的好处有二：不用判 $k=1$，$10^6$ 内 $6$ 的整数次幂不含 $0$。

## 正解

反过来，枚举特征值，然后找出特征值对应的日期。

特征值只有 $O(\log V)$ 个，并且每个特征值只有 $O(\log V)$ 位数，这也就意味着每个特征值最多对应 $O(\log V)$ 个日期，总体只需要判断 $O(\log ^2 V)$ 个日期是否合法。

判断完是否合法后，对答案进行排序输出。这一步可以是 `struct` 配合 STL 的 `sort`，也可以手写冒泡排序等。根据具体的实现方式，时间复杂度介于 $O(\log^2 V\log\log V)$ 和 $O(\log^4 V)$ 之间。

## 参考代码

以下为 C++ 代码：

```cpp
#include<bits/stdc++.h>
using namespace std;
const long long Mx=1e17;
int n,a[1000005];
long long k;
struct date{int m,d;};
bool operator < (date x,date y){return x.m<y.m || x.m==y.m && x.d<y.d;}
vector<date> all;
void mian(){
	scanf("%d%lld",&n,&k);
	for(int i=1;i<=n;i++)
		scanf("%d",&a[i]);
	if(k==1){puts("0");return;}
	for(long long v=k;;){
		long long sep=10;
		while(v/sep>n)sep*=10;
		while(v>=sep){
			long long m=v/sep,d=v%sep;
			if(d!=v%(sep/10) && 1<=d && d<=a[m])
				all.emplace_back((date){m,d});
			sep*=10;
		}
		if(v<=Mx/k)v*=k;
		else break;
	}
	sort(all.begin(),all.end());
	printf("%llu\n",all.size());
	for(date i:all)
		printf("%d %d\n",i.m,i.d);
}
int T;
int main(){
	for(scanf("%d",&T);T;T--){
		all.clear();
		mian();
	}
}
```

参考 Python 3 代码：

```python
for T in range(int(input())):
    n,k=map(int,input().split())
    a=[0]+list(map(int,input().split()))
    dates=[]
    Mx=10**16
    if k>1:
        val=k
        while val<Mx:
            T=str(val)
            for i in range(1,len(T)):
                m,d=T[:i],T[i:]
                if d[0]!='0' and 1<=int(m)<=n and int(d)<=a[int(m)]:
                    dates.append((m,d))
            val*=k
    def key_of(x):
        return int(x[0])*Mx+int(x[1])
    dates.sort(key=key_of)
    print(len(dates))
    for i in dates:
        print(i[0],i[1])
```