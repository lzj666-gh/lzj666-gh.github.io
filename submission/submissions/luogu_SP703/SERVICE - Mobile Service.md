# SERVICE - Mobile Service

## 题目描述

 A company provides service for its partners that are located in different towns. The company has three mobile service staff employees. If a request occurs at some location, an employee of the service staff must move from his current location to the location of the request (if no employee is there) in order to satisfy the request. Only one employee can move at any moment. They can move only on request and are not allowed to be at the same location. Moving an employee from location p to location q incurs a given cost C(p,q). The cost function is not necessarily symmetric, but the cost of not moving is 0, i.e. C(p,p)=0. The company must satisfy the received requests in a strict first-come, first-serve basis. The goal is to minimize the total cost of serving a given sequence of requests.

 Task

 You are to write a program that decides which employee of the service staff is to move for each request such that the total cost of serving the given sequence of requests is as small as possible.

## 输入格式

 The first line of input contains the number of test cases - nTest. Each test case contains:

 The first line of each test cases contains two integers, L and N. L (3 <= L <= 200) is the number of locations and N (1 <= N <= 1000) is the number of requests. Locations are identified by the integers from 1 to L. Each of the next L lines contains L non-negative integers. The jth number in the line i+1 is the cost C(i,j), and it is less than 2000.

 The last of each test cases contains N integers, the list of the requests. A request is identified by the identifier of the location where the request occurs. Initially, the three service staff employees are located at location 1, 2 and 3, respectively.

## 输出格式

 For each test case write the minimal total cost in a separate line.

## 时空限制

时间限制: 2448 ms
内存限制: 1500 MB
