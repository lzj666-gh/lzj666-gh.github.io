# P2851 题解

题意中的金额我们不妨抽象为线段长度  
所以题意可以简化成：怎样拼凑成两段线段，且它们的长度之差等于T（图中数字为硬币编号）  
![](https://i.loli.net/2018/10/19/5bc95326d4c5b.png)  

你要怎么去拼凑线段，这就有些背包的感觉。所以我们可以分别从John和店主不同的角度来考虑最优解  

因为John的硬币数是有限的，所以可以视为多重背包，求达到一定钱数所需的最少的硬币数量;店长的硬币数是无限的，所以可以视为完全背包，也是求同种方案最少的硬币数量，再在最后枚举每种付钱和找钱的方案硬币数之和，求个min即可得出答案    

但是问题是，我们应该一直找到多少钱的方案才能保证找到合法的最优解呢？我认为这是这道题最关键的部分，以下为证明（然而其他的题解都没有说清楚）     

其余几位大佬的题解中说到，最大应一直找到$t+V_{max}^2$。这是先从店主的角度考虑的  

设货币面值为$V_{1}\le V_{2}\le \dots V_{n}$，$(V_{max}=V_{n})$那么当老板需要找$V_{max}^2$的钱时，至少需要$V_{max}$枚硬币。设一个前缀和数组为$S_{0}\ S_{1}\ S_{2}\dots S_{n}\ (S_{0}=0)$，其中共有$V_{max}+1$个元素。根据抽屉原理，至少有两个前缀和与$V_{max}$同余，则它们的差$=x\times V_{max}(x\text{为正整数且}x\ge 1)$。显然当$V_{max}$的数量足够时，将这一部分替换成$x$个面值为$V_{max}$是最优的（不要纠结真正采用的方案）。对于$V_{n-1}$，同理。  
所以在$V_{max}^2$的范围内一定可以找出最优方案，对于更大的$t+V_{max}^2$也一定可以   

顺手贴一下代码，同时感谢题解区的大佬们 
```cpp
#include <cstdio>
#include <cstring>
const int maxT=10000+10;
const int maxn=100+5;
const int maxv=120;
int f[maxT+maxv*maxv],g[maxT+maxv*maxv];//f[i]、g[i]分别表示John和店长付i元钱最少需要用的硬币 
int v[maxn],c[maxn];//如题意所示 
inline int max(int x,int y) {return x>y?x:y;}
inline int min(int x,int y) {return x<y?x:y;}
int main()
{
    int n,t;
    scanf("%d%d",&n,&t);
    for (int i=1;i<=n;i++)
        scanf("%d",&v[i]);
    int sum=0,mx=0;
    for (int i=1;i<=n;i++)
    {
        scanf("%d",&c[i]);
        sum+=c[i]*v[i];
        mx=max(mx, v[i]*v[i]);
    }
    if (sum<t)//买不起，退了 
    {
        printf("-1\n");
        return 0;
    }
    memset(g, 0x3f, sizeof(g));
    memset(f, 0x3f, sizeof(f));
    g[0]=0;
    f[0]=0;
    for (int i=1;i<=n;i++)
        for (int j=v[i];j<=mx;j++)//Rob找j元钱所用的最小钱数 
            g[j]=min(g[j], g[j-v[i]]+1);
    //实际上应该是g[i][j]=min(g[i-1][j], g[i][j-v[i]+1])
    //g[i][j]表示考虑到第i个物品支付j元的最少硬币数 
    //但是因为第一维存储的信息用不到
    //且更新前g[i][j]记录的就是g[i-1][j]的信息 
    //所以可以只用一维 
    for (int i=1;i<=n;i++)
    { 
        for (int j=1;j<=c[i];j<<=1)
        {
            for (int k=t+mx;k>=j*v[i];k--)//倒过来更新（实际上是拆分成01背包的形式） 
                f[k]=min(f[k], f[k-j*v[i]]+j);
            c[i]-=j;//相当于用拆分的物品进行了一次更新，要从数量中减去 
        }
        if (c[i])//还有剩余的没更新 
            for (int k=t+mx;k>=c[i]*v[i];k--)
                f[k]=min(f[k], f[k-c[i]*v[i]]+c[i]);
    }
    int ans=0x3f3f3f3f;
    for (int i=t;i<=t+mx;i++)
        ans=min(ans, f[i]+g[i-t]);
    printf("%d\n",ans==0x3f3f3f3f?-1:ans);
    return 0;
}
```