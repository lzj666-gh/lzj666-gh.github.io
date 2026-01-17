# P3572 题解

### 题目大意
鸟要飞过树林，每次只能飞一段，长度有限制，停靠在树上

如果这棵树比刚才的矮，无论中间有多高的屏障，不用耗费体力，否则耗费体力$1$

问:最开始在树$1$，飞到树$n$，需要多少体力
### 解题思路
观察数据范围，明显是要$O(qn)$的算法

首先会每次询问分别处理，不难得到$dp$的状态转移方程

$$F_i=min(a_j>ai?f_j:f_j+1)$$

$j$在可以调到的距离内

这个算法是$O(qn^2)$的，肯定会$TLE$，考虑优化

我们可以发现每次要转移的区间是**连续且单调的**

因此可以使用单调队列优化

这个优化要考虑$2$个因素（满足前面的前提下再考虑后面的）

1. $F_i$单调不下降

2. $a_i$单调上升

- 还要记得一句话：**如果一个选手比你小，还比你强，你就可以退役了**，这句话很多单调队列都用得上

### 代码
```cpp
#include <cstdio>
int n,m,x,head,tail,a[1000001],q[1000001],f[1000001];
int read(){
    char ch=getchar();int res=0,w=1;
    while(ch<'0'||ch>'9') {if(ch=='-') w=-1;ch=getchar();}
    while(ch>='0'&&ch<='9') {res=res*10+ch-'0';ch=getchar();}
    return res*w;
}
int main(){
	n=read();
	for(register int i=1;i<=n;i++) a[i]=read();
	m=read();
	while(m--)
	{
		x=read();head=tail=1;q[tail]=1;
		for(register int i=2;i<=n;i++)
		{
			while(head<=tail&&i-q[head]>x) head++;
			if(a[q[head]]>a[i]) f[i]=f[q[head]];
			else f[i]=f[q[head]]+1;
			while(head<=tail&&(f[q[tail]]>f[i]||(f[q[tail]]==f[i]&&a[q[tail]]<=a[i]))) tail--;
			q[++tail]=i;
		}
		printf("%d\n",f[n]);
	}
    return 0;
}
```
