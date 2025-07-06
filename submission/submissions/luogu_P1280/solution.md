# P1280 题解

唔~普及组水题，比较适合DP练习


这题显然是一个线性动规，那么肯定是第一时间想到设f[i]:1~i的最大空闲时间，但是，想了一下之后发现，第i时刻的最大空闲时间是和后面i+选择任务的持续时间的时刻有关系的，那么，正着找肯定是不行的，我们来试一下倒着搜,即设f[i]表示i~n的最大空闲时间，经尝试，发现是完全可行的，可以列出动态转移方程如下

**（本时刻无任务）f[i]=f[i+1]+1;//继承上一个时刻的最大空闲时间后+1**

**（本时刻有任务）f[i]=max(f[i],f[i+a[sum])//a[sum]表示在这个时刻的任务的持续时间，找出选择哪一个本时刻任务使空闲时间最大化**

那么既然是倒着搜，从后往前的任务对应的开始时间自然也要反过来，从大到小排序（同时也是为了把相同开始时间的任务放到一起）,当然在进行状态刷新的时候别忘了拿sum不断计一下已经到哪一个任务了


那么。。喜闻乐见的，上代码。。。。


```cpp
#include<iostream>  
#include<algorithm>  
using namespace std;  
long int n,k,sum[10001],num=1,f[10001];  
struct ren//结构体，一起排序 ，从大到小   
{  
    long int ks,js;  
};  
ren z[10001];  
int cmp(ren a,ren b)  
{  
    return a.ks>b.ks;  
}  
int main()  
{  
    long int i,j;   
    cin>>n>>k;  
    for(i=1;i<=k;i++)  
    {  
    cin>>z[i].ks>>z[i].js;    
    sum[z[i].ks]++;  
    }  
    sort(z+1,z+k+1,cmp);  
    for(i=n;i>=1;i--)//倒着搜   
    {  
        if(sum[i]==0)  
        f[i]=f[i+1]+1;  
        else for(j=1;j<=sum[i];j++)  
        {  
            if(f[i+z[num].js]>f[i])  
            f[i]=f[i+z[num].js];  
            num++;//当前已扫过的任务数   
        }  
    }  
    cout<<f[1]<<endl;  
}  

```