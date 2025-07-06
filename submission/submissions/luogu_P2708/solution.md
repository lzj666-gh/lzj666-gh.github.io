# P2708 题解

一道水题

对于读入的长度为m的字符串，只需要从第二个开始判断，如果和前面的一样（s[i]==s[i-1]）就删去，如：

0111000111

变成：

0101
如果最后一个是1  答案就是删取后的字符串长度；

如果最后一个是0  答案就加1 （相当于把全是背面朝上的变成全是正面朝上的）

```cpp
#include<bits/stdc++.h>
using namespace std;
int main()
{
            int i,m,k;
       string s;
       cin>>s;
       m=s.size();k=m-1;
       for(i=1;i<m;++i)
         if(s[i]==s[i-1])k--;         //删除语句
          if(s[m-1]=='0')k++;
       cout<<k;
       return 0;
}
```