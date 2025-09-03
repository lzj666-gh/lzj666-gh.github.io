# P2392 题解

### 贪心题:既然是算较短的时间，如果左脑所用时间少就加在左脑，如果右脑所用时间少就加在右脑


------------

```c
#include<bits/stdc++.h>
using namespace std;
int a[5],i,j,sum1,sum2,t,homework;
int main(){
    for(i=1;i<=4;i++)
        cin>>a[i];//输入
    for(i=1;i<=4;i++){
    sum1=sum2=0;//两边脑子时间清零
    for(j=1;j<=a[i];j++)
        {cin>>homework;
        if(sum1<=sum2) sum1+=homework;
        else sum2+=homework;}//哪边时间短就加在哪边
        t+=max(sum1,sum2);//取较长时间累加
    }cout<<t;//输出
    return 0;
}
```
### 满怀期待的提交后，结果有点震惊 [结果](https://www.luogu.org/recordnew/show/17877263)
### 果然，贪心不是正解
### 后来思考了一下，便感觉是dp，对于一道题只有两个状态，一是加到左脑，二是加到右脑，所以是01背包
### 这里还可以用另一个思想，将一边的脑子加到最接近一半则另一边脑子时间就是正解
```c
#include<bits/stdc++.h>
using namespace std;
int a[5],i,j,k,sum,t,homework[21],dp[2501];
int main(){
	for(i=1;i<=4;i++)
		cin>>a[i];
	for(i=1;i<=4;i++){
		sum=0;	
		for(j=1;j<=a[i];j++)
			{cin>>homework[j];//输入
			sum+=homework[j];}//总时间累加
		for(j=1;j<=a[i];j++)
			for(k=sum/2;k>=homework[j];k--)//只要是总和的一半
				dp[k]=max(dp[k],dp[k-homework[j]]+homework[j]);//01背包
		t+=sum-dp[sum/2];//累加为另一个脑子
		for(j=1;j<=sum/2;j++)
		dp[j]=0;//清零
	}
	cout<<t;//输出
	return 0;
}
```
