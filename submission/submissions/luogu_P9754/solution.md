# P9754 题解

# 前言

本蒟蒻在考场中时并没有写出此题，但是赛后重新做一遍后发现居然并没有想象中那么难，甚至写完后交两遍就过了！而且就算是第一遍也得到了 85 分的高分！

所以考场时为什么没有写出这道题呢？（懊恼）

------------

本篇题解中所有代码基于这样的设置：

```cpp
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll,ll> pr;
const int MAXN=256;
ll max(ll x,ll y){return x>y?x:y;}
ll min(ll x,ll y){return x<y?x:y;}
pr mp(ll x,ll y){return (pr){x,y};}
//用来输入的变量
ll n,op,k,addr_in;
string s,ti,ni,in1[MAXN],in2[MAXN];
```

所以若是遇见了不认识的东西，多半是从这里出来的。

**额外声明：因为是大模拟，所以笔者的代码中的变量名以容易理解优先，笔者承诺代码并非 AI 生成，均为笔者自己所写。**

# 正文

## 题意理解

其实去除掉**对齐规则**后，题面并不难理解，难度也会下降很多，因此这里主要解释**对齐规则**。

所谓“对齐”，就是对于一个类型的变量，其拥有一个**对齐要求**，每个类型的变量的起始位置的地址，以及终止位置的下一位的地址，都必须是这个**对齐要求**的整数倍。

这就意味着对于一个变量，其内部的地址可能并不是连续的。

拿题面中给出的例子举例：

```cpp
struct TypeA{
    short MemberA;
    int MemberB;
    short MemberC;
};
TypeA ElementA;
```

为了阅读方便，我将变量名修改了一下。

上面这个例子中，我们定义了一个结构体类型 `TypeA`，在其中包含了三个成员，分别是 `short` 类型的 `MemberA` 和 `MemberC`，以及 `int` 类型的 `MemberB`。

然后我们定义了一个 `TypeA` 类型的元素 `ElementA`。

接下来分析 `ElementA` 的内存分布  ，`MemberA` 的大小为 $2$ 字节，占据的地址为第 $0\sim1$ 字节。`MemberB` 的大小为 $4$ 字节，占据的地址本应是第 $2\sim5$ 字节——但是注意：根据**对齐规则**，`int` 类型的元素的起始位置必须是 $4$ 的整数倍，因此 `MemberB` 占据的地址应为第 $4\sim7$ 字节。

`MemberC` 占据的地址为第 $8\sim9$ 字节。

根据**对齐规则**，可得 `TypeA` 类型的元素的**对其要求**为其成员类型中最大的**对齐要求**，为 $4$ 字节。

于是我们得到，`TypeA` 类型的元素占据的地址为 $0\sim9$ 字节，**对齐要求**为 $4$ 字节。

对吗？

当然不对，我们知道，根据**对齐规则**，元素终止位置的下一位的地址也应该是**对齐要求**的整数倍，虽然这一点并没有在题面中很好地说明，但是题面中给出的例子却是这样的。

因此，`TypeA` 类型的元素占据的地址为 $0\sim11$ 字节，**对齐要求**为 $4$ 字节。

下为 `TypeA` 类型的元素占据地址的示意图：

$\mathrm{\displaystyle\begin{aligned}
&0\ &\fbox{MemberA}\\
&1\ &\fbox{MemberA}\\
&2\ &\fbox{None}\\
&3\ &\fbox{None}\\
&4\ &\fbox{MemberB}\\
&5\ &\fbox{MemberB}\\
&6\ &\fbox{MemberB}\\
&7\ &\fbox{MemberB}\\
&8\ &\fbox{MemberC}\\
&9\ &\fbox{MemberC}\\
&10\ &\fbox{None}\\
&11\ &\fbox{None}\\
\end{aligned} }$

图中的 $\mathrm{None}$，即为适应**对齐规则**而留下的空洞。

而我如果再定义一个 `TypeB` 呢？就像这样：

```cpp
struct TypeB{
    byte Member1;
    TypeA Member2;
};
TypeB ElementB;
```

那么 `ElementB` 占据的地址长这样（假设没有定义元素 `ElementA`）：

