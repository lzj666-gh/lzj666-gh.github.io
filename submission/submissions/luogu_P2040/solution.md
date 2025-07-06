# P2040 题解

~~发现自己跑的好优越,只是$2^{n}$级的复杂度~~

**其实这道题目你会发现其实只需要关心是否会与这盏灯操作一次就够了!**

为什么? 其实如果是操作 2 次, 4 次,或者 6 次......其实都是对答案是一样的---**根本没有操作!** 而 1 ,  3 , 5 ,7 ....也就等同于操作一次!

如 5 号灯操作了5下(原来是 **开**的) 就是:关,开,关,开,关...

**结果还是关**

那么...我们对于这 9 个格子,只要二进制操作一番就好了,比如:


$\mathcal{100111101}$


\*就是对于1,4,5,6,7,9这些灯盏操作,那么我们只要记录是否能够完成就好了!\*

~~有疑问的欢迎提问,但尽量别举报...~~


```cpp
#include <bits/stdc++.h>
#define P pair<int,int>
#define sc scanf
#define pi printf
#define N 1500
#define M 300005
#define INF 0x3f3f3f3f
 using namespace std;
inline int getmax(int x,int y){return (x>y)?x:y;}
inline int getmin(int x,int y){return (x>y)?y:x;}
int n,ans=INF,tot,a[13],s[13],how[13];
inline void get(int n)
{
    int cnt=0;
    memset(s,0,sizeof s);
    while(n)
    {
        s[cnt++]=n%2;
        n/=2;
    }
}
int main(int argc, char const *argv[])
{
    for(int i=0;i<9;i++) scanf("%d",a+i);
    for(int used=0;used<(1<<9);used++) // 暴力枚举二进制
    {
        get(used); memset(how,0,sizeof how);
        for(int i=0;i<9;i++) //算i号的灯盏被操作了多少次!
            if(s[i]) //9 个格子的打暴力,其实可以变得简洁一些!
            {
                if(!i) how[0]++,how[1]++,how[3]++;
                else if(i==1) how[0]++,how[1]++,how[2]++,how[4]++;
                else if(i==2) how[1]++,how[2]++,how[5]++;
                else if(i==3) how[0]++,how[6]++,how[4]++,how[3]++;
                else if(i==4) how[4]++,how[1]++,how[3]++,how[5]++,how[7]++;
                else if(i==5) how[4]++,how[5]++,how[2]++,how[8]++;
                else if(i==6) how[6]++,how[3]++,how[7]++;
                else if(i==7) how[7]++,how[6]++,how[8]++,how[4]++;
                else if(i==8) how[5]++,how[7]++,how[8]++;
            }
        bool flag=true;
        for(int i=0;i<9;i++)  // 计算是否可行!
            if(how[i]%2==1 && a[i]) flag=false;
            else if(how[i]%2==0 && !a[i]) flag=false;
        if(flag)
        {
            tot=0;
            for(int i=0;i<9;i++) if(s[i]) tot++;
            ans=getmin(tot,ans);
        } 
    }
  //  printf("%d\n",ans);
}

```
