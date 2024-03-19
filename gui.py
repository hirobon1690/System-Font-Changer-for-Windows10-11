import customtkinter as ctk
import tkinter.filedialog
import tkinter as tk
import subprocess
import ttc2ttf

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("700x800")
        self.title("System Font Changer for Windows 10/11")

        self.weight_ja=["Bold", "Semibold", "Regular", "Semilight", "Light"]
        self.weight_en=["Black", "Black Italic", "Bold", "Bold Italic", "Semibold","Semibold Italic", "Regular", "Italic", "Semilight","Semilight Italic" ,"Light", "Light Italic", "Variable"]
        self.frame=[]
        self.label=[]
        self.entry=[]
        self.button=[]
        self.tab=[]
        
        
        self.frame.append(ctk.CTkFrame(self))
        self.frame[0].pack(fill="y", expand=True, side="top")
        self.tabview = ctk.CTkTabview(master=self.frame[0])
        self.tabview.pack(padx=20, pady=20)
        
        self.tab.append(self.tabview.add("STEP 1"))
        self.tab.append(self.tabview.add("STEP 2"))
        self.tab.append(self.tabview.add("STEP 3"))
        self.tab.append(self.tabview.add("STEP 4"))
        self.tab.append(self.tabview.add("ABOUT"))
        
        for i in range(5):
            self.label.append(ctk.CTkLabel(self.tab[1], text=self.weight_ja[i], fg_color="transparent"))
            self.label[i].grid(row=i+1,column=0, padx=10, pady=10)
            
            self.entry.append(ctk.CTkEntry(self.tab[1], width=300))
            self.entry[i].grid(row=i+1,column=1, padx=10)
            
            self.button.append(ctk.CTkButton(self.tab[1], text="参照"))
            self.button[i].bind("<Button-1>", lambda e, i=i: self.open_file_dialog(i))
            self.button[i].grid(row=i+1,column=2, padx=10)
            
        for i in range(13):
            self.label.append(ctk.CTkLabel(self.tab[2], text=self.weight_en[i], fg_color="transparent"))
            self.label[i+5].grid(row=i+1,column=0, padx=10, pady=10)
            
            self.entry.append(ctk.CTkEntry(self.tab[2], width=300))
            self.entry[i+5].grid(row=i+1,column=1, padx=10)
            
            self.button.append(ctk.CTkButton(self.tab[2], text="参照"))
            self.button[i+5].bind("<Button-1>", lambda e, i=i+5: self.open_file_dialog(i))
            self.button[i+5].grid(row=i+1,column=2, padx=10)
            
        
        self.button2 = ctk.CTkButton(self.tab[1], text="生成", command=self.run_script)
        self.button2.grid(row=6,column=0, padx=10, pady=20)
        
        self.button3 = ctk.CTkButton(self.tab[2], text="生成", command=self.run_segoe)
        self.button3.grid(row=14,column=0, padx=10, pady=20)
        ctk.CTkLabel(self.tab[0], text="本プログラムを使用して生じたいかなる問題も作成者(@hirobon1690)は責任を負いません．", fg_color="transparent").pack(pady=10)
        ctk.CTkLabel(self.tab[0], text="必ず大事なデータのバックアップ・復元ポイントを作成してから操作を行ってください．", fg_color="transparent").pack(pady=10)
        
        self.label1 = ctk.CTkLabel(self.tab[0], text="もとのフォントのバックアップを作成します．以下のボタンをクリックしてください", fg_color="transparent")
        self.label1.pack(pady=10)
        self.button4 = ctk.CTkButton(self.tab[0], text="バックアップ", command=self.backup)
        self.button4.pack(pady=10)
        self.label2 = ctk.CTkLabel(self.tab[0], text="未実行", fg_color="transparent")
        self.label2.pack(pady=10)
        
        self.label3 = ctk.CTkLabel(self.tab[0], text="游ゴシックをttfに分割します．", fg_color="transparent")
        self.label3.pack(pady=10)
        self.button4 = ctk.CTkButton(self.tab[0], text="分割", command=self.ttc2ttf)
        self.button4.pack(pady=10)
        self.label4 = ctk.CTkLabel(self.tab[0], text="未実行", fg_color="transparent")
        self.label4.pack(pady=10)

        ctk.CTkLabel(self.tab[1], text="Yu Gothic UIと置き換えたいフォントを選択してください．", fg_color="transparent").grid(row=0,column=0, columnspan = 3)
        ctk.CTkLabel(self.tab[2], text="Segoe UIと置き換えたいフォントを選択してください．", fg_color="transparent").grid(row=0,column=0, columnspan = 3)

        ctk.CTkButton(self.tab[3], text="フォルダを開く", command=self.open_directory).pack(pady=10)
        ctk.CTkLabel(self.tab[3], text="delete_yugoth.cmdを右クリックして「管理者として実行」してください", fg_color="transparent").pack(pady=10)
        ctk.CTkLabel(self.tab[3], text="delete_segoe.cmdを右クリックして「管理者として実行」してください", fg_color="transparent").pack(pady=10)
        ctk.CTkLabel(self.tab[3], text="edit_registry.regをダブルクリックして実行してください", fg_color="transparent").pack(pady=10)
        ctk.CTkLabel(self.tab[3], text="outputフォルダにあるすべてのフォントを選択して「すべてのユーザーにインストール」してください", fg_color="transparent").pack(pady=10)
        ctk.CTkLabel(self.tab[3], text="上記の操作が完了後，再起動してください", fg_color="transparent").pack(pady=10)
        
        ctk.CTkLabel(self.tab[4], text="System Font Changer for Windows 10/11", fg_color="transparent").pack(pady=10)
        ctk.CTkLabel(self.tab[4], text="https://github.com/hirobon1690/System-Font-Changer-for-Windows10-11", fg_color="transparent").pack(pady=10)
        ctk.CTkLabel(self.tab[4], text="Contact me on Twitter @hirobon1690", fg_color="transparent").pack(pady=10)
        
    def open_file_dialog(self, i):
        print(i)
        filename = tkinter.filedialog.askopenfilename()
        print(f"Selected file: {filename}")
        self.entry[i].insert(0, filename)
        
        
    def run_script(self):
        subprocess.run(["C:\\Program Files (x86)\\FontForgeBuilds\\bin\\ffpython.exe", "main.py","./source/yugoth/Bold.ttf", self.entry[0].get(), "./output/YuGothicUI-Bold.ttf"])
        subprocess.run(["C:\\Program Files (x86)\\FontForgeBuilds\\bin\\ffpython.exe", "main.py","./source/yugoth/Semibold.ttf", self.entry[1].get(), "./output/YuGothicUI-Semibold.ttf"])
        subprocess.run(["C:\\Program Files (x86)\\FontForgeBuilds\\bin\\ffpython.exe", "main.py","./source/yugoth/Regular.ttf", self.entry[2].get(), "./output/YuGothicUI-Regular.ttf"])
        subprocess.run(["C:\\Program Files (x86)\\FontForgeBuilds\\bin\\ffpython.exe", "main.py","./source/yugoth/Semilight.ttf", self.entry[3].get(), "./output/YuGothicUI-Semilight.ttf"])
        subprocess.run(["C:\\Program Files (x86)\\FontForgeBuilds\\bin\\ffpython.exe", "main.py","./source/yugoth/Light.ttf", self.entry[4].get(), "./output/YuGothicUI-Light.ttf"])
        print("done")
        
    def run_segoe(self):
        subprocess.run(["C:\\Program Files (x86)\\FontForgeBuilds\\bin\\ffpython.exe", "main.py","./source/segoe/Black.ttf", self.entry[5].get(), "./output/SegoeUI-Black.ttf"])
        subprocess.run(["C:\\Program Files (x86)\\FontForgeBuilds\\bin\\ffpython.exe", "main.py","./source/segoe/BlackItalic.ttf", self.entry[6].get(), "./output/SegoeUI-BlackItalic.ttf"])
        subprocess.run(["C:\\Program Files (x86)\\FontForgeBuilds\\bin\\ffpython.exe", "main.py","./source/segoe/Bold.ttf", self.entry[7].get(), "./output/SegoeUI-Bold.ttf"])
        subprocess.run(["C:\\Program Files (x86)\\FontForgeBuilds\\bin\\ffpython.exe", "main.py","./source/segoe/BoldItalic.ttf", self.entry[8].get(), "./output/SegoeUI-BoldItalic.ttf"])
        subprocess.run(["C:\\Program Files (x86)\\FontForgeBuilds\\bin\\ffpython.exe", "main.py","./source/segoe/Semibold.ttf", self.entry[9].get(), "./output/SegoeUI-Semibold.ttf"])
        subprocess.run(["C:\\Program Files (x86)\\FontForgeBuilds\\bin\\ffpython.exe", "main.py","./source/segoe/SemiboldItalic.ttf", self.entry[10].get(), "./output/SegoeUI-SemiboldItalic.ttf"])
        subprocess.run(["C:\\Program Files (x86)\\FontForgeBuilds\\bin\\ffpython.exe", "main.py","./source/segoe/Regular.ttf", self.entry[11].get(), "./output/SegoeUI-Regular.ttf"])
        subprocess.run(["C:\\Program Files (x86)\\FontForgeBuilds\\bin\\ffpython.exe", "main.py","./source/segoe/Italic.ttf", self.entry[12].get(), "./output/SegoeUI-Italic.ttf"])
        subprocess.run(["C:\\Program Files (x86)\\FontForgeBuilds\\bin\\ffpython.exe", "main.py","./source/segoe/Semilight.ttf", self.entry[13].get(), "./output/SegoeUI-Semilight.ttf"])
        subprocess.run(["C:\\Program Files (x86)\\FontForgeBuilds\\bin\\ffpython.exe", "main.py","./source/segoe/SemilightItalic.ttf", self.entry[14].get(), "./output/SegoeUI-SemilightItalic.ttf"])
        subprocess.run(["C:\\Program Files (x86)\\FontForgeBuilds\\bin\\ffpython.exe", "main.py","./source/segoe/Light.ttf", self.entry[15].get(), "./output/SegoeUI-Light.ttf"])
        subprocess.run(["C:\\Program Files (x86)\\FontForgeBuilds\\bin\\ffpython.exe", "main.py","./source/segoe/LightItalic.ttf", self.entry[16].get(), "./output/SegoeUI-LightItalic.ttf"])
        # subprocess.run(["C:\\Program Files (x86)\\FontForgeBuilds\\bin\\ffpython.exe", "main.py","./source/segoe/Variable.ttf", self.entry[17].get(), "./output/SegoeUI-Variable.ttf"])
        print("done")
        
    def backup(self):
        self.label2.configure(text="実行中")
        subprocess.run(["copy", "C:\\Windows\\Fonts\\segoeui*.ttf", ".\\backup\\segoeui\\"],shell=True)
        self.label2.configure(text="50%...")
        subprocess.run(["copy", "C:\\Windows\\Fonts\\YuGoth*.ttc", ".\\backup\\yugoth\\"],shell=True)
        self.label2.configure(text="backupフォルダにバックアップが保存されたことを確認してください．")
    
    def ttc2ttf(self):
        self.label4.configure(text="0%...")
        ttc2ttf.ttc2ttf(".\\backup\\yugoth\\YuGothB.ttc", "./backup/yugoth/ttf/")
        self.label4.configure(text="25%...")
        ttc2ttf.ttc2ttf(".\\backup\\yugoth\\YuGothL.ttc", "./backup/yugoth/ttf/")
        self.label4.configure(text="50%...")
        ttc2ttf.ttc2ttf(".\\backup\\yugoth\\YuGothM.ttc", "./backup/yugoth/ttf/")
        self.label4.configure(text="75%...")
        ttc2ttf.ttc2ttf(".\\backup\\yugoth\\YuGothR.ttc", "./backup/yugoth/ttf/")
        subprocess.run(["copy", ".\\backup\\yugoth\\ttf\\YuGoth*_0.ttf", ".\\output\\"],shell=True)
        self.label4.configure(text="完了")
        
        
    def open_directory(self):
        subprocess.run(["explorer", ".\\"])
        
        
app = App()
app.mainloop()