$\mathrm{\displaystyle\begin{aligned}
&0\ &\fbox{Member1}\\
&1\ &\fbox{None}\\
&2\ &\fbox{None}\\
&3\ &\fbox{None}\\
&4\ &\fbox{MemberA}\\
&5\ &\fbox{MemberA}\\
&6\ &\fbox{None}\\
&7\ &\fbox{None}\\
&8\ &\fbox{MemberB}\\
&9\ &\fbox{MemberB}\\
&10\ &\fbox{MemberB}\\
&11\ &\fbox{MemberB}\\
&12\ &\fbox{MemberC}\\
&13\ &\fbox{MemberC}\\
&14\ &\fbox{None}\\
&15\ &\fbox{None}\\
\end{aligned} }$

其中第 $4\sim15$ 字节的地址被类型 `TypeA` 的 `Member2` 占据。

那么 `TypeB` 类型的元素的**对齐要求**为 $4$ 字节，占据地址为第 $0\sim15$ 字节。

没有问题吧？

## 操作实现

### 1. 类型的存储

由于需要定义很多新的类型，所以我们需要解决这些类型的存储问题。

具体地，我们可以构建一个结构体来表示一个类型。

先来看看一个类型需要些什么东西吧：

1. 类型名称。

2. 成员元素的类型，以及成员元素的名称。

3. 占据内存大小。

4. **对齐要求**，这个尤为重要。

于是我们可以得到一个这样的结构体：

```cpp
//类型结构体
struct Type{
    string Name;//类型名称
    vector<Type*> Member_Type;//类型成员类型
    vector<string> Member_Name;//类型成员元素
    ll Memory_Size;//类型占用内存大小
    ll Memory_Align;//类型对齐要求
    void clear(){
        Name.clear();
        Member_Type.clear();
        Member_Name.clear();
        Memory_Align=Memory_Size=0;
    }
};
```

此外，我们还需要存储已被定义过的类型：

```cpp
Type Def_Type[MAXN];//已被定义过的类型
ll Type_Num;//已被定义过的类型数量
```

还应该能够对于一个名称，找到对应的类型。

```cpp
map<string,Type*> Name_To_Type;//名称到类型的映射
```

这样，我们的类型存储系统就完成了：

```cpp
//类型结构体
struct Type{
    string Name;//类型名称
    vector<Type*> Member_Type;//类型成员类型
    vector<string> Member_Name;//类型成员元素
    ll Memory_Size;//类型占用内存大小
    ll Memory_Align;//类型对齐要求
    void clear(){
        Name.clear();
        Member_Type.clear();
        Member_Name.clear();
        Memory_Align=Memory_Size=0;
    }
};
Type Def_Type[MAXN];//已被定义过的类型
ll Type_Num;//已被定义过的类型数量
map<string,Type*> Name_To_Type;//名称到类型的映射
```



### 2. 元素的存储

除了声明一个结构体类型外，题目还要求我们支持定义元素。

对于元素，由于只有最外层的元素拥有自由的名称，因此我们只存储最外层的元素。

对于一个元素结构体，需要：

1. 元素类型。

2. 元素名称。

3. 元素起始地址。

于是可以写出这样的元素结构体：

```cpp
//元素结构体
struct Element{
    Type Ele_Type;//元素类型
    string Name;//元素名称
    ll Address;//元素起始地址
    void clear(){
        Ele_Type.clear();
        Name.clear();
        Address=0;
    }
};
```

同样地，我们还需要能够存储已被定义的元素，以及名称到元素的查找：

```cpp
Element Def_Ele[MAXN];//已被定义过的元素
ll Ele_Num;//已被定义过的元素数量
map<string,Element*> Name_To_Ele;//名称到元素的映射
```

这样，我们的元素存储系统就完成了：

```cpp
//元素结构体
struct Element{
    Type Ele_Type;//元素类型
    string Name;//元素名称
    ll Address;//元素起始地址
    void clear(){
        Ele_Type.clear();
        Name.clear();
        Address=0;
    }
};
Element Def_Ele[MAXN];//已被定义过的元素
ll Ele_Num;//已被定义过的元素数量
map<string,Element*> Name_To_Ele;//名称到元素的映射
```

### 3. 地址分配

地址分配与题面中的 2、3、4 操作有着密不可分的关系，对于地址的分配，我们显然也需要一个系统来维护。

