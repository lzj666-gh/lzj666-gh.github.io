# P2580 题解

# map的练手题
## map轻松搞定~~
这道题可以给大家练练STLmap的用法，让大家感受STL的方便QAQ

看到楼下没有map的好题解（就是精简的）~~（可能我眼睛不好）~~

比什么字典树不简单多了QAQ

先把所有的人名字存起来，使用map，这样可以建立从名字到数的映射，标记为1，然后扫一遍，如果为1，输出OK，同时将1更新为2，如果遇到为2，输出REPEAT，如果为0，说明没有，输出WRONG，不就行了？


时间复杂度O(n+m);

具体解释&&map的介绍见代码：

```
#include<map>
#include<cmath>
#include<stack>
#include<cstdio>
#include<vector>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;
typedef long long ll;
map<string,int>a; //map定义，相当于数组的升级版，表示string到int的映射，举个简单例子，可以用a["OK"]=1;进行赋值（说白了就是括号里的数据类型是map<>前面的，=的后面就是map<>后面的数据类型）
string s;//用于读入的字符串
int n,m;
int main(){
    cin>>n;
    while(n--){//因为是n+m就可以了，所以直接n--，--QWQ
    	cin>>s;
    	a[s]=1;//直接这样赋值
    }
    cin>>m;
    while(m--){
    	cin>>s;
    	if(a[s]==1){puts("OK");a[s]=2;}//前面讲的很清楚，不赘述了
    	else if(a[s]==2)puts("REPEAT");//输出
    	else puts("WRONG");
    }
	return 0;//完美的过程，不是吗？
}
```