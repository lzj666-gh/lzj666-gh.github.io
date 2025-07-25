# P3952 题解

#### [点*我看@题￥目(晚了^会被&删](https://www.luogu.org/problemnew/show/P3952)

## 解题背景

~~我也不知道为什么会有解题背景~~ 这道题很久之前就听说过并且看过题面，但是由于久负盛名的**毒瘤**我一直懒得写。这两天我跟*jiang25262*搞到一起的时候我发现他也在做这道题，而且据*FCL*说，jiang佬已经做这题做了一个多月了……

于是本着~~试试看~~的心态开始着手解决这道题。这道题从接手到AC时间跨度大概**27h**（算上吃饭睡觉~~打游戏~~等时间），时间上可能比jiang佬稍微快一点。说来也巧，就在我刚接手这道题的那天晚上，jiang佬十分神犇地**AC**了……

再看看我自己俩小时写出来的一个爆零和一个28pts，更加坚定了我要A掉这题的想法

当晚心态爆炸

## 解题思路

这道题一眼看上去似乎很好办，操作总结起来就两点
- 求最大循环嵌套层数
- 判断是否有语法错误

为了节省时间和空间，本题我采用**在线做法**。即边读边操作输出。这种做法对于离线做法来说有利有弊，后文将会讲到 （jiang25262采用的是离线做法）

### 求最大循环嵌套层数

循环嵌套的结构非常类似一个栈的结构，都满足**先进后出，后进先出**的性质。那么这个问题就可以用一个栈来维护，具体实现如下

新定义一个栈，姑且命名为`zhan`好了……
- 对于读到的每一个`F`，向栈中压入任意一个元素，我们每次都压入`1`
- 询问当前栈元素的个数，每次保存其最大值
- 对于读到的每一个`E`，弹出栈顶元素
- 栈元素个数的最大值就是最大循环嵌套层数

这样看上去没什么大问题，手出一组数据也是能过的。这个子问题先告一段落

### 判断是否有语法错误

根据题面：

> 其中语法错误只有:1、F和E不匹配  2、新建的变量与已经存在但未被销毁的变量重复两种情况

我们着手解决这样两个子问题
- 匹配`F`和`E`
- 判断冲突变量名

#### 匹配`F`和`E`

我们很容易就可以想出一种显而易见的`ERR`情况：**输入数据的行数为奇数**，这样它无论怎样都不会匹配成功，直接抛出`ERR`

还有一种比较容易想的`ERR`情况：**F和E的个数不相等**，这样也不会匹配成功，抛出`ERR`

在以上两种情况都不满足的情况下，我们大致思考一下，发现只剩下一种`ERR`情况：**一个(不是一层)循环已经完全退出，但还有多余的E试图继续退出该循环**。这种情况实现起来其实也容易，因为我们事先维护了一个栈，所以我们在遇到`E`的时候先判断一下栈是不是空了，如果栈没空，就弹出栈顶元素。如果栈空了，直接抛出`ERR`

#### 判断冲突变量名

这个东西看上去不太好搞，实际上实现起来确实有一定难度。变量名的开辟与销毁虽然也满足**先进后出，后进先出**的结构，但却不能用栈来维护，因为栈不支持元素的查找。所以在碰到一个变量名时，栈无法确认它是否已经出现，故而无法判断变量名冲突。

根据以上分析，我们需要一种结构来同时支持如下两种操作：
- 有类似栈的先进后出后进先出顺序
- 支持元素查找

经过一番思索，我决定使用**字符串**来解决这个问题。具体实现如下：
- 定义一个变量列表字符串`sublist`，并赋初值为"0"
- 每次读入`F`获得一个变量名sub时，将其添加到`sublist`末端。因为字符串的特殊性质，直接`sublist+=sub`即可，需要注意，`sub`也应当是一个字符串类型而不是字符型。
- 使用字符串类自带的函数find()寻找刚读入的`sub`在`sublist`中**第一次**出现的位置，如果满足`sublist.find(sub)==sublist.length()-1`则该变量名未被使用过。
- 每次读入`E`销毁一个变量名时，直接删掉字符串最后一个字符即可

判断语法的两个子问题到此已经解决完毕