具体地，我们只需要知道两个东西：“地址分配到了哪”，和“该地址处有什么东西”。

对于“地址分配到了哪”，我们可以用一个数记录：

```cpp
ll Addr_Pos;//已分配到的地址位置
```

而对于“该地址处有什么东西”，我们显然需要开一个映射。

不过这道题的地址可能会很大，所以一个一个地址去存显然不现实，于是考虑对于每一个元素，只以其地址的左右端点为键值：

```cpp
map<pr,Element*> Addr_To_Ele;//地址到元素的映射
```

但是在一个元素的内部会存在空洞怎么办？

那就是操作 4 需要考虑的问题了，这里先不管。

总得来说，我们的地址维护系统长这样：

```cpp
//地址
ll Addr_Pos;//已分配到的地址位置
map<pr,Element*> Addr_To_Ele;//地址到元素的映射
```

### 4. 初始化

在最开始没有任何操作时，存在四种**基本类型**：

1. `byte`，大小为 $1$ 字节，**对齐要求**为 $1$ 字节。

2. `short`，大小为 $2$ 字节，**对齐要求**为 $2$ 字节。

3. `int`，大小为 $4$ 字节，**对齐要求**为 $4$ 字节。

4. `long`，大小为 $8$ 字节，**对齐要求**为 $8$ 字节。

不难发现，**基本类型**的**对齐要求**就是它们的大小。

同时，**基本类型**没有成员类型。

所以我们需要进行预处理：

```cpp
//预处理
void init(){
    Def_Type[1].Name="byte";
    Def_Type[2].Name="short";
    Def_Type[3].Name="int";
    Def_Type[4].Name="long";
    Def_Type[1].Memory_Align=Def_Type[1].Memory_Size=1;
    Def_Type[2].Memory_Align=Def_Type[2].Memory_Size=2;
    Def_Type[3].Memory_Align=Def_Type[3].Memory_Size=4;
    Def_Type[4].Memory_Align=Def_Type[4].Memory_Size=8;
    Name_To_Type["byte"]=&Def_Type[1];
    Name_To_Type["short"]=&Def_Type[2];
    Name_To_Type["int"]=&Def_Type[3];
    Name_To_Type["long"]=&Def_Type[4];
    Type_Num=4;
}
```

### 4.5 间言

那么现在万事具备，只欠东风了。完成此题目需要的变量等东西都已经写好了，接下来讲解操作的实现。

### 5. 操作 1

操作 1 让我们创建一个新类型。

对于一个类型的各种要素，需要进行如下操作：

* 名称：这个就在输入里面，直接赋值即可。

* 成员：这个也在输入里面，遍历输入赋值即可。

* **对齐要求**：类型的**对齐要求**为其成员中的最大**对齐要求**，在遍历中访问每一个成员的**对齐要求**，然后取最大即可。

* 占用内存大小：这个需要斟酌一下，首先，不能单纯地计算成员大小的总和，因为需要注意**对齐规则**，在进入下一个成员的大小计算时，需要判断起始位置是否满足**对齐规则**，若不满足，则需要将起始位置后移。在所有成员计算完毕后，还应该判断这个类型的终止位置的下一位是否满足**对齐规则**，若不满足，则需将终止位置后移。最后计算出的终止位置与起始位置作差即可（不过默认起始位置为 $0$）。

最后，别忘了维护已被定义的类型的数组，以及类型名称到类型的映射。

具体代码如下：

```cpp
//创建一个类型的函数
void Type_Create(string type_name,ll num,string *ar1,string *ar2){
    Type New_Type;//创建一个新类型
    New_Type.clear();
    New_Type.Name=type_name;//名字直接赋值
    for(int i=1;i<=num;i++){
        New_Type.Member_Type.push_back(Name_To_Type[ar1[i]]);//成员类型直接赋值
        New_Type.Member_Name.push_back(ar2[i]);//成员名称直接赋值
    }
    ll pos=0;//起始地址默认为 0
    vector<Type*>::iterator it=New_Type.Member_Type.begin();
    for(;it!=New_Type.Member_Type.end();it++){//遍历成员
        ll Align=(*it)->Memory_Align;//成员对齐要求
        ll Size=(*it)->Memory_Size;//成员大小
        New_Type.Memory_Align=max(New_Type.Memory_Align,Align);//类型的对齐要求为其成员中的最大对齐要求
        if(pos%Align)pos=(pos/Align+1)*Align;//如果起始地址不满足对齐规则
        pos+=Size;//下一个成员的起始地址(这个成员的终止地址)
    }
    if(pos%New_Type.Memory_Align)
        pos=(pos/New_Type.Memory_Align+1)*New_Type.Memory_Align;//如果终止地址不满足对齐规则
    New_Type.Memory_Size=pos;//终止地址减去起始地址即为大小(起始地址默认为 0)
    Def_Type[++Type_Num]=New_Type;//别忘了维护这个数组
    Name_To_Type[type_name]=&Def_Type[Type_Num];//别忘了维护这个映射
}
```

