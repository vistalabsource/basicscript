# Basc
自分で作った学習/入門用スクリプト言語です。
基本的にPythonで機能を拡張します。
# 機能
主に
- 変数
- if文
- 関数定義・呼び出し
- 繰り返し（for, while)
- リスト
- 例外処理（try-catch, throw)
- モジュール（この言語の目玉機能）
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
```

# モジュール機能
この言語の一番の特徴です。
Pythonでモジュールを自作してBascの機能を拡張できます
※注意：Pythonでモジュールを自作する場合、必ずpylibという名前のディレクトリを作成して、その中にPythonスクリプトを入れてください。

以下、基本的な機能です。
``` python
def add(x, y):
    return x + y
exports {
    'add' : add # exports以外の名前だとインクルードできない。
}
```
```
include ファイル名;

write(add(1 + 1));
// -> 2
```


