# P1435 题解

###解题思路：该题说是考察如何将一个字符串添加成一个回文串的，不如说是一道求最长公共自序列的变式题，为啥这么说呢？肯定是有原因在里面的

1.    首先，我们要摸清回文串的特性，回文就是正着读反着读一样，一种非常对称不会逼死强迫症的字符串；这就是我们的突破口。。。你难道以为是逼死强迫症么？哈哈，太天真了，突破口其实是因为回文正着读反着读都相同的特性。。。这样我们就可以再建一个字符数组存储倒序的字符串

2.    我们先分析下样例：ab3bd，

它的倒序是:db3ba

这样我们就可以把问题转化成了求最长公共自序列的问题，为啥可以这么转化呢？

它可以这么理解，正序与倒序“公共”的部分就是我们回文的部分，如果把正序与倒序公共的部分减去你就会惊奇的发现剩余的字符就是你所要添加的字符，也就是所求的正解

ad
da把不回文的加起来就是我们梦寐以求的东西：回文串（卧槽？太没追求了）

把ad，da加起来成回文串就是adb3bda，所以这个问题就可以转化成了求最长公共自序列的问题，将字符串的长度减去它本身的“回文的”（最长公共自序列）字符便是正解

3.    找到解题思路后我们就可以开始写了，最长公共自序列问题是个经典的dp问题，

最容易想到的方法就是开个二维数组dp【i】【j】，i，j分别代表两种状态；

那么我们的动态转移方程应该就是if(str1[i] == str2[j])    dp[i][j]=dp[i-1][j-1]+1;

        Else dp[i][j] = max(dp[i-1][j], dp[i][j-1];

依此即可解出最长公共自序列，用字符串长度减去即是正解


```cpp
#include<cstdio>
#include<cstring>
#include<iostream>
#include<cstdlib>
using namespace std;
int n;
int dp[5001][5001];
char str1[5001],str2[5001];
int main()
{
    //freopen("palindrome.in", "r", stdin);
    //freopen("palindrome.out", "w", stdout);
    scanf("%s", str1+1);
    n = strlen(str1+1);
    for(int i = 1; i <= n; i++)
        str2[i] = str1[n-i+1];                                //做一个逆序的字符串数组 
    for(int i = 1; i<=n; i++)
        for(int j = 1; j <= n; j++)
            if(str1[i] == str2[j])
                dp[i][j] = dp[i-1][j-1] + 1;        //最长公共自序列匹配 
            else
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]);        //不匹配的往下匹配状态 
    printf("%d\n", n-dp[n][n]);                        //字符串长度减去匹配出的最长公共自序列的值 
    return 0;                                        //即需要添加的字符数 
}
```
可这并不是最优解法，只是能ac这道题而已
若是将内存限制改为2MB呢？


不过，没关系，正常开一个5001\*5001的数组一定会爆掉的，此时你是不是在思考另一种解决方案来优化一下空间复杂度，如果我可以把它用一维数组代替二维数组中的状态量是不是也可以求出正解

没错。它真的能

求出正解；

如果你仔细研究一下就会发现每次搜索到str1的第i个元素的时候，数组dp【】【】真正使用到的元素仅仅是dp【i】【j】和dp【i-1】【k】（0    <=    k    <=     n(n = strlen(str1)）

即dp【】【】的第一下标从0-->i-2就没有用处了，因此我们可以开辟两个滚动数组来降低空间复杂度

Dp1【】用来记录当前状态，dp2【】用来记录之前的状态也就相当于刚才的dp【i-1】【j】

动态转移方程应该这么表达if(str1[i]    ==        str2[i])    dp1[j]     =    dp2[j-1] +1;

Else    dp1[j]    =    max(dp1[j-1],     dp2[j]);

源代码在此，天下我有：



```cpp
#include<cstdio>
#include<cstring>
#include<iostream>
#include<cstdlib>
using namespace std;
int n;
int dp1[5001],dp2[5001];            //此处用两个滚动数组记录，一个记录之前的状态，一个记录此时的状态
char str1[5001],str2[5001];
int main()
{
    //freopen("palindrome.in", "r", stdin);
    //freopen("palindrome.out", "w", stdout);
    scanf("%s", str1+1);
    n = strlen(str1+1);
    for(int i = 1; i <= n; i++)
        str2[i] = str1[n-i+1];                                //做一个逆序的字符串数组 
    for(int i = 1; i<=n; i++)
    {
        for(int j = 1; j <= n; j++)
            if(str1[i] == str2[j])                     
                dp1[j] = dp2[j-1]+1;                //“发现”匹配就记录
            else
                dp1[j] = max(dp1[j-1],dp2[j]);        //不匹配就匹配后面的状态 
        memcpy(dp2, dp1, sizeof(dp1));                //记录之前的状态“滚动”匹配 
    }
    printf("%d\n", n-dp1[n]);            //字符串长度减去匹配出的最长公共自序列的值                          
    return 0;                            //即需要添加的字符数
}

```