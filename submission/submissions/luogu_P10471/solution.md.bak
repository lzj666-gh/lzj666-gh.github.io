# P10471 题解

## [P10471 最大异或对 The XOR Largest Pair](https://www.luogu.com.cn/problem/P10471) 题解

#### 题目简述：

共给你 $N$​ 个整数，其中任选两数进行**异或运算**，求最大值。

#### 分析算法：

1、枚举

时间复杂度：$O(N^2)$ ，直接排除，OUT。

2、运用字典树进行枚举，具体方法在后面。

#### 知识点梳理：

1、异或：两个数进行按位异或运算，相同为 $0$，不相同为 $1$。

2、字典树：

字典树（trie 树）是一种用于实现**字符串快速检索**的多叉树结构。

trie 树的每个节点都拥有若干个字符指针，若在插入或检索字符串时扫描到一个字符 c，就沿着当前节点的 c 字符指针，走向该指针指向的节点。

#### 思路分析：

上文提到，用枚举肯定超时。

考虑运用字典树对其进行优化。

优化方法：

把每一个数字转换成二进制的 $01$ 字符串插入字典树，再依次遍历整棵字典树。

遍历的时候我们该注意什么？该选择哪一条分支遍历下去？

选择：因为异或运算是相同为 $0$，不相同为 $1$，所以我们考虑贪心，即这一位尽量为 $1$。

给一个更直观的图片，以下即为字典树，存储的是数字 $3$、$2$、$1$、$0$：（别忘了二进制转化）。

![](https://cdn.luogu.com.cn/upload/image_hosting/kqs5mf6o.png)

**~~晚上11点临时画的，画技不好勿喷~~**

#### 代码实现：

字典树的代码实现：

```cpp
struct EDGE{//结构体存字典树 
	ll son[2];
}node[MAXN];
```

没错，就这么简单。`node[p].son[t]` 表示在字典树的 $p$ 号节点的第 $t$ 个分支（$t$ 为 $0$ 或 $1$）。

将一个数字插入操作：

```cpp
void insert(ll num)//插入数字num 
{
	now=0;
	for(int i=31;i>=0;i--)//一定是i>=0!!不是i;（血泪的教训，调到了晚上11点）
	{
		t=(num>>i)&1;//取该位
		if(!node[now].son[t]) node[now].son[t]=++cnt;//创建新的字典树节点 
		now=node[now].son[t];//更新现在所处的节点 
	}
	return;
}
```

查询操作：

```cpp
ll find(ll num)//查询数字num 
{
	ans=now=0;
	for(int i=31;i>=0;i--)//一定是i>=0!!不是i;（血泪的教训，调到了晚上11点） 
	{
		t=(num>>i)&1;
		if(!node[now].son[t^1])
			now=node[now].son[t];
		else
		{
			now=node[now].son[t^1];
			ans=ans^(1<<i);
		}
	}
	return ans;
}
```

好啦，接下来主函数很简单的，直接上完整代码：

```cpp
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
ll n,sum,ans,now;
bool t;
const int MAXN=1e7+5;
ll a[MAXN];
struct EDGE{//结构体存字典树 
	ll son[2];
}node[MAXN];
ll cnt;
inline void read(ll &num)//快读，不会的同学可忽略 
{
	char ch=getchar();
	while(ch<'0'||ch>'9')
	{
		if(ch=='-') num=-num;
		ch=getchar();
	}
	while(ch>='0'&&ch<='9')
	{
		num=(num<<1)+(num<<3)+(ch-'0');
		ch=getchar();
	}
	return;
}
void insert(ll num)//插入数字num 
{
	now=0;
	for(int i=31;i>=0;i--)//一定是i>=0!!不是i;（血泪的教训，调到了晚上11点）
	{
		t=(num>>i)&1;
		if(!node[now].son[t]) node[now].son[t]=++cnt;//创建新的字典树节点 
		now=node[now].son[t];//更新现在所处的节点 
	}
	return;
}
ll find(ll num)//查询数字num 
{
	ans=now=0;
	for(int i=31;i>=0;i--)//一定是i>=0!!不是i;（血泪的教训，调到了晚上11点） 
	{
		t=(num>>i)&1;
		if(!node[now].son[t^1])
			now=node[now].son[t];
		else
		{
			now=node[now].son[t^1];
			ans=ans^(1<<i);
		}
	}
	return ans;
}
int main(){
	read(n);
	for(int i=1;i<=n;i++)
	{
		read(a[i]);
		insert(a[i]);
	}
	for(int i=1;i<=n;i++)
		sum=max(sum,find(a[i]));//打擂台 
	printf("%lld\n",sum);
	return 0;
}
```

**[AC 记录](https://www.luogu.com.cn/record/161540694)**

**附：如果你会了本题，建议去做双倍经验[P4551 最长异或路径](https://www.luogu.com.cn/problem/P4551)**