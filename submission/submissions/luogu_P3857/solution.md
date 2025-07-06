# P3857 题解

# Solution
线性基板子题

对于每一个开关,我们可以看成一个0/1串,初始是一个全部为0的串,要求经过这些开关的操作后,出现的不同的0/1串的个数

终点就是不同这两个字,这就决定了我们可以使用线性基来解决这道题

首先了解一下线性基的性质对于两个数字a,b,可以有0,a,b,a^b四种情况
把b换成a^b依然如此

即**线性基内的元素是不重复的**

那么我们就可以把这些0/1串换成10进制后丢到线性基里面去,然后统计线性基内元素个数
在这里稍微讲一下线性基的原理

线性基可以说是一种容器,并且对于每一位都有一个数,这个数一定保证自己所在的这一位为1
我们开一个数组记录线性基,对于每一个数x我们都对它的每一位从高到低进行一遍扫描,与线性基中这一位去匹配
如果线性基中这一位为空,我们就把x加入这一位中,然后就不用做下去了
如果线性基中这一位有值,我们就用x去xor这个数,表示消去这一位,知道出现第一种情况
这种方法就保证了线性基内元素的**不重复性**
除此之外,线性基还有三条最重要的性质
>1.  线性基能相互异或得到原集合的所有相互异或得到的值
>2.  线性基是满足性质1的最小的集合
>3.  线性基没有异或和为0的子集

对于第1,2条性质,不需要太多解释,在这里主要证明一下第三条性质
>证明:假设有$a_1\bigoplus a_2\bigoplus ... \bigoplus a_n=0$,那么$a_1$一定可以由$a_2\bigoplus ... \bigoplus a_n$表示,那么我们把$a1$从线性基中删除依然可以异或除原来可以异或的元素,并且比原来的元素个数还要少,这样原来的线性基就与第二条性质最小集合相违背,所以假设不成立

下面是线性基构造代码
```cpp
void init (lol box) {
	for(int i=50;i>=0;i--) {
		if(!(box>>i&1)) continue; 
		if(!arr[i]) {++cnt,arr[i]=box;break;}
		else box^=arr[i]; 
	} 
}
```
我们知道,线性基内的元素都是由外界元素异或出来的,那么对于线性基内每个元素,我们都有选/不选两种情况,所以$Ans=1<<cnt$

欢迎踩博客[real_l](https://www.cnblogs.com/real-l/p/9639498.html)
# Code
```cpp
#include<bits/stdc++.h>
#define lol long long
using namespace std;
const int N=51,mod=2008;
int cnt;
lol arr[N];
void init (lol box) {
    for(int i=50;i>=0;i--) {
        if(!(box>>i&1)) continue; 
        if(!arr[i]) {++cnt,arr[i]=box;break;}
        else box^=arr[i];
    }
}
int main()
{
    int n,m; scanf("%d%d",&n,&m);
    for(int i=1;i<=m;i++) {
        char s[N]; scanf("%s",s);
        int len=strlen(s); lol x=0;
        for(int i=0;i<len;i++) x+=(1ll<<(n-i))*(s[i]=='O');
        init(x);
    }
    printf("%lld\n",(1ll<<cnt)%mod);
    return 0;
}
```