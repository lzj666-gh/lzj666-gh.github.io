# P1649 题解

```cpp
/*
此题数据范围是n<=100,本来正解是bfs或者最短路径spfa
我先想用暴搜试一下看能拿多少分
没想到居然能AC，但是我后来调了一下，发现这是一个有点巧的事情
如果你把方向数组的顺序改一下，也许就只能拿90，不管怎么说，我还是侥幸过了
思路还是很好理解。
下面上代码 ： 
*/ 
#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
int n,x0,y0,xn,yn,ans=0x7fffffff/2,bj;char l;
int a[105][105];
int dx[4]={1,0,-1,0};
int dy[4]={0,-1,0,1};
//右 下 左  上 
void Read()
{
	scanf("%d",&n);
	for(int i=1;i<=n;i++)
	    for(int j=1;j<=n;j++)
	    {
	    	cin>>l;//读入字符的时候因为题目说了有空格，所以用cin而没用scanf 
	    	if(l=='A')x0=i,y0=j,a[i][j]=-1;//标记不能重复走 
	    	if(l=='B')xn=i,yn=j,a[i][j]=0;
	    	if(l=='x')a[i][j]=-1;
    	}
} 
void dfs(int x,int y,int t,int k)
//x坐标+y坐标+t为上次的方向+k为当前转角次数 
{
	if(k>=ans)return ;
	//剪枝！！！ ：不管你搜到没有，因为本题是求的最少次数，所以如果发现当前的k都大于ans，那么直接return 
	if(x==xn&&y==yn){ans=min(ans,k);bj=1;return ;}//取ans最小并标记找到 
	for(int i=0;i<4;i++)
	{
		int nx=dx[i]+x;int ny=dy[i]+y;//四个方向的走后点的新坐标 
		if(nx<=0||nx>n||ny<=0||ny>n)continue;//判界 
		if(!a[nx][ny])//不走回路 
		{
			a[nx][ny]=-1;//标记不能走 
		    int f=0;
			if(i!=t)f=1;if(t==-1)f=0;//f判断方向，如果当前方向i与上一次的方向t不同，说明要转向，记f=1 
	    	dfs(nx,ny,i,k+f);
	    	//下一个位置的坐标+方向+次数累加 
	    	a[nx][ny]=0;//回溯 
		}
	}
}
int main()
{
    Read();
    dfs(x0,y0,-1,0);//下面是暴力dfs 
    if(bj)printf("%d",ans);
    else printf("-1");
    return 0;
} 
```