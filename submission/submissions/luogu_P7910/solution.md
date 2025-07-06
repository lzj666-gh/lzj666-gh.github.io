# P7910 题解

### 题目简述
给定长度为 $n$ 的序列 $a_i$。现在要维护单点修改与冒泡排序后一元素的下标。

$n\leq8000,q\leq2\times 10^5$，修改操作不超过 $5000$ 次。

### 解题思路

可以发现，对于一个已经有序的数列，单点修改一个值，我们可以通过前后冒泡各一次来保持有序，举个例子：

原序列为 $1,1,4,5,6,7$，修改为 $1,1,9,5,6,7$。

我们可以从前往后冒泡，再次维持了数列的有序。这样的操作是 $\mathcal{O}(n)$ 的。

同样的，我们可以维护一个有序数列，并记录原下标与先下标之间的关系（用数组记录），每次修改后更新这种关系。

这样，修改操作是 $\mathcal{O}(n)$ 的，查询是 $\mathcal{O}(1)$ 的。完结撒花。

下面给出考场代码：

```cpp
#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
const int MAXN=8005;
int n,q;
int t[MAXN];
struct node{
	int pre,id;
}a[MAXN];
bool cmp(node x,node y){
	if(x.pre!=y.pre) return x.pre<y.pre;
	return x.id<y.id;
}//两个元素之间的优先级
int main(){
	//freopen("sort.in","r",stdin);
	//freopen("sort.out","w",stdout);
	scanf("%d%d",&n,&q); 
	for(int i=1;i<=n;i++){
		scanf("%d",&a[i].pre);
		a[i].id=i;
	}//输入
	sort(a+1,a+n+1,cmp);//排序
	for(int i=1;i<=n;i++)
		t[a[i].id]=i;
	for(int i=1;i<=q;i++){
		int opt,x,v;
		scanf("%d",&opt);
		if(opt==1){//单点修改
			scanf("%d%d",&x,&v);//Ax->v
			a[t[x]].pre=v;
			for(int j=n;j>=2;j--)
				if(cmp(a[j],a[j-1])){
					node kkksc03=a[j];
					a[j]=a[j-1];
					a[j-1]=kkksc03;
				}//前扫
			for(int j=2;j<=n;j++)
				if(cmp(a[j],a[j-1])){
					node kkksc03=a[j];
					a[j]=a[j-1];
					a[j-1]=kkksc03;
				}//后扫
			for(int i=1;i<=n;i++)
				t[a[i].id]=i;//更新关系
		}
		else{
			scanf("%d",&x);
			printf("%d\n",t[x]);
		}
	}
	return 0;
}
```
update 2021.11.7

最近有一些小朋友问我为什么要前后各扫一次。

原因是更改的时候只修改了一个元素，我们不知道他是改大了还是改小了。

举个栗子，比如原序列是 $4,5,6$。

把 $5$ 改成 $1$ 就要往前扫，把 $5$ 改成 $9$ 就要往后扫。