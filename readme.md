# System Font Changer for Windows 10/11
## About
Windows 10/11のシステムフォントを強制的に変更する強力なツールです．  
他のツールでは変更不可能なシステムの深い部分のフォントを変更することができます．
![Noto Sans Japaneseに変更した例](https://github.com/hirobon1690/System-Font-Changer-for-Windows10-11/assets/58695125/6d1b0c0c-b1e5-4583-a868-89dc772aecb2)


## 免責
本ツールを使用することによって生じた不具合・故障などについてリポジトリの作成者は一切の責任を負わないもとのします．

## インストール
1. [FontForge](https://fontforge.org/en-US/)をインストールします．
2. [Python](https://www.python.org/)をインストールします．
3. 依存関係を以下の手順に従ってインストールします．
Powershellまたはコマンドプロンプトを開いて
```cmd
pip install customtkinter fontTools
```
4. このリポジトリをダウンロード(clone)します．

## 使い方
ダウンロードしたリポジトリのフォルダをPowershellまたはコマンドプロンプトで開いて
```cmd
python ./gui.py
```
ウィザードに従ってください．
![image](https://github.com/hirobon1690/System-Font-Changer-for-Windows10-11/assets/58695125/cbe34af7-1cc8-474b-a873-4663e8cf599f)


## 仕組み
オリジナルのシステムフォント（Yu Gothic UI, Segoe UI）のフォント名などのプロパティを完全にコピーしたフォントを生成し，オリジナルを置換することで根本的にフォントを置き換えています．

## 注意
使用するフォントのライセンス等に十分注意してください．
Sourceフォルダ内のフォントには触らないでください．
