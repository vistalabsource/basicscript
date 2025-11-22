# Basc
自分で作った学習/入門用スクリプト言語です。
# 機能
主に
- 変数
- if文
- 関数定義・呼び出し
- 繰り返し（for, while)
- リスト
- 例外処理（try-catch, throw)
ざっくりいうとこんな感じです。

以下、サンプルコードです

# 変数
``` 
let x : "Hello, world!";
write(x);
```

# if文
``` 
let x : 5;
if x > 10
{
    write("gt10");
}
else if x > 3
{
    write("gt3");
}
else
{
    write("small");
}
  
```

# 関数定義・呼び出し
``` 
function add : x, y
{
    return x + y;
}

write(add(1, 1));
