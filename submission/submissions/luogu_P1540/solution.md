# P1540 题解

由于本题数据范围较小，我们可以用指针的方法做。

注：本文中的“指针”指的是“指针的思想”，并不是“指针类型”的“指针”。

先开两个数组，一个数组a存标记，在读入单词x时，若当前数组a中的第x位的标记为“1”，则表示该单词在内存中，若标记为“0”，则表示该单词不在内存中，这样做就可以一步判断读入的单词在当前是否在内存中，而不必从头到尾找。这样做还有一个好处，在存入单词时只需要把数组a中的第x位的标记“0”改为“1”，而在删去内存中的单词x时，只需要把数组a的第x位的标记“1”改为“0”，这样就可以做到一步到位，大大降低时间复杂度，提高程序效率。这是本题的关键之一，需要各位好好体会体会，理解理解。

再说另一个数组b。数组b存储的是内存中的单词，而且要按读入顺序存入，如b[1]中存储的单词x是在时间1存入的。要注意的是，若当前读入的单词x已经在内存中（即a[x]==1）那就不用存入数组b中，遇到内存中没有的新单词才存入。

接下来要讲指针。指针有两个，一个是l，指向当前内存中的单词中最先一个存入的，如b[l]是当前内存中第一个存入的。另一个是r，指向当前内存中的单词中最后一个存入的，如b[r]是当前内存中最后一个存入的。所以，数组b的第l位到第r位存储的就是当前内存中的单词。

遇到新单词时（即a[x]==0），情况有两种：

1.内存没被用完(即r<=m)。此时指针r向右移一位，在b[r]中存入新单词，并在数组a中把单词x的标记改为1；

2.内存已满（即r>m）。此时先删去当前内存中最先存入的单词（b[l]）。删除操作不用太复杂，只需要先把指针l向右移一位，然后再修改a数组的第b[l]位的标记就可以了，可联系上文加深理解。不要忘了最后在b[r]中存入新单词x。

这题大概就是这样做了，如果你感觉可以自己AC掉，就先不要看以下程序，自己试着打打程序。如果WA了就再认真看看上文，如果AC了就把你的程序和以下程序对比对比，看看有什么可以改进的地方。


代码如下：

    
    
```cpp
    #include <iostream>
    #include <stdio.h>
    #include <algorithm>
    using namespace std;
    int n,m,x,ans,l,r,a[1005],b[1005];
    int main()
    {
        cin>>m>>n;
        l=0;r=0;//初始化两个指针
        for (int i=1;i<=n;i++)
         {
             scanf("%d",&x);//边读入边做
             if (a[x]==0) 
             {
                 ans++;
                r++;b[r]=x;a[x]=1;//因为每次遇到新单词都要做这些操作，不如搬到判断语句外做，这样程序更简洁
                if (r>m) {l++;a[b[l]]=0;}
             }
         }
        cout<<ans;
        return 0;//千万不能忘记打这句，不然在比赛中会出错
}
```