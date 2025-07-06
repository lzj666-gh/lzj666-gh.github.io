# P1551 题解

本 _**蒟蒻**_ 第一篇题解

所以多多包容啦thx

~~说实话我才A了二十一道题~~

~~没错但我还是不要脸的上来发题解~~

好了cd结束   下面正题
```cpp
#include<bits/stdc++.h>
using namespace std;
int n,m,q,f[10010],c,d,a,b;
int fd(int x)//找出x家的大佬 也就是二叉树的祖先节点
{
	if(f[x]==x)//x是x的爸爸，简单的来说就是x没爸爸了
    
    //他是家里最大的大佬，所以返回的x就是我们所求的祖先节点
	return x;
	else 
	return  f[x]=fd(f[x]);//x不是他自己的爸爸，所以他上面还
    //有爸爸，我们的目标是祖先节点，所以我们此时要做的是问他
    //爸爸的爸爸是谁，即再使用一次fd（find）函数【其实就是一个递归过程
}
void hb(int x,int y)
{
	f[fd(y)]=fd(x);//合并x子集和y子集，直接把x子集的祖先节
    //点与y子集的祖先节点连接起来，通俗点来说就是把x的最大祖
    //先变成y子集最大祖先的爸爸
	return ;
}
int main()
{
	scanf("%d%d%d",&n,&m,&q);
	for(int i=1;i<=n;i++)
	f[i]=i;
	for(int i=1;i<=m;i++)
	{
	     scanf("%d%d",&c,&d);
	     hb(c,d);
	}
	for(int i=1;i<=q;i++)
	{
		scanf("%d%d",&a,&b);
		if(fd(a)==fd(b))//如果a所在子集的大佬[前面已经解释过了]和b所在子集的大佬一样，即可知a和b在同一个集合
		printf("Yes\n");
		else
		printf("No\n");
	}
	return 0;
}
```
很简单的一个并查集

我的程序应该还算简洁

好了没了，我可能说的比较啰嗦

需要的朋友将就着看下咯

多多指教

本蒟蒻告辞

谢谢啦（爱你们略略略