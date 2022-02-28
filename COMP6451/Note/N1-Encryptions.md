# Encryption

## 日期

+ 二〇二二·二·二三
+ 很晴☀
+ 温暖

## AES

### Keys

+ Share Key

## RSA

### Keys

+ Public Key

## Elliptic Curve

### Keys

+ Public Key
+ random $n$ (Private end )
+ random $r$ (Public end)
+ Private: $K_{priv} = n$
+ Public: $K = g^n$

### Encryption  

+ $E_K(m) = (g^r, m\circ K^r)$

### Decryption

+ $D_{K_{priv}}(x, y) = y\circ (x^n)^{-1}$