按理说，题目要求的两个子问题我们都已经解决，这题应该做完了。但是更加复杂的情况其实还在后面。

## 特殊情况处理

我们回顾“时间复杂度”的性质想一想，一个循环如果想对时间复杂度的指数有影响，那么这个循环的**本身复杂度**必须是一次或更高次项。常数级别的循环不会对复杂度的指数有影响，比如两个例子（以题目标准书写）：

```cpp
  F i 3 n
  F j 2 n
  F k 6 n
```
这个算法的时间复杂度是$O(n^3)$的

```cpp
  F i 4 7
  F j 2 9
  F k 12 95
```
这个算法的时间复杂度是$O(1)$的，因为循环只到达了常数级别

**注意，以上我所说的性质仅仅针对本题而言（因为本题的n趋近于正无穷），不适用于其他环境**

我们再回归“循环”的性质想一想，进入一个循环的条件是什么。那当然是满足`初始值<=终止值`这样一个条件。那么有，`F i 72 1`、`F i n 23`显然是两个不能进入的循环。而对于一个不能进入的循环，**嵌套在它之下的循环也不能进入**

综上，我们在两个子问题的处理上出了漏洞，有这样三个：
- 未判断常数级别的循环
- 未判断是否能进入循环
- 循环嵌套的最大层数判定不正确

我们一一解决

### 判断常数级别的循环

这个好办，只要看一看起始值和终止值是否同时不是n就好了。但是判断好判断，之后的处理不能少。因为这个循环的影响是常数级的，所以嵌套层数可以视为不影响，只要在判出常数级循环后再弹出一个栈顶元素就好了

### 判断能否进入循环&最大层数判定

这无疑是这道题目的一个重大难点。在讨论这部分的时候，我们会将之前所做的一些操作彻底推翻，重新维护新的操作来满足新的需求。

判断能否进入循环也好办，把n视作`inf`，然后比较一下起始值和终止值就能很快得出结果

重难点在于最大层数判定。当我们判出不能进入循环的时候，下面的嵌套应该全部抛弃不看，但是我们面临一个问题：**我们怎么知道哪些嵌套在它下面？**。追根溯源，这个问题的产生就在于我们对之前维护的层数栈的处理。上文提到：

> 对于读到的每一个`F`，向栈中压入任意一个元素，我们每次都压入'1'

问题就出在“每次都压入'1'上面”，这直接导致了我们无法获取当前嵌套的层数。一个很好的解决办法就是，**对于读到的每一个`F`，向栈中压入当前嵌套深度值i**。这样处理的好处是显而易见的，我们在判断无法进入循环后就有了一个舍弃哪些循环的范围。具体操作如下：
- 定义一个`runflag`，并赋初值为-1
- 当我们判定到不能进入当前循环时，把`runflag`的值赋为栈顶元素
- 如果`runflag`是-1，正常取栈元素个数的最大值作为答案。否则不记录
- 读到`F`、`E`时正常压入弹出元素
- 每次弹出都询问栈顶元素，如果栈顶已经退回了`runflag`深度，则把`runflag`还原成-1

特殊情况处理完毕，但在真正实现的时候为了保险我还进行了其他的存储操作，具体见附的AC代码

## 数据处理

真的以为这题做完了吗？当然不是。如果一上来就做这道题，你会发现，连数据的读入都不会，甚至你无法获得小明的答案（我在这里卡了10min ~~真丢人~~）。下面我们对于数据处理重点讨论。因为字符串的灵活性，我的大部分操作直接使用字符串读入完成。

### 获得小明的答案

在读完行数之后用一个字符串`tmp`存`O(xxx)`的内容，然后判断`tmp[2]`是不是数字(其实就是'1')，如果是，则小明的答案可以记为'0'（表示$O(1)$)。如果不是，那么把字符串从头到尾扫一遍，用类似快读的方式获取小明的答案。具体代码如下：

```cpp
for(rint i=0;i<tmp.length();++i)
    if(tmp[i]>='0'&&tmp[i]<='9'){
        hisans+=tmp[i]-'0';
        hisans*=10;
    }
hisans/=10;
```

### 获得循环的各项参数

