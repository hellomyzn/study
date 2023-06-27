import tkinter as tk

class Application(tk.Frame):
    # masterを元にして設定していく
    def __init__(self, master=None):
        super().__init__(master)

        # ボタンとかの表示をうまくやってくるもの
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # ボタンのオブジェクトを生成
        self.hi_there = tk.Button(self)
        # テキストを挿入
        self.hi_there["text"] = "Hello World\n(click me)"
        # クリックされた時の処理を追加
        self.hi_there["command"] = self.say_hi
        # トップに持ってきている
        self.hi_there.pack(side="top")

        # ボタンを生成
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        # bottomに配置する
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

# tkのインスタンスを生成
root = tk.Tk()
# tkのインスタンスを引数で渡してる
app = Application(master=root)
# アプリをスタートしている
app.mainloop()
