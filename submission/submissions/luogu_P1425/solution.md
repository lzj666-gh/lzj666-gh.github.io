# P1425 题解

```cpp
#include <iostream>
using namespace std;
int main()
{
    int a,b,c,d;
    cin>>a>>b>>c>>d;
    int x=c-a,y=d-b;
    if(y<0){x--;y+=60;}
    cout<<x<<" "<<y;
    return 0;
}
```
这道题确实简单，但是我开始的时候居然把x、y的初始化弄反了。。。
额啊啊啊啊……

好吧现在发思路。

首先肯定硬算小时数和分钟数，即c-a和d-b。

但是d<b怎么办？WA掉？

no no no，我当然会处理。

如果d<b（y减出来是个负数），那么x一定大于0（肯定的啦~），所以可以向小时借60分钟，把y变成正数。

于是就有了以上代码。

啊，好辛苦【手动哭泣】
