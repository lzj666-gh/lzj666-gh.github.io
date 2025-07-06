# P1928 题解

这题考递归，难度适中。

题解[P1928 外星密码](https://www.luogu.com.cn/problem/P1928)

[更好的阅读体验？](https://www.luogu.com.cn/blog/wwwluogucn/solution-p1928)

------------
$1.$初步思路

输入的这个字符串是被多重「压缩」的，所以一重一重地「解压缩」可能会非常非常麻烦（不过应该是可行的），导致代码极其难以理解。

所以，我们使用**递归算法**，在读入这个字符串之后，找出被压缩的内容，再对被压缩的那个字符串实行「解压缩」操作。

举个例子：`AC[3FUN]`

首先，我们找到了被压缩的字符串：`3FUN`

对`3FUN`进行解压，得到`FUNFUNFUN`

再把原来的字符串`AC`后面添上`FUNFUNFUN`即可。

由于这个只有一重「压缩」，可能递归思想体现的不太明显，这里再举一个多重「压缩」的例子：

`SAD[4MLE[2TLE[2RE[2WA]]]`

首先找到被「压缩」的部分：

`[2MLE[2TLE[2RE[2WA]]]]`

（从此处开始剩下的部分就是递归的内容了，全部由程序自主实现）

对这个部分进行解压，找到被「压缩」的部分：

`[2TLE[2RE[2WA]]]`

再对这个部分进行解压，找到被「压缩」的部分：

`[2RE[2WA]]`

再对这个部分进行解压，找到被「压缩」的部分：

`[2WA]`

（开始一层一层跳出递归）

对这个部分进行解压并加到前一个字符串的末尾：

`[2REWAWA]`

再对这个部分进行解压并加到前一个字符串的末尾：

`[2TLEREWAWAREWAWA]`

再对这个部分进行解压并加到前一个字符串的末尾：

`[2MLETLEREWAWAREWAWATLEREWAWAREWAWA]`

再对这个部分进行解压并加到前一个字符串的末尾：

`SADMLETLEREWAWAREWAWATLEREWAWAREWAWAMLETLEREWAWAREWAWATLEREWAWAREWAWA`

至此，递归结束，「密码」破译完毕。

所以，我们只需要找到被「压缩」的子串，并把这个字符串扔给「解压缩」程序即可。

------------
$2.$注意事项

最重要的是： 千万不要跳进这个函数里面企图探究更多细节，否则就会陷入无穷的细节无法自拔。[——OI Wiki](https://oi-wiki.org/basic/divide-and-conquer/#_3)

我们也看到了，上面对`SAD[4MLE[2TLE[2RE[2WA]]]`的分析细节很多很多，十分复杂。

我们只需要把这个需要「解压缩」的字串扔给「解压缩」函数即可。

------------
$3.$代码实现

```cpp
#include<bits/stdc++.h>//万能头棒棒哒
using namespace std;
string yunqian(){
    int k;//压缩的次数
    char ch;//输入的字符
    string s="",str="";//s是最终答案，str是被压缩的字串，别忘了初始化
    /*注意：ch,s,str应该定义在函数内部，才能在每次递归中初始化，否则会导致一堆RE，可能还有几个MLE，总之没法AC，我就因为这个错了好几回*/
	while(cin>>ch){//不断输入字符
		if(ch=='['){//如果找到了被压缩的字串
			cin>>k;//输入压缩次数
			str=yunqian();//递归调用
			while(k--){
				s+=str;//把解压后的字串复制k次后添加到原来的字符串上
			}
		}
		else if(ch==']'){//如果找到了压缩的字串的末尾
			return s;//结束这一层递归并返回已经被解压的字串
		}
		else{//如果没有被压缩
			s+=ch;//直接在最后添上这个字符。
		}
	}
}
int main(){
	cout<<yunqian();
	return 0;//完结撒花～
}
```

$\text{The\ end.}$