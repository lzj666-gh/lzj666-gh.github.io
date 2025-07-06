# P1061 题解

虽然这题有点水，但是逛了一圈题解区，没有令我满意的$dfs$做法。

个人认为$dfs$是十分优美的，她的自相似的性质总是如此迷人，所以我们写$dfs$的时候也要优雅一点才好。

-------------------

题意不再赘述，下面我们直接分析$dfs$过程。

```
void dfs(int pos,int step)
{
	if(pos==0)return;
	if(step==6)return;
	if(a[pos]<t&&a[pos<a[pos+1]-1)
	{
		a[pos]++;
		for(int i=pos+1;i<=w;i++)
		a[i]=a[i-1]+1;
		output();
		dfs(w,step+1);
	}
	else dfs(pos-1,step);
}
```

我们用数组$a[30]$表示$Jam$数，下标从$1$开始。

### 递归边界

- 因为最多只要输出$5$个字符串（事实上该算法也因此效率较高，不必担心超时问题），所以计算5个之后就可以直接结束了，因此
**$if(step==6)return;$**

- 宏观上讲，我们是把a数组的元素一个一个往后移，所以当第一个元素都不可以移动时，自然程序也就结束了。
**$if(pos==0)return;$**

### 状态转移

- 如果位置为$pos$的a数组元素可以向后移动，那么我们将其移动一位，同时因为要保证jam数从小到大，我们把pos后面的元素往前移动，这不难理解，前面元素的“权”大于后面元素的“权”，如果要使得序列单调递增，就必须这么做。

- 如果位置为pos的元素不能移动，那么我们就移动位置为pos-1的元素。

----------------------

代码：

```
//code by rainman
#include<bits/stdc++.h>
using namespace std;

int s,t,w,c;
int a[30],cnt;

inline void output()
{
	for(int i=1;i<=w;i++)
	cout<<(char)('a'+a[i]-1);
	cout<<endl;
}

void dfs(int pos,int step)
{
	if(pos==0)return;
	if(step==6)return;
	if(a[pos]<t&&a[pos]<a[pos+1]-1)
	{
		a[pos]++;
		for(int i=pos+1;i<=w;i++)
		a[i]=a[i-1]+1;
		output();
		dfs(w,step+1);
	}
	else dfs(pos-1,step);
}

int main()
{
	cin>>s>>t>>w;
	fflush(stdin);
	while((c=getchar())!=EOF)
	{
		int temp=c-'a'+1;
		if(temp>=1&&temp<=26)a[++cnt]=temp;
	}
	
	a[w+1]=0x7f;
	dfs(w,1);
	return 0;
}
```