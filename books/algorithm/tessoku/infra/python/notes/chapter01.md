# Chapter01
## 01 The First Problem
### Properties
- [Task](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_a)
- [Answer](https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap01/answer_A01.py)
```
問題文
整数 
N が与えられるので、一辺の長さが 
N であるような正方形の面積を出力するプログラムを作成してください。

制約
N は 
1 以上 
100 以下の整数
```
### Note
**入力の受け取り方**
```
# 単数の入力
N = int(input())
```

## 02 Linear Search
### Properties
- [Task](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_b)
- [Answer](https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap01/answer_A02.py)
```
問題文
N 個の整数A List の中に、整数 X が含まれるかどうかを判定するプログラムを作成してください。

制約
N は 1 以上 100 以下の整数
X は 1 以上 100 以下の整数
A は1 以上 100 以下の整数
```

### Note
**入力の受け取り方**
```
# 複数の入力
N, X = map(int, input().split())

# リストの入力
A = list(map(int, input().split()))
```

## 03 Two Cards
### Properties
- [Task](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_c)
- [Answer](https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap01/answer_A03.py)

### Note
**計算量**
```
O(N2)
100^2 = 10^4
```

## 04 Binary Representation
### Properties
- [Task](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_d)
- [Answer](https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap01/answer_A04.py)

### Note
**解き方**
A: 入力から２で割っていく
入力 % 2 = 余り兼2進数の変換値
1. 13 % 2 = 1
2. 6 % 2 = 0
3. 3 % 2 = 1 
4. 1 % 2 = 1
0になるまで行い、`1101`　と２進数になる


B: 2進数の大きい桁数から特定の数Nを引き、
- マイナスにならなければ`1`で、Nは引かれた数になる
- マイナスになった場合`0`で、Nの値は変わらない

N - 2進数の桁数 = 2進数の変換値
1. 13 - 32 = 0
2. 13 - 16 = 0
3. 13 - 8  = 1
4. 5  - 4  = 1
5. 1  - 2  = 0
6. 1  - 1  = 1


出力の桁数が決まっている場合はBを使う


## 05 Three Cardsh
### Properties
- [Task](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_e)
- [Answer](https://github.com/E869120/kyopro-tessoku/blob/main/codes/python/chap01/answer_A05.py)
```
問題文
赤・青・白の 
3 枚のカードがあります。
太郎君は、それぞれのカードに 
1 以上 
N 以下の整数を書かなければなりません。
3 枚のカードの合計を 
K にするような書き方は何通りありますか。

制約
N は 
1 以上 
3000 以下の整数
K は 
3 以上 
9000 以下の整数
```
### Note
**アルゴリズムを考える前に計算量を考える**

全探索するとNの3乗でNが3000だから、
```
N^3 = 27 * 10^9
```
N^10より小さい数になる。
制限時間2秒は目安として大体10^7-8ぐらいが良い。

**解き方**
赤、青を全探索し、白の数が`1 <= X <= N` であればOK
計算量も
```
N^2 = 27 * 10^6
```
N^7より小さい数になるからOK
