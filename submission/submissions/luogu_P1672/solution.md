# P1672 题解

# [USACO05FEB] Feed Accounting S题解


1、题意描述
------------
依照[题面](https://www.luogu.com.cn/problem/P1672)：已知今日日期 $D$ 和最近一次饲料运到至今所消耗的饲料 $F2\sim F1$。有 $C$ 头牛，每头牛每天都吃掉恰好 $1$ 千克饲料，对于每头牛，有一个开始日期 $ate$ 和一个结束日期 $Left$，求上一船饲料运到的时间。


2、思路
----
此题正解是差分，但我却阴差阳错想到了**二分答案**。此题的二分答案的思路是：初始化左端点 $l=0$，右端点 $r=d$ （今天日期），然后开始二分答案 $mid$。对于每次二分到的 $mid$，记录以它为**上一船饲料运到的时间**所消耗的饲料，然后判断其是否与 $F1-F2$ 相等，最后记录答案并输出即可。此算法复杂度为 $O(n \log n)$。

**如有解释不当之处，请辅以代码理解！**

3、贴代码：
----
``` cpp
#include<bits/stdc++.h>
using namespace std;
int c,f1,f2,d,ate[110],Left[110],ans;
bool check(int x){//检查此答案是否合法
	int jl=0;
	for(int i=1;i<=c;i++){
		if(ate[i]<=x){
			if(Left[i]>=x&&Left[i]<=d)
				jl+=Left[i]-x+1;
			else if(Left[i]>d)
				jl+=d-x+1;	
		}
		else{
			if(ate[i]<=d){
				if(Left[i]>=d)
					jl+=d-ate[i]+1;
				else
					jl+=Left[i]-ate[i]+1;	
			}
		}			
	}
	return jl>=f1-f2;
}
int main()
{
    ios::sync_with_stdio(NULL);//快读
    cin.tie(NULL);
    cout.tie(NULL);
    cin>>c>>f1>>f2>>d;
    for(int i=1;i<=c;i++)
    	cin>>ate[i]>>Left[i];//ate表示此牛来的日期，Left表示离开日期
    int l=1,r=d,mid;
    while(l<=r){//二分答案
    	mid=(l+r)/2;
    	if(check(mid)){//如果此答案满足，则记录下来
    		ans=mid;
    		l=mid+1;
	}
	else
		r=mid-1;
	} 
	cout<<ans;
	return 0;
}
```
[AC记录](https://www.luogu.com.cn/record/114834648)