定义四个字符串`opt`、`sub`、`tmpsta`、`tmpend`，然后读入。如果`tmpsta[0]`是'n'，且`tmpend[0]`和`tmpsta[0]`和`tmpend[0]`不全是'n'，则可以进入循环。

然后用上文类似的代码，获得真正的起始值`sta`和终止值`end`，判断能否执行循环。

## 最后的话

这一题到此就做完了，但是我们仍然要注意一些细节性的问题。

因为我是在线做的，在线做的优点就是边读边做，省时间省空间。但是如果某些变量忘记清零就会导致某些玄幻而低级的错误。jiang25262的离线做法据说开了三个10w级别的数组来模拟栈……但是他的清零就是10行`memset`了事。

除了离线和在线，还要避免重复输出的情况，需要使用一个`flag`来避免输出多次。具体见文末附上的AC代码。

## 感谢阅读

### 欢迎加入我们的团队！ &emsp; [团队传送门](https://www.luogu.org/team/show?teamid=10716)

持续捕捉洛谷野生大佬中（14/1e9+7），也欢迎萌新前来投食。团队QQ群号可**私信叶小枫**获取。

## AC代码

```cpp
#include<bits/stdc++.h>
#define ll long long
#define rint register int
using namespace std;
stack<int> zhan;
int main(){
    int t;scanf("%d",&t);
    while(t--){
        int n;scanf("%d",&n);
    	int nowline=0,pos=0;
    	int Fcnt=0,Ecnt=0,cnt=0;
        int hisans=0,myans=0;
        int runflag=-1;
    	bool endflag=false;
        string tmp;cin>>tmp;
        string sublist="0";
        for(rint i=0;i<tmp.length();++i)
            if(tmp[i]>='0'&&tmp[i]<='9'){
                hisans+=tmp[i]-'0';
                hisans*=10;
            }
        hisans/=10;
        if(tmp[2]=='1') hisans=0;
        for(rint i=1;i<=n;++i){
            string sub,opt,tmpsta,tmpend;
            int sta=0,end=0;
            cin>>opt;
            if(opt=="F"){
            	++Fcnt;++pos;
                zhan.push(pos);
                cin>>sub>>tmpsta>>tmpend;
                if(tmpend[0]=='n'&& (!(tmpsta[0]=='n'&&tmpend[0]=='n'))) ++cnt;
                for(rint j=0;j<tmpsta.length();++j){
                    sta+=tmpsta[j]-'0';
                    sta*=10;
                }
                sta/=10;
                if(tmpend[0]!='n'){//如果end是数字 
                    for(rint i=0;i<tmpend.length();++i){
                        end+=tmpend[i]-'0';
                        end*=10;
                    }
                    end/=10;
                    if(sta>end)//如果循环不能执行 
                        runflag=pos;
                }
                if(runflag==-1||pos<runflag) myans=max(myans,cnt);
                sublist+=sub;
                if(sublist.find(sub)!=sublist.length()-1){
                	printf("ERR\n");cnt=0;nowline=i;endflag=true;break;
                }
                sta=0;end=0;
            }
            else if(opt=="E"){
            	--cnt;++Ecnt;
                if(zhan.empty()&&!endflag){
            		printf("ERR\n");cnt=0;nowline=i;endflag=true;break;
                }
                if(zhan.top()<=runflag){
                	pos=0;
                	runflag=-1;
                }
                if(!zhan.empty()) zhan.pop();
                if(sublist.length()>0) sublist=sublist.substr(0,sublist.length()-1);
            	if(zhan.empty()) cnt=0;
            }
        }
        if(endflag){
        	cnt=0;
        	while(!zhan.empty())
        		zhan.pop();
        		string cnm;
        	for(rint i=1;i<=n-nowline+1;++i) getline(cin,cnm);
        	continue;
        }
        if(Fcnt!=Ecnt){
        	if(!endflag) printf("ERR\n");
        	while(!zhan.empty()) zhan.pop();
        	cnt=0;
        	continue;
        }
        while(!zhan.empty()) zhan.pop(); 
        if(!endflag){
        	if(myans==hisans) printf("Yes\n");
        	else printf("No\n");
        }
        myans=hisans=0;
    }
    return 0;
}
```