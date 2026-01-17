# P5015 题解

先让我们看看这句话~


**输入格式：**  
输入文件只有一行，一个字符串$s$  
**【数据规模与约定】**  
规定 $|s|$ 表示字符串 $s$ 的长度（即字符串中的字符和空格数）。  
对于 100% 的数据，$1 ≤ |s| ≤ 5$，输入可能包含大、小写英文字母、数字字符、空格和行末换行符。

$1 ≤ |s| ≤ 5$

这说明了什么？
输入的一行里最多只有5个字符！

于是就有个不要循环的做法啦！

```
#include<bits/stdc++.h>
using namespace std;
int main(){
    int ans=0;
    char c;
    if(cin>>c)ans++; //cin自动去除空格换行
    if(cin>>c)ans++; //cin在读不到数据时返回0
    if(cin>>c)ans++;
    if(cin>>c)ans++;
    if(cin>>c)ans++;
    cout<<ans;
}
```