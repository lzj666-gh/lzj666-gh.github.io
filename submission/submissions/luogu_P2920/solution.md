# P2920 题解

~~其实这道题水的要命，别看它是道黄题~~ ~~（之所以这么讲，其实是因为本蒟蒻只是个小学生，黄题都非常困难）~~，  
如果这句话伤到了你，我表示抱歉(^_^)

好了，废话不多说，我们切入正题，首先，不懂得分治的可以去看[这位大佬的文章](https://www.luogu.org/blog/HOJQVFNA/qian-tan-er-fen-di-bian-jie-wen-ti)，  
这道题是让我们求最晚可以在什么时间起床，这里我们需要加入一个小小的贪心，就是结束时间短的放前面处理，至于为什么，相信你肯定能理解  
然后，我们定义三个变量，$left$ ,$right$ ,$mid$ ,其中，$left$ 表示再找这个区间的起点，而 $right$ 表示这个区间的终点，$mid$ 表示它们中间的值,像这种地方，一般只需背个模板就行了，然后，本题最最重要的地方来了 —— 判断函数，（像本蒟蒻就是在这里卡了很久）  
首先，我们可以这么判断，如果当前所在的时间加上这个任务所需要的时间，没有超过这个任务所必须结束的时间，那么，新的时间则等于原来的时间加上任务所花的时间，否则，证明这个数不合法，本题的思路就是这样，如果你还不明白，请仔细看下面的代码：  
```
#include <iostream>
#include <cstdio>
using namespace std;
struct node
{
	int start;   //起始时间 
	int comes;   //必须在什么时间结束 
};
struct node que[1000001];
int n;
bool check(int cnt)
{
	int x,y,tnt=cnt;
	for(x=1;x<=n;x++)
	{
		if(que[x].start+tnt<=que[x].comes)//如果当前的时间加上任务所需的时间小于等于结束时间，将新的时间等于旧的时间加上任务时间
			tnt=que[x].start+tnt;
		else
			return false;//否则，说明这个数不合法
	}
	return true;
}
int main()
{
	int right=1000000000,left=1,mid=(left+right)/2;
	int i,j,k,ans=0;
	scanf("%d",&n);
	for(i=1;i<=n;i++)
		scanf("%d %d",&que[i].start,&que[i].comes);//读入数据
	for(i=1;i<=n;i++)
		for(j=i+1;j<=n;j++)
			if(que[i].comes>que[j].comes)
				swap(que[i],que[j]);//结束时间短的需放在前面处理
	while(left<=right)//这个只是一个模板，本人使用的是记录答案法
	{
		mid=(left+right+1)/2;//防止死循环
		if(check(mid))
		{
			ans=mid;    //如果这个数合法，那么在它的右边寻找更优解
			left=mid+1;
		}
		else
			right=mid-1;//否则，就在它的左边寻找解
	}
	if(ans!=0)
		cout<<ans;
	else
		cout<<-1;
	return 0;//圆满结束
}
```