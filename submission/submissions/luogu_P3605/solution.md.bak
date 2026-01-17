# P3605 题解

[${\color{#aa66ee}\text{欢迎拜访我这个蒟蒻的博客}}$](https://www.luogu.com.cn/blog/Wendigo/)

[P3605 【\[USACO17JAN\]Promotion Counting晋升者计数】](https://www.luogu.com.cn/problem/P3605)

### 此题算法:树状数组+$dfs$

这仔细一想是道比较纯的树状数组题

~~你看了粉兔的题解后会发现那个$a[]$数组尤为鬼畜~~

![](https://s2.ax1x.com/2019/12/06/QYYvVA.jpg)

>(手画抨击粉兔)

**我这里有最容易理解的算法，走过路过不要错过**

首先将拿到的数组**离散化**(如下)

```cpp
for(int i=1;i<=n;i++)
	scanf("%d",p+i),b[i]=p[i];
sort(b+1,b+n+1); //unique什么的真的没啥用
for(int i=1;i<=n;i++)
	p[i]=lower_bound(b+1,b+n+1,p[i])-b;
```
加完**单向边**后$dfs$：

若令$ans[]$表示节点的最终答案，则有

>**$ans[x]=x$的下属中比$x$强的**

>**$~~~~~~~~~~~~=$树状数组中加了$x$下属后比$x$强的$-$原来就比$x$强的**

所以$dfs$可以写成这样：

```cpp
void dfs(int x){//x为节点，p[]为离散化后的数组
	//hx为值域树状数组
	ans[x]=-(hx.fsum(n)-hx.fsum(p[x]));//原来比x强的
	for(auto i:g[x]) dfs(i);     //加x的下属
	ans[x]+=(hx.fsum(n)-hx.fsum(p[x]));//后来比x强的
	hx.fix(p[x],1); //加x自己
}
```
![](https://s2.ax1x.com/2019/12/06/QYUCng.jpg)




## 以下是代码+注释

```cpp
#include <bits/stdc++.h>
using namespace std;
const int N=1e5+10;
int n,p[N],b[N],ans[N];
vector<int> g[N];
struct hxtree{ //树状数组
	int v[N];
	int flow(int x){
		return x&-x;
	}
	void fix(int x,int y){
		for(;x<=n;x+=flow(x))
			v[x]+=y;
	}
	int fsum(int x){
		int ret=0;
		for(;x;x-=flow(x))
			ret+=v[x];
		return ret;
	}
}hx;
void dfs(int x){//x为节点，p[]为离散化后的数组
	//hx为值域树状数组
	ans[x]=-(hx.fsum(n)-hx.fsum(p[x]));//原来比x强的
	for(auto i:g[x]) dfs(i);     //加x的下属
	ans[x]+=(hx.fsum(n)-hx.fsum(p[x]));//后来比x强的
	hx.fix(p[x],1); //加x自己
}
int main(){
	scanf("%d",&n);
	for(int i=1;i<=n;i++)
		scanf("%d",p+i),b[i]=p[i];
	sort(b+1,b+n+1); //对萌新很友好的两步离散化
	for(int i=1;i<=n;i++)
		p[i]=lower_bound(b+1,b+n+1,p[i])-b;
	// for(int i=1;i<=n;i++)
	// 	printf("%d%c",p[i]," \n"[i==n]);
	for(int i=2;i<=n;i++){
		int fa;
		scanf("%d",&fa);
		g[fa].push_back(i);
	}
	dfs(1);
	for(int i=1;i<=n;i++)
		printf("%d\n",ans[i]); //1+1=2
	return 0;
}
```

这题就像身边的“萌新”向自己学习，

结果不久他们就分到了省选班，而自己越来越弱。

**写题解不易，喜欢就点个赞吧。**

谢谢大家! !






