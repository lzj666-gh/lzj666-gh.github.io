# P1024 题解

```cpp

【二分】
因为区间很大，所以可以二分。
三个答案都在[-100,100]范围内，两个根的差的绝对值>=1,保证了每一个大小为1的区间里至多有1个解，也就是说当区间的两个端点的函数值异号时区间内一定有一个解，同号时一定没有解。那么我们可以枚举互相不重叠的每一个长度为1的区间，在区间内进行二分查找。
【参见代码】
#include<cstdio>
double a,b,c,d;
double fc(double x)
{
    return a*x*x*x+b*x*x+c*x+d;
}
int main()
{
    double l,r,m,x1,x2;
    int s=0,i;
    scanf("%lf%lf%lf%lf",&a,&b,&c,&d);  //输入
    for (i=-100;i<100;i++)
    {
        l=i; 
        r=i+1;
        x1=fc(l); 
        x2=fc(r);
        if(!x1) 
        {
            printf("%.2lf ",l); 
            s++;
        }      //判断左端点，是零点直接输出。
                        
                        //不能判断右端点，会重复。
        if(x1*x2<0)                             //区间内有根。
        {
            while(r-l>=0.001)                     //二分控制精度。
            {
                m=(l+r)/2;  //middle
                if(fc(m)*fc(r)<=0) 
                   l=m; 
                else 
                   r=m;   //计算中点处函数值缩小区间。
            }
            printf("%.2lf ",r);  
            //输出右端点。
            s++;
        }
        if (s==3) 
            break;             
            //找到三个就退出大概会省一点时间
    }
    return 0;
}

```

【盛金公式】の做法
```cpp
#include <iostream>
#include <math.h>
#include <iomanip>
using namespace std;
int main()
{
     double a,b,c,d;
     double as,bs,t,si;
     double x1,x2,x3;
     cin>>a>>b>>c>>d;
     as=b*b-3*a*c;
     bs=b*c-9*a*d;
     t=(2*as*b-3*a*bs)/(2*sqrt(as*as*as));
     si=acos(t);
     x1=(-b-2*sqrt(as)*cos(si/3))/(3*a);
     x2=(-b+sqrt(as)*(cos(si/3)+sqrt(3)*sin(si/3)))/(3*a);
     x3=(-b+sqrt(as)*(cos(si/3)-sqrt(3)*sin(si/3)))/(3*a);
     cout<<fixed<<setprecision(2)<<x1<<" ";
     cout<<fixed<<setprecision(2)<<x3<<" ";
     cout<<fixed<<setprecision(2)<<x2<<" ";
     return 0;
}
```
盛金公式：
       
       一元三次方程:aX的三次方+bX的二次方+cX+d=0
       重根判别公式：
           A=b的二次方-3ac
           B=bc-9ad
           C=c的二次方-3bd
       当A=B=0时，X1=X2=X3= -b/3a= -c/b = -3d/c

【暴力枚举--出奇迹】

```cpp
#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
   double a,b,c,d;
   scanf("%lf%lf%lf%lf",&a,&b,&c,&d);
   for(double i=-100;i<=100;i+=0.001)
   {
      double j=i+0.001;
      double y1=a*i*i*i+b*i*i+c*i+d;
      double y2=a*j*j*j+b*j*j+c*j+d;
      if(y1>=0&&y2<=0||y1<=0&&y2>=0)
      {
         double x=(i+j)/2;
         printf("%.2lf ",x);
      }
   }
}
```