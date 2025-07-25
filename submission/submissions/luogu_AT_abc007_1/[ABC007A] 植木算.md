# [ABC007A] 植木算

## 题目描述

[problemUrl]: https://atcoder.jp/contests/abc007/tasks/abc007_1

小学生のたかはし君は、遠足で林にきています。遠足を楽しんでいる彼は、木が一直線に並んでいることに気づきました。 そして、授業で、「植木算」というものを習ったことを思い出しました。彼が授業で習った植木算の問題は、「木が $ 4 $ 本 一直線に並んでいるとき、隣り合う木の"間"は何箇所存在するか。」というもので、その答えは図1の通り $ 3 $ 箇所です。

 ![](https://cdn.luogu.com.cn/upload/vjudge_pic/AT_abc007_1/a11513331b08f5d8e107a10d2459fe55959a0c30.png) 図1. 4本の木の間は3箇所今回、遠足中の彼が見ている光景は、その問題のシチュエーションとよく似通っていて、隣り合う木の間の数を数えたくなりました。 彼は遠足パンフレットに、一直線に生えている木々の本数が書かれていることに気づきました。しかし、彼は実際に木の間を数える手段しか知らないので、本数によってはとても時間がかかってしまうかもしれません。

そこで、あなたにお願いがあります。 一直線に並んでいる木々が $ n $ 本あるという情報が与えられるので、隣り合う木の間の数を出力するプログラムをたかはし君のために作ってあげてください。

## 输入格式

入力は以下の形式で標準入力から与えられる。

> $ n $

- $ 1 $ 行目には、一直線に並んでいる木々の本数を表す整数 $ n\ (1\ ≦\ n\ ≦\ 10,000) $ が与えられる。

## 输出格式

隣り合う木の間の数を $ 1 $ 行に出力せよ。出力の末尾に改行をいれること。

## 提示

### Sample Explanation 1

問題文中で説明したケースであり、彼が授業で習った時の値設定です。

### Sample Explanation 2

100本並んでいるので、間は99箇所あります。

### Sample Explanation 3

$ 1 $ 本の木しかないので、$ 0 $ と出力してください。 !\[\](http://abc007.contest.atcoder.jp/img/abc/007/1-2.png) 図2. サンプル3の図(木が1本のケース)

## 时空限制

时间限制: 2000 ms
内存限制: 256 MB