### 6. 操作 2

操作 2 让我们创建一个新元素。

先来分析一下如何处理一个新元素的各种要素：

* 类型：这个就在输入里面，通过名称到类型的映射直接赋值即可。

* 名称：这个就在输入里面，直接赋值即可。

* 元素起始地址：这个直接赋为目前地址分配到的最高位置即可，但要注意，如果当前地址不满足**对齐规则**，则需要按**对齐要求**后移地址。

好像挺简单的？

然后别忘了维护已被定义过的元素的数组，以及元素名称到元素的映射。

最后，别忘了维护地址，因为一个类型的声明是不会占用内存的，而元素的定义是会切实占用内存的。

具体代码如下：

```cpp
//创建一个元素的函数
void Ele_Create(string type_name,string ele_name){
    Element New_Ele;//创建一个新元素
    New_Ele.clear();
    ll Align=Name_To_Type[type_name]->Memory_Align;//该元素的类型的对齐要求
    ll Size=Name_To_Type[type_name]->Memory_Size;//该元素的大小
    if(Addr_Pos%Align)Addr_Pos=((Addr_Pos/Align+1)*Align);//若起始位置不满足对齐规则
    New_Ele.Address=Addr_Pos;//起始地址赋值
    New_Ele.Ele_Type=*Name_To_Type[type_name];//通过映射找到该类型，赋值
    New_Ele.Name=ele_name;//名称直接赋值
    Def_Ele[++Ele_Num]=New_Ele;//别忘了维护这个数组
    Name_To_Ele[ele_name]=&Def_Ele[Ele_Num];//别忘了维护这个映射
    Addr_To_Ele[mp(Addr_Pos,Addr_Pos+Size-1)]=&Def_Ele[Ele_Num];//将元素的起始位置和终止位置作为键值加入元素
    Addr_Pos+=Size;//更新最高位地址
}
```

### 7. 操作 3

操作 3 让我们访问某个元素。

比较棘手的是，这个元素的名字中间是带点的。

这意味着我们需要先找到最外层元素，然后根据最外层元素的类型找到次外层元素，然后根据次外层元素的类型找到……

如此往复，是一个递归的过程。

不过实际上实现并不需要递归，具体地，分为以下几步：

1. 处理元素的名称，将中间的调用符（即 `.`）去掉，剩下的分开放入一个队列中。

2. 取出队首元素，弹出队首，根据元素的类型遍历成员名称，若是遇上了与新队首元素同名的成员，即停止遍历，更新起始地址。具体地，起始地址也需要满足**对齐规则**。

3. 重复 2 操作，直到队列为空。

最后，更新完毕的起始地址即为所需的答案。

具体代码如下：

```cpp
//访问某个元素的函数
ll Visit_Ele(string ele_name){
    queue<string> name;//存储名称的队列
    string tool;//如其名
    tool.clear();
    for(int i=0;i<(ll)ele_name.length();i++){//处理名称
        if(ele_name[i]=='.'){//如果遇上了调用符
            name.push(tool);
            tool.clear();
        }
        else tool+=ele_name[i];
    }
    name.push(tool);
    ll pos=Name_To_Ele[name.front()]->Address;//起始地址为最外层元素的起始地址
    Type type=Name_To_Ele[name.front()]->Ele_Type;//最外层元素的类型
    name.pop();
    while(!name.empty()){
        string Name=name.front();//取出队首
        name.pop();
        vector<string>::iterator it1=type.Member_Name.begin();//遍历成员名称
        vector<Type*>::iterator it2=type.Member_Type.begin();//遍历成员类型
        for(;it1!=type.Member_Name.end();it1++,it2++){
            if(pos%(*it2)->Memory_Align)
                pos=(pos/(*it2)->Memory_Align+1)*(*it2)->Memory_Align;//如果起始地址不满足对齐规则
            if(*it1==Name){//如果找到了新队首
                type=**it2;
                break;
            }
            else pos+=(*it2)->Memory_Size;//更新起始地址
        }
    }
    return pos;
}
```

