import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WIN_CLOSED, InputText, Output
import search_beta
import translate_serch
from pygame import mixer
import tkinter
from tkinter import ttk
import sqlite3
root = tkinter.Tk()

#プログレスバー(非確定的)
pb = ttk.Progressbar(
    root,
    length="100",
    mode="indeterminate", #非確定的モード
    )
 #自動増加モード開始
pb.pack()
#テーマ
sg.theme('Black') 
#レイアウト
layout = [  [sg.Text('このソフトの利用はgoogleの規約に違反しているのであまり利用はお勧めできません')],
            [sg.Text('検索ワード', size=(15, 1)), InputText('', key='textbox', size=(30, 20))],
            [sg.Button('Start search', key='Search')],
            [sg.Text('検索件数1~20(必ず入力してください)'), InputText('', key='kensu', size=(3, 1))],
            [sg.Output(size=(80,20),)],
         ]
#window生成
window = sg.Window('スクレイピング', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: #ウィンドウのXボタンを押したときの処理
        window.close()
    if event == 'Search':
        pb.start()
        #効果音再生
        mixer.init()        #初期化
        mixer.music.load("E:\Python\plg3-7\メッセージ表示音1.mp3")
        mixer.music.play(3) #再生回数
        x = values['kensu'] 
        word = values['textbox'] 
        output = search_beta.serch_google(word, x) #元の言語で検索
        output2 = translate_serch.translate_google(word, x) #英語に翻訳して検索
        con = sqlite3.connect("scraping")
        print(output)
        print(output2)
        pb.stop()
        sqdbs = [output]
        try:
            con.executemany('INSERT INTO syain VALUES (?,?,?)',sqdbs)
        except sqlite3.Error as e:
                       con.commit()
                       con.close()












