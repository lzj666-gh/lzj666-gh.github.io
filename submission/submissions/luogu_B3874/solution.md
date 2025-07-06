# B3874 题解

分析题意不难看出，如果所有人倒序进入教室，就变成了普通的逆序对问题。

直接归并排序或者树状数组求解即可。

解法一：归并排序
```
#include<iostream>
using namespace std;
const int N = 3e5+5;
int n;
int a[N], b[N];
long long ans = 0;

void merge(int l, int r)
{
	int mid = l + r >> 1;
	if(l>=r)
		return;
	merge(l, mid);
	merge(mid+1, r);
	int i = l, j = mid + 1, k = 0;
	while(i<=mid && j<=r)
	{
		if(a[i]>a[j])
		{
			ans += mid - i + 1;
			b[++k] = a[j++];
		}
		else
			b[++k] = a[i++];
	}
	while(i<=mid)
		b[++k] = a[i++];
	while(j<=r)
		b[++k] = a[j++];
	
	for(int i=l;i<=r;i++)
		a[i] = b[i-l+1];
}

int main()
{
	cin>>n;
	for(int i=n;i;i--)	//倒序读入数据
		cin>>a[i];
	merge(1, n);
	cout<<ans;
	return 0;
}
```

解法二：树状数组
```
#include<iostream>
using namespace std;
const int N = 3e5+5;
int n;
int a, c[N];
long long ans;

int lowbit(int x)
{
	return x & -x;
}

void add(int x, int y)
{
	for(int i=x;i<=n;i+=lowbit(i))
		c[i] += y;
}

int ask(int x)
{
	int res = 0;
	for(int i=x;i;i-=lowbit(i))
		res += c[i];
	return res;
}

int main()
{
	cin>>n;
	for(int i=n;i;i--)
	{
		cin>>a;
		a++;	//由于lowbit(0)=0，注意把a整体向右偏移一位 
		ans += ask(a-1);
		add(a, 1);
	}
	cout<<ans;
	return 0;
}
```