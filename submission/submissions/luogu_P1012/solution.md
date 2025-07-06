# P1012 题解

## 这里有证明

今明两天期末考试，本蒟蒻自忖考得不行，为转移注意力，特地来洛谷更新一下题解 ~~（这是什么神逻辑）~~ 。话说这是本蒟蒻的第一篇题解，也是花了很长时间憋出来的一篇题解（萌新想写题解真难），但原文讲的并不清楚 ~~估计只有我自己能看懂~~ ，此次修改务求让大伙一看就明白。本题解看着字多，思路还是比较简单的。

本题解重心在证明。先贴下代码，非常简短：

```cpp
#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

string s[21];int n;
bool cmp(const string &a,const string &b) { // &表示引用
    return (a+b > b+a);
}
int main(void) {
    cin >> n;
    for(int i=1;i<=n;++i) cin >> s[i];
    sort(s+1,s+n+1,cmp);
    for (int i=1;i<=n;++i) cout << s[i];
    return 0;
}

```

证明之前，我们先定义几个符号   
$ \overline {ab} $ （a,b是数字字符串）  
表示 $ a+b $ 也就是把$a$和$b$连起来写  
$ \overline {abc} $ （a,b,c都是数字符串）（当然再多几个字符串也没关系，跟上面一个意思）  
没错，这个东西本来是表示数字的，现在被我们借过来表示字符串  

$ a \geqslant b $ 表示正常的$a$大于等于$b$ （下面这个就是不正常的）  
**a>=b** a,b是数字字符串 表示 $ a+b \geqslant b+a $  
**注意区分这两个大于等于！**  

**a\*n** a是数字字符串 n是正整数 表示把$a$连续写$n$遍形成的很长的字符串

说明了这么几个奇怪的符号之后，我们正式开始证明。

从代码中可以看出，我们把$a$数组按这个 **>=** 符号 **降序** 排好序，再直接输出就是正确的答案了。容易发现，对于任意一种排列方式，只要相邻的两个数**不**满足 前面的 **>=** 后面的（注意这是那个奇怪的大于等于），那么这种排列肯定不是最优的。也就是说，对于最优排列，肯定有 第一个串 **>=** 第二个串    第二个串 **>=** 第三个串   第三个串 **>=** 第四个串 ... 依此类推。

经过这一些简单的推理，证明的思路实际上很清晰了（千万不要误认为证完了）：只需要再证明传递性（由**a>=b** 且 **b>=c** 能否推出 **a>=c**)。这是最后的一步，也是关键的一步。

先证明一个性质： 如果 **a>=b**，那么 **a\*n >= b**。 （思路：递推/数学归纳法）  

由**a>=b**即 $ \overline {ab} \geqslant \overline {ba} $  
可知 $ \overline {aab} \geqslant \overline {aba} $ 并且 $ \overline {aba} \geqslant \overline {baa} $   
从而 $ \overline {aab} \geqslant \overline {baa} $ 也就是 **a\*2>=b**

由**a\*2>=b**即 $ \overline {aab} \geqslant \overline {baa} $ 又由   $ \overline {ab} \geqslant \overline {ba} $   
可知 $ \overline {aaab} \geqslant \overline {abaa} $ 并且 $ \overline {abaa} \geqslant \overline {baaa} $   
从而 $ \overline {aaab} \geqslant \overline {baaa} $ 也就是 **a\*3>=b**  

依此类推，便能证得 **a\*n>=b**  
类似地，由 **a>=b**，也可以得到 **a>=b\*n**。
相反，如果 **a\*n>=b** 或者 **a>=b\*n**，也能得到 **a>=b**。（口胡一个证明，如果不满足**a>=b**这个结论，肯定不满足题设，如果能满足**a>=b**这个结论，题设肯定成立。大概是一个反证法？）

有了这个结论，我们只要对$a,b,c$各乘上一个合适的整数（没错就是合适），不难证明传递性了。

### 原以为修改后能改短，~~却发现它变长了~~。但是你看我改的这么认真，不点个赞再走吗？

2019\-09\-11 写作  2020\-01\-13 修改 （这次小修改求管理通过）（逃