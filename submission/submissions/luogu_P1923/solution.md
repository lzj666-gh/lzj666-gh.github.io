# P1923 题解

# 思路 1 (60pts)： $O(nlog_2n)$

想法：对原数组进行快速排序，然后 $O(1)$ 输出。

```cpp
#include<bits/stdc++.h>
using namespace std;
int x[5000005],k;
int main()
{
	int n;
	scanf("%d%d",&n,&k);
	for(int i=0;i<n;i++)
		scanf("%d",&x[i]);
	sort(x,x+n);//快排
	printf("%d",x[k]);
}
```

# 思路 2 (100pts)： $O(n)$

想法：根据快排思想来寻找第 $k$ 小的数。

快排的核心思想是二分。

在原二分的基础上可以进行修改：因为每次递归都会将数组划分为三部分，而答案只会在这三部分中的一个，不需要再对其他部分进行搜索，从而达到优化时间复杂度的效果。

```cpp
#include<bits/stdc++.h>
using namespace std;
int x[5000005],k;
void qsort(int l,int r)
{
	int i=l,j=r,mid=x[(l+r)/2];
	do
	{
		while(x[j]>mid)
			j--;
		while(x[i]<mid)
			i++;
		if(i<=j)
		{
			swap(x[i],x[j]);
			i++;
			j--;
		}
	}
	while(i<=j);
	//快排后数组被划分为三块： l<=j<=i<=r
	if(k<=j) qsort(l,j);//在左区间只需要搜左区间
	else if(i<=k) qsort(i,r);//在右区间只需要搜右区间
	else //如果在中间区间直接输出
	{
		printf("%d",x[j+1]);
		exit(0);
	}
}
int main()
{
	int n;
	scanf("%d%d",&n,&k);
	for(int i=0;i<n;i++)
		scanf("%d",&x[i]);
	qsort(0,n-1);
}
```

# 思路 3 (100pts)：$O(n)$

~~C++ 的宝库：STL~~

在 STL 里有一个神奇的函数 `nth_element`。

它的用法是 `nth_element(a+x,a+x+y,a+x+len);`。

执行之后数组 $a$ 下标 $x$ 到 $x+y-1$ 的元素都小于 $a[x+y]$，下标 $x+y+1$ 到 $x+len-1$ 的元素 都大于 $a[x+y]$，但不保证数组有序。此时 $a[x+y]$ 就是数组区间 $x$ 到 $x+len-1$ 中第 $y$ 小的数，当然也可以自己定义 $cmp$ 函数。

结论：差不多就是将我们的思路 2 做了一遍。

`nth_element` 的时间复杂度是 $O(n)$ 的，不过 STL 常数普遍较大……但还是能过此题。

```cpp
#include<bits/stdc++.h>
using namespace std;
int x[5000005],k;
int main()
{
	int n;
	scanf("%d%d",&n,&k);
	for(int i=0;i<n;i++)
		scanf("%d",&x[i]);
	nth_element(x,x+k,x+n);//简短又高效
	printf("%d",x[k]);
}
```