### 8. 操作 4

操作 4 让我们访问一个地址。

这里最棘手的的地方在于：在**对齐规则**下，地址的分配并不是连续的，中间会出现空洞。

这意味着我们需要在访问时判断这个地址是否有元素占据。

具体地，可以分为一下几步：

1. 判断访问地址是否在某个元素内，即地址是否小于最高位地址。若是，进入 2；反之输出 `ERR`。

2. 通过地址到元素的映射找到该地址落于哪个元素之内。

3. 然后就和操作 3 一样，遍历元素的成员，找到地址在哪个成员中，记录下成员名称。

4. 判断地址合法性，若地址处于为了满足**对齐规则**而留下的空洞中，这时应该输出 `ERR`；反之进入 5。

5. 若此时元素类型为**基本元素**，则进入 6；反之重复 3。

6. 将记录下来的成员名称用调用符连接，输出。

好像比较复杂，其实和操作 3 差不了多少。

具体代码如下：

```cpp
//访问某个地址的元素
string Visit_Addr(ll addr){
    if(addr>=Addr_Pos)return "ERR";//判断地址是否在某个元素中
    Element ele;
    map<pr,Element*>::iterator it=Addr_To_Ele.begin();
    for(;it!=Addr_To_Ele.end();it++){//寻找地址所处的元素
        if(addr<(*it).first.first or addr>(*it).first.second)continue;
        ele=*((*it).second);
        break;
    }
    ll pos_goal=addr-ele.Address,pos_s=0,pos_t;//目标地址、起始地址、终止地址
    Type type=ele.Ele_Type;//当前元素类型
    string ele_name;//元素名称
    ele_name.clear();
    ele_name+=ele.Name;//元素名称先加上最外层元素名称
    while(!type.Member_Name.empty()){//循环直到元素类型为基本类型(此时元素类型没有成员)
        vector<Type*>::iterator it1=type.Member_Type.begin();//遍历当前元素类型的成员类型
        vector<string>::iterator it2=type.Member_Name.begin();//遍历当前元素类型的成员名称
        for(;it1!=type.Member_Type.end();it1++,it2++){
            pos_t=pos_s+(*it1)->Memory_Size;//更新终止地址
            if(pos_goal<pos_t and pos_goal>=pos_s){//如果目标地址在此成员中
                ele_name+='.'+*it2;//更新元素名称
                type=**it1;//更新元素类型
                //这两行代码需要注意：不可调换位置
                //因为 it2 是 type 的迭代器,type 更改后,it2 也会相应改变
                //因此需要在改变 type 之前调用 it2
                break;
            }
            else{//如果目标地址不在此成员中
                if(it1+1==type.Member_Type.end())return "ERR";//如果这个成员是最后一个成员了,说明目标地址为空洞
                ll Align=(*(it1+1))->Memory_Align;//该成员的对齐要求
                if(pos_t%Align)pos_t=(pos_t/Align+1)*Align;//如果终止地址不满足对齐规则
                if(pos_goal<pos_t)return "ERR";//如果目标地址在满足对齐规则后处于此成员内了,那么说明目标地址为空洞
                pos_s=pos_t;//更新起始位置
            }
        }
    }
    if(ele_name=="")return "ERR";//特判,若名称为空,则说明不存在元素包含这个地址
    return ele_name;
}
```

### 9. 框架

这大概是全代码中最简单的地方了。

具体代码如下：

