# P1865 题解

首先，这个是在“数论”这个任务里的

那我们就聊聊数论。

素数（质数）的定义大家小学都学过：除了1和它本身没有其他约数的数叫素数，有其他约数的叫合数，1既不是素数，也不是合数；

~~（这个先搁置一边）~~

我们判断素数的程序大家应该都写过

```cpp
#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;//n保证是自然数 
    cin>>n;
    if(n==1)
    {
        cout<<"既不是素数，也不是合数";
        return 0; 
    }
    for(int i=2;i<=sqrt(n);i++)
    {
        if(n%i==0)
        {
            cout<<"是合数";
            return 0; 
        }
    }
    cout<<"是素数";
    return 0;
}
```
这个方法的原理就是素数的定义；

当然在这里，这样求区间素数个数显然会超时；

所以我们换个角度从判断素数，变成判断合数；

合数显然是可以分解质因数的，既然如此，也就说明，质数的倍数（倍数>1）都是合数，所以就有了埃氏筛（不懂各种筛法的同学可以看洛谷[【模板】线性筛素数](https://www.luogu.org/problemnew/show/3383 "【模板】线性筛素数")的题解）

本质上就是从2开始把它除本身的倍数全部删去，以此类推（这时你可能要问那到这个数的时候怎么判断它是不是质数，事实上，如果自然数N在N-1的时候没有把它标记掉就肯定是质数（具体证明可百度））

区间和可以用前缀和处理；

f[r]-f[l-1] (此处已修改，感谢@33028120040712wcl @Kyle_Lowry，以前太弱了~~现在也是~~)

下面是代码

```cpp
#include<bits/stdc++.h>
using namespace std;

int f[1000001];
bool vis[1000001];

void shai(int n)
{
    f[1]=0;
    vis[1]=true;
    for(int i=2;i<=n;i++)
    {
        if(vis[i]==false) //在筛里进行前缀和
        {
            f[i]=f[i-1]+1;//前缀和计算
            for(int j=i+i;j<=n;j=j+i)
            {
                vis[j]=true;//标记操作
            }
        }
        else f[i]=f[i-1];//前缀和转移
    }
}

int main()
{
    int n,m;
    scanf("%d%d",&m,&n);
    shai(n);
    for(int i=1;i<=m;i++)
    {
        int l,r;
        scanf("%d%d",&l,&r);
        if(l<1 || r>n) cout<<"Crossing the line"<<endl;//判断是否超出区间
        else 
        {
            int y=f[r]-f[l-1];//此处已经修改
            cout<<y<<endl;
        }
    }
    return 0;
}
```