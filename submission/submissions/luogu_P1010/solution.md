# P1010 题解

看了下面大佬们的题解，有点复杂，本蒟蒻来一发简单的

主要思路是递归/分治，因为分解出的指数还要继续分解，是重复的但规模更小的问题

关于求$log_2 x$,暴力枚举即可，数据很小
```
#include<iostream>
#include<cmath>
using namespace std;
int a;
void fff(int x)
{
    for(int i=14;i>=0;i--) //两万的数据最多是2（14）
    {
        if(pow(2,i)<=x){
        //pow（n，m）在cmath库中，返回n^m；枚举出第一个幂次方
            if(i==1) cout<<"2"; //2（1）不用再往后分解了且2^1输出为2，单独出来
            else if(i==0) cout<<"2(0)"; //2（0）也不用再往后分解了，单独出来
            else{ //若i>1则继续分解指数i
                cout<<"2(";
            fff(i);
            cout<<")";
            }
            x-=pow(2,i); //继续循环分解余下的
            if(x!=0) cout<<"+";
            //加号处理的最简单方法：若此x还没分解完，则后面还有项，所以输出一个+号
        }
    }
}
int main()
{
    cin>>a;
    fff(a);
    return 0;
}
```