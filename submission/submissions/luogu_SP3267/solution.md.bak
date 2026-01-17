# SP3267 题解

今天机房讲了莫队。

但是蒟蒻我并没有听懂，所以晚上回家恶补，才弄明白莫队。

莫队是莫涛大神发明的，它的作用就是用优秀的复杂度求解于一些区间之间的操作，莫队其实就是一个优雅的暴力，它的复杂度是O(n sqrt(n))；

以此[题](https://www.luogu.org/problemnew/show/SP3267)为例，其实这题和[这题](https://www.luogu.org/problemnew/show/P1972)是一样的，不过P1972会卡莫队。

回到此题：

题意很直白，我就不多赘述；

思路1：

暴力，这题最朴素的作法无非就是从l到r扫一遍，用数组记下出现的数，然后求值：

```cpp
#include<bits/stdc++.h>
using namespace std;
#define maxn 100010
bool flag[maxn];
int n, m, a[maxn], sum, ans, l, r, x, y;
int main()
{
	//freopen("count.in","r",stdin);
	//freopen("count.out","w",stdout);
	scanf("%d%d", &n, &m);
	for(int i = 1; i <= n; ++ i)
		scanf("%d", &a[i]);
	for(int i = 1; i <= m; ++ i)
	{
		scanf("%d%d%d%d", &l, &r, &x, &y);
		memset(flag, 0, sizeof(flag));
		sum = ans = 0;
		for(int j = l; j <= r; ++ j)
			if(a[j] >= x && a[j] <= y)
			{
				++ sum;
				if(flag[a[j]] == 0)
				{
					flag[a[j]] = 1;
					++ ans;
				}
			}
		printf("%d %d\n", sum, ans);
	}
	return 0;
}
```
ans即为所求；

但是这种作法的复杂度是O(n*n)的，肯定过不了；

那么就需要一些优化：

我们用两个指针不断的移动到相应的区间；
```cpp
int l = 0, r = 1;
```
然后在移动的时候，我们就不停的add，del；

如果要想右，就add；

否则，就del；
```cpp
void add(int x)
{
	if(cnt[a[x]] == 0)
		++ now;
	++ cnt[a[x]];
}
```
```cpp
void del(int x)
{
	-- cnt[a[x]];
	if(cnt[a[x]] == 0)
		-- now;
}
```

```cpp
while(l < q[i].l)
	del(l ++);
while(l > q[i].l)
	add(-- l);
while(r < q[i].r)
	add(++ r);
while(r > q[i].r)
	del(r --);

```
就是上面这样，

这就是莫队？

不，还有一个地方，

我们来假设要查询的区间为[1, 10000000]呢？

那不一样还是没有优化。

所以莫队还要一个很重要的地方，就是排序；

该如何排序？

如果按左端点排序，那么右端点就会不好表示；

如果按右端点排序，那么左端点就会不好表示；

这个时候，分块大法万岁；

把长度为n的序列，分成sqrt(n)个块；

把查询区间按照左端点所在块的序号排个序，如果左端点所在块相同，再按右端点排序。

其实，蒟蒻我也不明白这为什么会快200多ms，但它就是会；

整个程序的复杂度为O(n * sqrt(n));

代码时间：

```cpp
#include<bits/stdc++.h>
using namespace std;

#define maxn 1000010
int n, m, a[maxn], cnt[maxn], ans[maxn], bein[maxn], l = 1, r, now;

struct node
{
	int l, r, id;
}q[maxn];

bool cmp(node a, node b)
{
	return bein[a.l] == bein[b.l] ? a.r < b.r : bein[a.l] < bein[b.l];
}

void add(int x)//加入操作 （右移 
{
	if(cnt[a[x]] == 0)
		++ now;
	++ cnt[a[x]];
}

void del(int x)//删除（左移 
{
	-- cnt[a[x]];
	if(cnt[a[x]] == 0)
		-- now;
}

void print(int x)//要从后往前输出，所以来递归输出 
{
	if(x / 10)
		print(x / 10);
	//printf("%d", x % 10);
	putchar(x % 10 + '0');
	//printf("K"); 
}

int main()
{
    scanf("%d", &n);//输入 
	for(int i = 1; i <= ceil((double) n / sqrt(n)); ++ i)
		for(int j = (i - 1) * sqrt(n) + 1; j <= i * sqrt(n); ++ j)
			bein[j] = i;//这是分的块 
	for(int i = 1; i <= n; ++ i)
		scanf("%d", &a[i]);//还是输入 
	scanf("%d", &m);//继续输入 
	for(int i = 1; i <= m; ++ i)
	{
		scanf("%d%d", &q[i].l, &q[i].r);//还要输入 
		q[i].id = i;//记录下序号，cmp中要用 
	}
    sort(q + 1, q + m + 1, cmp);//排序 
    /*这种作法就不需要add和del 
    for(int i = 1; i <= m; ++i) {
        int ql = q[i].l, qr = q[i].r;
        while(l < ql) now -= !--cnt[aa[l++]];
        while(l > ql) now += !cnt[aa[--l]]++;
        while(r < qr) now += !cnt[aa[++r]]++;
        while(r > qr) now -= !--cnt[aa[r--]];
        ans[q[i].id] = now;
    }
	*/
	for(int i = 1; i <= m; ++ i)
	{
		while(l < q[i].l)//l右移 
			del(l ++);
		while(l > q[i].l)//l左移 
			add(-- l);
		while(r < q[i].r)//r右移 
			add(++ r);
		while(r > q[i].r)//r左移 
			del(r --);
		ans[q[i].id] = now;
	}
    for(int i = 1; i <= m; ++ i)
	{
		print(ans[i]);//输出 
		printf("\n");//记得换行 
	}
	return 0;
}
```
因为在本蒟蒻最开始学的时候没有懂，所以有拜读了[WAMonster](https://www.cnblogs.com/WAMonster/p/10118934.html)大佬的文章，可能在思路上会有部分相同，而且我也强力推荐这位大佬的博客，写的特别好。