# P4514 题解

# 一位树状数组区间操作的方法就是

开两个树状数组A,B，如果我们想让[1,x]中所有数+v，那么就在A中x位置+x*v，B中x位置+v。

如果我们想查询[1,y]的和，那么ans=A中[1,y]的和+B中[y+1,n]的和*x。

## 问： 那么二维的呢？
## 答： 把两个换成四个。。。
# 代码
```
#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
const int maxn=2050;
int n,m;
struct BIT
{
    int s[maxn][maxn];
    void updata(int x,int y,int val)
    {
        if(!x||!y)  return ;
        for(int i=x;i<=n;i+=i&-i)    for(int j=y;j<=m;j+=j&-j)    s[i][j]+=val;
    }
    int query(int x,int y)
    {
        int ret=0,i,j;
        for(i=x;i;i-=i&-i)  for(j=y;j;j-=j&-j)  ret+=s[i][j];
        return ret;
    }
}A,B,C,D;
char str[5];
void add(int x,int y,int val)
{
    A.updata(x,y,val*x*y),B.updata(x,y,val*x),C.updata(x,y,val*y),D.updata(x,y,val);
}
int query(int x,int y)
{
    return A.query(x,y)+y*(B.query(x,m)-B.query(x,y))+x*(C.query(n,y)-C.query(x,y))+x*y*(D.query(n,m)-D.query(x,m)-D.query(n,y)+D.query(x,y));
}
int main()
{
    scanf("%s%d%d",str,&n,&m);
    int i,a,b,c,d,e;
    while(scanf("%s%d%d%d%d",str,&a,&b,&c,&d)!=EOF)
    {
        if(str[0]=='L') scanf("%d",&e),add(a-1,b-1,e),add(a-1,d,-e),add(c,b-1,-e),add(c,d,e);
        else    printf("%d\n",query(a-1,b-1)-query(a-1,d)-query(c,b-1)+query(c,d));
    }
    return 0;
}
```