# P2668 题解

这道题的核心是 ~~暴力模拟~~ ! !

这是搜索的顺序

![](https://cdn.luogu.com.cn/upload/pic/32162.png)

特别注意：**大小王**牌值不同，**不能算一对 ! ! ! ! ! ! ! ! **   只有做**火箭**才能一起出

具体内容看代码

代码较长但是很容易懂，注释很多

```
#include<bits/stdc++.h>
using namespace std;
int T,n,ans,sum[25];
void dfs(int x)//x为出牌次数
{
	if (x>=ans) return;
	//顺子
	int k=0;//单顺子
	for (int i=3;i<=14;i++)//注意2和大小王不能考虑
	{
		if(sum[i]==0) k=0;//顺子断了
		else
		{
			k++;//顺子长度增加
			if(k>=5)//单顺子达到五张
			{
				for(int j=i;j>=i-k+1;j--) sum[j]--;//出牌
				dfs(x+1);//继续搜
				for(int j=i;j>=i-k+1;j--) sum[j]++;//回溯
			}
		}
	}
	k=0;//双顺子
	for(int i=3;i<=14;i++)
	{
		if(sum[i]<=1) k=0;
		else 
		{
			k++;
			if(k>=3)//双顺子达到三组
			{
				for(int j=i;j>=i-k+1;j--) sum[j]-=2;//出牌
				dfs(x+1);
				for(int j=i;j>=i-k+1;j--) sum[j]+=2;//回溯
			}
		}
	}
	k=0;//三顺子    //以下同理
	for(int i=3;i<=14;i++)
	{
		if(sum[i]<=2) k=0;
		else 
		{
			k++;
			if(k>=2)//三顺子达到两组
			{
				for(int j=i;j>=i-k+1;j--) sum[j]-=3;
				dfs(x+1);
				for(int j=i;j>=i-k+1;j--) sum[j]+=3;
			}
		}
	}
	//带牌
	for(int i=2;i<=14;i++)//枚举有3张或4张的牌（这样才能带牌）
	{
		if(sum[i]<=3)
		{
			if(sum[i]<=2) continue;//三张以下（不含三张）不能带牌
			sum[i]-=3;//出掉用来带别人的牌
			for(int j=2;j<=15;j++)//带单张
			{
				if(sum[j]<=0||j==i) continue;//没有牌怎么带？？
				sum[j]--;//出掉被带的单张
				dfs(x+1);
				sum[j]++;//回溯
			}
			for(int j=2;j<=14;j++)//带一对
			{
				if(sum[j]<=1||j==i) continue;//没有一对怎么带？
				sum[j]-=2;//出掉被带的一对
				dfs(x+1);
				sum[j]+=2;//回溯
			}
			sum[i]+=3;//回溯
		} 
		else//大于3可以4带别的也可以3带别的
		{
			sum[i]-=3;//先用3张带别的
			for(int j=2;j<=15;j++) //带单张  //以下原理同上
			{
				if(sum[j]<=0||j==i) continue;
				sum[j]--;
				dfs(x+1);
				sum[j]++;
			}
			for(int j=2;j<=14;j++) //带一对
			{
				if(sum[j]<=1||j==i) continue;
				sum[j]-=2;
				dfs(x+1);
				sum[j]+=2;
			}
			sum[i]+=3;
			
			sum[i]-=4; //再用4张带别的 
			for(int j=2;j<=15;j++) //带2个单张
            {
				if(sum[j]<=0||j==i) continue;//自己不能带自己喽
				sum[j]--;//出被带的第一张单张牌
				for (int k=2;k<=15;k++)//找第二张单张
				{
					if(sum[k]<=0||j==k) continue;
					sum[k]--;//出被带的第二张单张牌
					dfs(x+1);
					sum[k]++;//回溯
				}
				sum[j]++;//回溯
			}
			for(int j=2;j<=14;j++)//带2个对儿
			{
				if(sum[j]<=1||j==i) continue;
				sum[j]-=2;//出被带的第一对牌
				for(int k=2;k<=14;k++) 
				{
					if(sum[k]<=1||j==k) continue;
					sum[k]-=2;//出被带的第二对牌
					dfs(x+1);
					sum[k]+=2;//回溯
				}
				sum[j]+=2;//回溯
			}
			sum[i]+=4;//回溯
		}
	}
	//把剩下的牌出完
	for(int i=2;i<=15;i++) if(sum[i]) x++;
	ans=min(ans,x);
}
int main() 
{
	scanf("%d%d",&T,&n);
	while(T--)
	{
		ans=0x7fffffff;//搞大一点
		int x,y;
		memset(sum,0,sizeof sum);//多次询问，记得清零
		for(int i=1;i<=n;i++)
		{
			scanf("%d%d",&x,&y);
			if (x==0) sum[15]++;//把两张王存在一起（但是带牌的时候注意不要做对儿）
			else if(x==1) sum[14]++;//由于A的牌值大所以往后放
		    else sum[x]++;//其他牌存在相应位置
		}
		dfs(0);//开始暴搜
		printf("%d\n",ans);
	}
}
```