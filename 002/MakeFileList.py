# モジュールのインポート
import csv
import datetime
import os
import shutil
import tkinter
import tkinter.filedialog
import tkinter.messagebox
# OSの判別
osName = os.name
osDic = {'nt':('\\','\r\n'),'posix':('/','\n')}
separater = osDic[osName][0]
terminater = osDic[osName][1]

# フォルダ選択ダイアログの表示
root = tkinter.Tk()
root.withdraw()
fTyp = [("","*")]
iDir = os.getcwd()
#tkinter.messagebox.showinfo('ファイルリストを作りたいディレクトリを選択してください！')

# 処理ディレクトリパスの出力
Path = tkinter.filedialog.askdirectory(initialdir = iDir, title="FileListを作りたいディレクトリを選んでください")

NameList = os.listdir(Path)

table1 =[]
table1.extend([Path,"Files or Dir.s",len(NameList)])
table2 =[]
table2.extend(["No","File Name","Click here to open","Dir to copy"])

Filelist= []
for i in range(len(NameList)):
    Filelist.append([i+1, NameList[i],'=hyperlink("{0}{1}"&B{2})'.format(Path, separater,str(i+3)),''])
    

with open("FileList.csv","w") as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(table1)
    writer.writerow(table2)
    writer.writerows(Filelist)

#now = datetime.datetime.now()
#Filename = 'FileList{0:%Y%m%d%H%M}.xlsx'.format(now)#FileListYYYY㎜ddHHMM.xlsx
    

#os.rename("FileList.csv", Filename)

root.filename =  tkinter.filedialog.asksaveasfilename(initialdir = Path,title = "serect a directry to save Filelist", initialfile = "FileList.csv", filetypes = (("csv","*.csv"),("xlsx","*.xlsx"),("all files","*.*")))
shutil.move(os.getcwd() + '/FileList.csv', root.filename)

#tkinter.messagebox.showinfo('''
#    {0} OK
#    このあとFileCopy.pyを実行する場合は出来た FileListxxxxxxxx.xlsx のD列に
#    コピー先のディレクトリ名を入力し、ファイル名を FiliList.xlsx としてください
#    '''.format(root.fimename))
