# P11019 题解

官方题解（（（

考虑到我们实际上输出的是第一个 `]` 号之前的所有大写字母转为小写字母的结果，因此直接写出下面的代码（仅给出关键部分）：

```cpp
string s;
void main(){
  cin>>s;
  putchar('/');
  for(auto i:s)
    if(i==']') break;
    else if(isupper(i)) putchar(i-'A'+'a');
}
```

其中 `isupper` 这个函数是用于判断一个字符是否为大写字母，`putchar` 函数则是用于输出一个 `char`。