```cpp
//工作
void work(){
    scanf("%lld",&n);//输入 n
    while(n--){
        scanf("%lld",&op);//输入操作类型
        if(op==1){//操作 1
            cin>>s>>k;
            for(int i=1;i<=k;i++)cin>>in1[i]>>in2[i];
            Type_Create(s,k,in1,in2);
            cout<<Def_Type[Type_Num].Memory_Size<<" "<<Def_Type[Type_Num].Memory_Align<<"\n";
        }
        else if(op==2){//操作 2
            cin>>ti>>ni;
            Ele_Create(ti,ni);
            cout<<Def_Ele[Ele_Num].Address<<"\n";
        }
        else if(op==3){//操作 3
            cin>>s;
            cout<<Visit_Ele(s)<<"\n";
        }
        else if(op==4){//操作 4
            cin>>addr_in;
            cout<<Visit_Addr(addr_in)<<"\n";
        }
    }
}
```

### 10. 间言二

那么到这里，所有的操作就都已经讲完了。

这时，只需要把刚刚实现的代码拼起来就好了。

最后，别忘了塞进主函数里：

```cpp
//主函数
int main(){
    init();
    work();
    return 0;
}
```

**注意：洛谷提交不需要写 `freopen`，但是考试时需要哦。**

## 代码总览

