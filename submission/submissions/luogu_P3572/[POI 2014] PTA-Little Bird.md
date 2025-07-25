# [POI 2014] PTA-Little Bird

## 题目描述

In the Byteotian Line Forest there are $n$ trees in a row.

On top of the first one, there is a little bird who would like to fly over to the top of the last tree.

Being in fact very little, the bird might lack the strength to fly there without any stop.

If the bird is sitting on top of the tree no. i, then in a single flight leg it can fly toany of the trees no. $i+1,i+2,\cdots,i+k$, and then has to rest afterward.

Moreover, flying up is far harder to flying down.  A flight leg is tiresome if it ends in a tree at leastas high as the one where is started.  Otherwise the flight leg is not tiresome.

The goal is to select the trees on which the little bird will land so that the overall flight is leasttiresome, i.e., it has the minimum number of tiresome legs.

We note that birds are social creatures, and our bird has a few bird-friends who would also like to getfrom the first tree to the last one.  The stamina of all the birds varies,so the bird's friends may have different values of the parameter $k$.

Help all the birds, little and big!

## 输入格式

There is a single integer $n$ ($2\le n\le 1\ 000\ 000$) in the first line of the standard input:

the number of trees in the Byteotian Line Forest.

The second line of input holds $n$ integers $d_1,d_2,\cdots,d_n$ ($1\le d_i\le 10^9$)separated by single spaces: $d_i$ is the height of the i-th tree.

The third line of the input holds a single integer $q$ ($1\le q\le 25$): the number of birds whoseflights need to be planned.

The following $q$ lines describe these birds: in the $i$-th of these lines, there is an integer $k_i$ ($1\le k_i\le n-1$) specifying the $i$-th bird's stamina. In other words, the maximum number of trees that the $i$-th bird can pass before it has to rest is $k_i-1$.


## 输出格式

Your program should print exactly $q$ lines to the standard output.

In the $i$-th line, it should specify the minimum number of tiresome flight legs of the $i$-th bird.


## 时空限制

时间限制: 1000 ms
内存限制: 512 MB
