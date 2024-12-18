// 従来の var での変数宣言すると、意図せぬ場所で変数を上書きしたり、一度宣言した変数を、
// 同じ変数名で宣言し直したりしてしまう問題がありました（再宣言）。
// それらの問題を解決するために、ES2015では新たにletとconstでの変数宣言が追加されました。


// let は変数の 上書き（再代入） は可能ですが、再宣言は不可能 です。varとは異なり、letその宣言よりも前に参照できません。
let hoge = "letで定義したよ";
console.log(hoge) // letで定義したよ が出力される
hoge = "値を変えたよ";
console.log(hoge); // 値を変えたよ　が出力される
// let hoge = "再宣言するよ" //error


// const は変数の上書き（再代入）、再宣言が不可能です。letとは違って、初期化（値の代入）が必須です。
const fuga = "定数だよ";
console.log(fuga); // 定数だよ　が出力される
// fuga = "再代入するよ";  //error
// const fuga = "もっかい宣言するよ"; //error
