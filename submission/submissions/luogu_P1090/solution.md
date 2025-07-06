# P1090 题解

# O(n)算法
据说是离散化算法
就是先把原本的从小到大排序排好。然后用两个队列，一个是存储原本的，另一个是存储合成的（由于原本的是从小到大所有新开的也是从小到大）。然后在两个队列的头取最小的，执行两次然后把这两个合并加入第二个队列中。
然后由于输入：
$(1≤ai≤20000)$，所以用桶排序就可以$O(n)$时间复杂度

代码比较丑：
```cpp
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
int k,x,num,n1,n2,a1[30001],a2[30001],t[20001],w,sum;
int main()
{
	scanf("%d",&num);
	memset(a1,127/3,sizeof(a1));
	memset(a2,127/3,sizeof(a2));
	for (int i=1;i<=num;i++)
	{
		scanf("%d",&x);
		t[x]++;//桶
	}
	for (int i=1;i<=20000;i++)
	{
		while (t[i])//通排序
		{
			t[i]--;
			a1[++n1]=i;
		}
	}
	int i=1,j=1;
	k=1;
	while (k<num)
	{
		if (a1[i]<a2[j])//取最小值
		{
			w=a1[i];
			i++;
		}
		else
		{
			w=a2[j];
			j++;
		}
		if (a1[i]<a2[j])//取第二次
		{
			w+=a1[i];
			i++;
		}
		else
		{
			w+=a2[j];
			j++;
		}
		a2[++n2]=w;//加入第二个队列
		k++;//计算合并次数
		sum+=w;//计算价值
	}
	printf("%d",sum);
}
```

其实用循环队列会少一些内存~~不过我懒~~