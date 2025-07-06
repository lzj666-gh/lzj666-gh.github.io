# P1594 题解

//写写这篇题解复习动态规划

**【算法分析】**

乍一看这道题，以为可以用模拟来解，像这样：
![](https://cdn.luogu.com.cn/upload/pic/65103.png)

带入数据一算就知道：我们错了！

仔细一看题目要求的是最短时间，这就要求我们**遍历所有的可能情况**。用搜索显然较繁，于是 ~~没学过其他算法的蒟蒻~~ 我们想到了**动态规划**。

**【动归方程】**

按照动态规划的思想方法，我们：

（1）**设 f[i] 为前i辆车通过桥的最短时间，设 t[i][j] 为第i-第j辆车（租车的车队）通过所需时间；**

（2）分析方程：
![](https://cdn.luogu.com.cn/upload/pic/65113.png)

综合起来，我们就得到了**方程**：
![](https://cdn.luogu.com.cn/upload/pic/65114.png)

Perfect! 但是也不要忘记了**条件**：
![](https://cdn.luogu.com.cn/upload/pic/65116.png)

（3）其实我们也可以这样理解，**对于每一辆车i，j从第i-1辆车开始倒推，看看总重是否小于最大载重量；**是则能组成车队，否则不能，且前面的j-1辆车不能与i组成车队；

![](https://cdn.luogu.com.cn/upload/pic/65119.png)

**【细节处理】**

（1）预处理重量

定义W[i]为前i辆车的总重
**（即前缀和，是处理这类问题非常好的方法，可以降低时间复杂度）**
![](https://cdn.luogu.com.cn/upload/pic/65208.png)

 **需要知道第j辆车到第i辆车的总重时，用W[i]-W[j-1]就可以了；**

（2）预处理时间

**（值得一提的是本题解直接将时间计算出来，转为分钟，方便之后程序编写）**

方法是：
定义Sb为桥的全长；v[i]为第i辆车的速度；T[i]:第i辆车通过桥所需时间；t[i][j]:第i辆车到第j辆车组成的车队通过桥所需的时间；

![](https://cdn.luogu.com.cn/upload/pic/65210.png)

 **（3）w数组、v数组和W数组一定要开long long，否则两个较大的int相加会炸掉！**

~~（我在这里被坑掉两个点qwq）~~

**【代码】**
 ```cpp
#include<iostream>
#include<cstdio>
using namespace std;
long long Wb,Sb,n,w[1000],v[1000],W[1000];double T[1000],t[1000][1000],f[1000];
/*Wb:the weigh of the bridge;
  Sb:the distance of the bridge;
  w[i]:the weigh of car i; 
  v[i]:the speed of car i;
  T[i]:the time for car i to go across the bridge; (minutes)
  W[i][j]:the sum of w[i],w[i+1],...,w[j];
  t[i][j]:the time for car i,car i+1,...,car j to go across the bridge; (minutes)
  f[i]:we must spend f[i] to let car 1,car 2,...,car i to go;
  一定要开long long，否则会炸！ 
*/

int main()
{
	cin>>Wb>>Sb>>n;
	for(int i=1;i<=n;i++)
	{
		cin>>w[i]>>v[i];   
		T[i]=(double)Sb/v[i]*60;
		t[i][i]=T[i];
	}
	for(int i=1;i<=n-1;i++) 
	{
		for(int j=i+1;j<=n;j++)
		{
			t[i][j]=max(t[i][j-1],T[j]);
		}
	}
	for(int i=1;i<=n;i++)
	{
		W[i]=W[i-1]+w[i];
	}	
	for(int i=1;i<=n;i++)
    {
        f[i]=T[i]+f[i-1];  //前面i-1辆车所花的时间，加上第i辆车所花时间，就是前i辆车所花时间 
        for(int j=i-1;j>=1;j--)   //倒回去查，看看能不能组成一个从j到i的车队 
        {
        	if (W[i]-W[j-1]<=Wb) 
			{
				f[i]=min(f[i],f[j-1]+t[j][i]);  //cout<<f[i]<<" "; //能组成车队，比较时间 
			}
            else break;  //不能组成车队 
			
        }
    }
    printf("%0.1lf",f[n]); 
	return 0;
} 
```
PS：这是本人的第二篇题解（第一篇没过审核），求资磁！