```cpp
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll,ll> pr;
const int MAXN=256;
ll max(ll x,ll y){return x>y?x:y;}
ll min(ll x,ll y){return x<y?x:y;}
pr mp(ll x,ll y){return (pr){x,y};}
//用来输入的变量
ll n,op,k,addr_in;
string s,ti,ni,in1[MAXN],in2[MAXN];
//类型结构体
struct Type{
    string Name;//类型名称
    vector<Type*> Member_Type;//类型成员类型
    vector<string> Member_Name;//类型成员元素
    ll Memory_Size;//类型占用内存大小
    ll Memory_Align;//类型对齐要求
    void clear(){
        Name.clear();
        Member_Type.clear();
        Member_Name.clear();
        Memory_Align=Memory_Size=0;
    }
};
Type Def_Type[MAXN];//已被定义过的类型
ll Type_Num;//已被定义过的类型数量
map<string,Type*> Name_To_Type;//名称到类型的映射
//元素结构体
struct Element{
    Type Ele_Type;//元素类型
    string Name;//元素名称
    ll Address;//元素起始地址
    void clear(){
        Ele_Type.clear();
        Name.clear();
        Address=0;
    }
};
Element Def_Ele[MAXN];//已被定义过的元素
ll Ele_Num;//已被定义过的元素数量
map<string,Element*> Name_To_Ele;//名称到元素的映射
//地址
ll Addr_Pos;//已分配到的地址位置
map<pr,Element*> Addr_To_Ele;//地址到元素的映射
//函数
void Nothing();//一个不知道干什么用也没有存在感的空函数
void init();//预处理
void Type_Create(string,ll,string*,string*);//创建一个类型的函数
void Ele_Create(string,string);//创建一个元素的函数
ll Visit_Ele(string);//访问某个元素的函数
string Visit_Addr(ll);//访问某个地址的元素
void work();//工作

//主函数
int main(){
    init();
    work();
    return 0;
}

//创建一个类型的函数
void Type_Create(string type_name,ll num,string *ar1,string *ar2){
    Type New_Type;//创建一个新类型
    New_Type.clear();
    New_Type.Name=type_name;//名字直接赋值
    for(int i=1;i<=num;i++){
        New_Type.Member_Type.push_back(Name_To_Type[ar1[i]]);//成员类型直接赋值
        New_Type.Member_Name.push_back(ar2[i]);//成员名称直接赋值
    }
    ll pos=0;//起始地址默认为 0
    vector<Type*>::iterator it=New_Type.Member_Type.begin();
    for(;it!=New_Type.Member_Type.end();it++){//遍历成员
        ll Align=(*it)->Memory_Align;//成员对齐要求
        ll Size=(*it)->Memory_Size;//成员大小
        New_Type.Memory_Align=max(New_Type.Memory_Align,Align);//类型的对齐要求为其成员中的最大对齐要求
        if(pos%Align)pos=(pos/Align+1)*Align;//如果起始地址不满足对齐规则
        pos+=Size;//下一个成员的起始地址(这个成员的终止地址)
    }
    if(pos%New_Type.Memory_Align)
        pos=(pos/New_Type.Memory_Align+1)*New_Type.Memory_Align;//如果终止地址不满足对齐规则
    New_Type.Memory_Size=pos;//终止地址减去起始地址即为大小(起始地址默认为 0)
    Def_Type[++Type_Num]=New_Type;//别忘了维护这个数组
    Name_To_Type[type_name]=&Def_Type[Type_Num];//别忘了维护这个映射
}

//创建一个元素的函数
void Ele_Create(string type_name,string ele_name){
    Element New_Ele;//创建一个新元素
    New_Ele.clear();
    ll Align=Name_To_Type[type_name]->Memory_Align;//该元素的类型的对齐要求
    ll Size=Name_To_Type[type_name]->Memory_Size;//该元素的大小
    if(Addr_Pos%Align)Addr_Pos=((Addr_Pos/Align+1)*Align);//若起始位置不满足对齐规则
    New_Ele.Address=Addr_Pos;//起始地址赋值
    New_Ele.Ele_Type=*Name_To_Type[type_name];//通过映射找到该类型,赋值
    New_Ele.Name=ele_name;//名称直接赋值
    Def_Ele[++Ele_Num]=New_Ele;//别忘了维护这个数组
    Name_To_Ele[ele_name]=&Def_Ele[Ele_Num];//别忘了维护这个映射
    Addr_To_Ele[mp(Addr_Pos,Addr_Pos+Size-1)]=&Def_Ele[Ele_Num];//将元素的起始位置和终止位置作为键值加入元素
    Addr_Pos+=Size;//更新最高位地址
}

//访问某个元素的函数
ll Visit_Ele(string ele_name){
    queue<string> name;//存储名称的队列
    string tool;//如其名
    tool.clear();
    for(int i=0;i<(ll)ele_name.length();i++){//处理名称
        if(ele_name[i]=='.'){//如果遇上了调用符
            name.push(tool);
            tool.clear();
        }
        else tool+=ele_name[i];
    }
    name.push(tool);
    ll pos=Name_To_Ele[name.front()]->Address;//起始地址为最外层元素的起始地址
    Type type=Name_To_Ele[name.front()]->Ele_Type;//最外层元素的类型
    name.pop();
    while(!name.empty()){
        string Name=name.front();//取出队首
        name.pop();
        vector<string>::iterator it1=type.Member_Name.begin();//遍历成员名称
        vector<Type*>::iterator it2=type.Member_Type.begin();//遍历成员类型
        for(;it1!=type.Member_Name.end();it1++,it2++){
            if(pos%(*it2)->Memory_Align)
                pos=(pos/(*it2)->Memory_Align+1)*(*it2)->Memory_Align;//如果起始地址不满足对齐规则
            if(*it1==Name){//如果找到了新队首
                type=**it2;
                break;
            }
            else pos+=(*it2)->Memory_Size;//更新起始地址
        }
    }
    return pos;
}

//访问某个地址的元素
string Visit_Addr(ll addr){
    if(addr>=Addr_Pos)return "ERR";//判断地址是否在某个元素中
    Element ele;
    map<pr,Element*>::iterator it=Addr_To_Ele.begin();
    for(;it!=Addr_To_Ele.end();it++){//寻找地址所处的元素
        if(addr<(*it).first.first or addr>(*it).first.second)continue;
        ele=*((*it).second);
        break;
    }
    ll pos_goal=addr-ele.Address,pos_s=0,pos_t;//目标地址、起始地址、终止地址
    Type type=ele.Ele_Type;//当前元素类型
    string ele_name;//元素名称
    ele_name.clear();
    ele_name+=ele.Name;//元素名称先加上最外层元素名称
    while(!type.Member_Name.empty()){//循环直到元素类型为基本类型(此时元素类型没有成员)
        vector<Type*>::iterator it1=type.Member_Type.begin();//遍历当前元素类型的成员类型
        vector<string>::iterator it2=type.Member_Name.begin();//遍历当前元素类型的成员名称
        for(;it1!=type.Member_Type.end();it1++,it2++){
            pos_t=pos_s+(*it1)->Memory_Size;//更新终止地址
            if(pos_goal<pos_t and pos_goal>=pos_s){//如果目标地址在此成员中
                ele_name+='.'+*it2;//更新元素名称
                type=**it1;//更新元素类型
                //这两行代码需要注意：不可调换位置
                //因为 it2 是 type 的迭代器,type 更改后,it2 也会相应改变
                //因此需要在改变 type 之前调用 it2
                break;
            }
            else{//如果目标地址不在此成员中
                if(it1+1==type.Member_Type.end())return "ERR";//如果这个成员是最后一个成员了,说明目标地址为空洞
                ll Align=(*(it1+1))->Memory_Align;//该成员的对齐要求
                if(pos_t%Align)pos_t=(pos_t/Align+1)*Align;//如果终止地址不满足对齐规则
                if(pos_goal<pos_t)return "ERR";//如果目标地址在满足对齐规则后处于此成员内了,那么说明目标地址为空洞
                pos_s=pos_t;//更新起始位置
            }
        }
    }
    if(ele_name=="")return "ERR";//特判,若名称为空,则说明不存在元素包含这个地址
    return ele_name;
}

//预处理
void init(){
    Def_Type[1].Name="byte";
    Def_Type[2].Name="short";
    Def_Type[3].Name="int";
    Def_Type[4].Name="long";
    Def_Type[1].Memory_Align=Def_Type[1].Memory_Size=1;
    Def_Type[2].Memory_Align=Def_Type[2].Memory_Size=2;
    Def_Type[3].Memory_Align=Def_Type[3].Memory_Size=4;
    Def_Type[4].Memory_Align=Def_Type[4].Memory_Size=8;
    Name_To_Type["byte"]=&Def_Type[1];
    Name_To_Type["short"]=&Def_Type[2];
    Name_To_Type["int"]=&Def_Type[3];
    Name_To_Type["long"]=&Def_Type[4];
    Type_Num=4;
}

//工作
void work(){
    scanf("%lld",&n);//输入 n
    while(n--){
        scanf("%lld",&op);//输入操作类型
        if(op==1){//操作 1
            cin>>s>>k;
            for(int i=1;i<=k;i++)cin>>in1[i]>>in2[i];
            Type_Create(s,k,in1,in2);
            cout<<Def_Type[Type_Num].Memory_Size<<" "<<Def_Type[Type_Num].Memory_Align<<"\n";
        }
        else if(op==2){//操作 2
            cin>>ti>>ni;
            Ele_Create(ti,ni);
            cout<<Def_Ele[Ele_Num].Address<<"\n";
        }
        else if(op==3){//操作 3
            cin>>s;
            cout<<Visit_Ele(s)<<"\n";
        }
        else if(op==4){//操作 4
            cin>>addr_in;
            cout<<Visit_Addr(addr_in)<<"\n";
        }
    }
}
```

