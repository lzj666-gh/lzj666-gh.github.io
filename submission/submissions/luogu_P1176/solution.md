# P1176 题解

~~路过请看看啊，点个赞~~

这道题其实非常简单，跟2002年【NOIP普及组】过河卒基本思路一样，用递推的思想，把不能走的地方标记一下。
规律我就不推了直接看吧
```c
x[i][j]=x[i][j-1]+x[i-1][j];//应该看得懂
```
首先就是：定数组
```c
unsigned long long x[2000][2000];
bool y[2000][2000];//开得比n最大值大一些
```
输入并且赋初始值
```c
int n,m,a,b;
	cin>>n>>m;
	x[1][1]=1;
```
先把方格全标成“可以走”，不然标记"不可走"时会很麻烦
```c
for(int i=1;i<=n;i++)
	for(int j=1;j<=n;j++)
	{
		y[i][j]=true;
	}
```
输入坐标并标记“不可走”
```c
for(int i=1;i<=m;i++)
	{
		cin>>a>>b;
		y[a][b]=false;
	}
```
开始递推
```c
for(int i=1;i<=n;i++)
	for(int j=1;j<=n;j++)
	{
		if(y[i][j]==false||(i==1&&j==1))
		continue;//第一个格子和“不可走”格子跳过
		else if(i==1&&y[i][j]==true)x[i][j]=x[i][j-1]%100003;//边界情况，注意模100003
		else if(j==1&&y[i][j]==true)x[i][j]=x[i-1][j]%100003;//同上
		else if(y[i][j]==true)x[i][j]=(x[i-1][j]%100003+x[i][j-1]%100003)%100003;//规律应用
	}
```
输出
```c
cout<<x[n][n];
```
好啦，本片题解就到此啦，各位大佬不喜轻喷。

具体代码我不会发的，把上面的拼接在一起加头文件就可以了。