# P1234 题解

作为欢乐赛第一题，自然没有什么难度，标程也是搜索没有优化。本质上完全可以归入入门题一类。附程序：

```delphi

const st='hehe';
var n,m,i,j,s:longint;a:array[1..1000,1..1000]of char;
function find(x,y,k:longint):longint;              //在(x,y)第k个字符开始搜第k+1个
begin                                      //a[x,y]:=’ ‘;全用来标记
  if k=4 then exit(1);
  find:=0;
  if x>1 then
  if a[x-1,y]=st[k+1] then
  begin
  a[x,y]:=' ';
  find:=find+find(x-1,y,k+1);
  end;
  if y>1 then
  if a[x,y-1]=st[k+1] then
  begin
  a[x,y]:=' ';find:=find+find(x,y-1,k+1);
  end;
  if x<n then
  if a[x+1,y]=st[k+1] then
  begin
  a[x,y]:=' ';find:=find+find(x+1,y,k+1);
  end;
  if y<m then
  if a[x,y+1]=st[k+1] then
  begin
  a[x,y]:=' ';find:=find+find(x,y+1,k+1);
  end;
  a[x,y]:=st[k];
end;
begin
  readln(n,m);
  for i:=1 to n do
  begin
  for j:=1 to m do
  read(a[i,j]);
  readln;
  end;
  s:=0;
  for i:=1 to n do                          //搜第一个h
  for j:=1 to m do
  if a[i,j]='h' then
  s:=s+find(i,j,1);
  writeln(s);
end.

```
貌似很长，缩一下行不到40.