# 尾言

这个题目我在考后很快就写出来了，但是在考场中并没有写出来，十分令人沮丧。

总体而言，这个题目并没有很复杂的设定或是逻辑，繁琐的地方也可以很容易地解决，难度是远远比不上猪国杀的。

其实对于大模拟，无非就两种情况：

1. 很快写好了。

2. 到处报段错误，然后一直调不出。

其实做到第一种并不难，前提是我们需要一个清醒的大脑，并且需要时刻保持清晰的逻辑，明白自己该做什么。

切忌糊里糊涂定义一大堆数组映射然后无脑胡。

这就是为什么考场里面我没有写出这一题——我看到题面之后思维并不是很清醒。

虽然作为一个考生，我很想骂一句：大模拟取似行不行！

但从理性的角度分析，我个人认为这是一道很好的模拟题，因为它既没有繁琐的题面，也没有毒瘤的设定，也没有通过堆叠要素来增加难度，同时想法也很好，实现的过程也并不枯燥，而且考场实现也具有一定难度。

总体来说，写下来以后，感觉是很爽的。

话说这次 CSP-S，不知有多少考生被这道大模拟直接打退役。

我在此想对这些人，以及所有人说：

不管是作为一个 OIer，还是作为一个人。

不管是在 OI 中，还是生活中。

如果头脑混沌、思路不清，就将到处是 `ERROR`，处处报段错，寸步难行。

只有保持清晰的想法，才能前进。

只有明白自己要做什么，才能成功。

在此，祝好在这次 CSP 中退役的选手们，希望你们在接下来的 whk 生活中顺利。

祝贺在这次 CSP 中获奖的选手们，希望你们在接下来的 OI 生涯中再接再厉。

------------

这大概是本蒟蒻写过的最长的一篇题解了，大家能看到这里也实属不易。

由于本题解篇幅较长，因此可能出现表述不清或错误的情况，请在评论区指出，或私信本人，感激不尽。

希望大家看得开心！