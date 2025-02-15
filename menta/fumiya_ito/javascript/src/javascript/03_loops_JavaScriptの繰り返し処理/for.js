// for 文は、括弧で囲みセミコロンで区切った 3 つの引数と、ループ内で実行されるブロック文から成るループ(繰り返し処理)です。
// 初期化式で変数を初期化し、加算式で変数をループ毎に加算し、条件式の判定がfalseとなるまでブロック文をループします。

// for ([初期化式］;[条件式］;[加算式］) {
// // 繰り返す処理
// }

// 例1 for文内の処理が３回実行される
// for文：
for (let i = 0; i < 3; i++) {
  console.log(i);
}
/* 実行結果
      0
      1
      2
  */

// for文とbreak文
// for文・while文ループや switch 文を中断し、中断したブロック文の外へ処理を移します。

// for (let i = 0; i < 3; i++) {
//   if (条件式1) {
//     break;
//   }
// }

// 条件式1がtrueのとき、for文のループを抜ける
// 例1 break文で変数iが1のとき、ループを抜ける
for (let i = 0; i < 5; i++) {
  if (i === 1) {
    break;
  }
  console.log(i); // 0が出力される
}

// continue文
// for文やwhile文ループの中で、continue文に到達すると、ループ内のそれ以降の処理は行われず、ループの最初の処理から再び実行されます。

// for (let i = 0; i < 3; i++) {
//   if (条件式1) {
//     continue
//   }
//   console.log(i)
// }

// 条件式1がtrueのとき、continue文以降の処理は実行されない
// 例1: 変数iが3未満のとき、コンソール出力を行わない
for (let i = 0; i < 5; i++) {
  if (i < 3) {
    continue;
  }
  console.log(i + 1 + "回目の処理です");
}
/**
   4回目の処理です
   5回目の処理です
  */

//  for-of文
// 以下のように、文字列の値等をループ処理できます。
// for (変数 of 値) {
//   処理
// }

// 例1 文字列wordをループ処理し、各文字をコンソールに出力する
const word = "Hello";
for (let x of word) {
  console.log(x);
}
// 'H'
// 'e'
// 'l'
// 'l'
// 'o'
