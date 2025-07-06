# P10466 题解

[题目链接](https://www.luogu.com.cn/problem/P10466)

### 思路分析
对于每一个数字 $A_i$ 而言，要得到一个值，使得它们的差的绝对值最小，那么这个值只可能是在排序情况下的前一个或后一个位置的值。

若直接暴力计算，则可以使用插入排序，每次插入一个新的值，再进行上述方法的一个判断，时间复杂度为 $O(n^2)$，只能得 80 分。因此，需要考虑其它更优的方法解题。

我们可以思考这样一个问题：若要减少时间复杂度，那就要优化成一个 $O(n \log n)$ 排序，可是排完序后又该怎么做呢？我们可以发现，对于最后一个数字而言，因为它后面没有数字，所以，这个数字的答案为排序后它前面那个数字与它的差的绝对值。而在除去最后一个数字后，倒数第二个数字又成了新的最后一个数字，又可以用同样的方式计算答案。

这里我们可以用链表完成删除数据的操作，可是动态链表每一次查询的时间复杂度太大，所以采用查询速度更快的静态链表，利用结构体储存。这样我们就可以实现 $O(n \log n)$ 的排序；每个数字 $O(1)$，总计 $O(n)$ 的查询。

### 代码
```cpp
#include<bits/stdc++.h>
#define int long long
using namespace std;
const int N=1e5+5;
pair<int, int> a[N],ans[N];
int p[N],L[N],R[N];
signed main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int n,x;
	cin>>n;
	for(int i=1;i<=n;i++)
	{
		cin>>x;
		a[i]={x,i};
	}
	sort(a+1,a+n+1);
	a[0].first=INT_MIN;
	a[n+1].first=INT_MAX; 
	for(int i=1;i<=n;i++)
	{
		p[a[i].second]=i; 
		L[i]=i-1,R[i]=i+1;
	}
	for(int i=n;i>1;i--)
	{
		int k=p[i],left=L[k],right=R[k],v=a[k].first;
		int l=v-a[left].first;
		int r=a[right].first-v;
		if(l<=r)
			ans[i]={l,a[left].second};
		else 
			ans[i]={r,a[right].second}; 
		L[right]=left;
		R[left]=right; 
	}
	for(int i=2;i<=n;i++)
		cout<<ans[i].first<<" "<<ans[i].second<<"\n";
}
```