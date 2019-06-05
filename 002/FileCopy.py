import os
import csv
import shutil
import datetime
import tkinter as tk
import tkinter.filedialog as fDialog
import tkinter.messagebox as mBox
# OSの判別
osName = os.name
osDic = {'nt':('\\','\r\n'),'posix':('/','\n')}
separater = osDic[osName][0]
terminater = osDic[osName][1]

root = tk.Tk()
root.withdraw()
#fTyp = [("","*")]
#iDir = os.path.abspath(os.path.dirname(__file__))
#mBox.showinfo(title = "" , message = 'あらかじめFileList.csvにコピー先を記入してください。')
Path = os.getcwd()

ListPath = fDialog.askopenfilename(initialdir = Path, title="FileList.csvを開きます") 
#FileNames = os.listdir(Path)
FileList =[]

with open(ListPath, 'r') as f:
    reader = csv.reader(f)

    for row in reader:
         FileList.append(row)
         #print(row)

number = len(FileList)-2

Path = FileList[0][0]
try:
    os.chdir(Path)
except TypeError:
    mBox.showerror(message="適切なFileList.csvではありません")
    quit()
except FileNotFoundError:
    mBox.showerror(message= "指定されたパスが見つかりません")
    quit()

for i in range(number):
    fileName = str(FileList[i+2][1])
    if os.path.exists(fileName) == 1:
        result = "exist"
        copyPath = "copy_Dir"
        if FileList[i+2][3] != '':
            copyPath =str(FileList[i+2][3])
        if os.path.exists(copyPath)==0:
            os.mkdir(copyPath)
            os.chmod(copyPath,0o777)
        try:
            shutil.copy(fileName,copyPath + separater +fileName)
            FileList[i+2].append(result)
            FileList[i+2].append('=hyperlink("' + Path +separater + copyPath+separater+fileName+'")')
        except PermissionError:
            result ="Directry is NOT copied"
            FileList[i+2].append(result)
            copyPath = result
        print(fileName + ">>" + copyPath)
        
    else:
        result = "NOT exist"
        print(fileName + " is " + result)
        FileList[i+2].append(result)

now = datetime.datetime.now()
logFile = 'FileCopyLog{0:%Y%m%d%H%M}'.format(now)#File name+YYYY㎜ddHHMM.xlsx
logFile = fDialog.asksaveasfilename(initialdir = Path,title = "select a directry to save copy log", initialfile = logFile, filetypes = (("csv","*.csv"),("xlsx","*.xlsx"),("all files","*.*")))

with open(logFile,"w") as f:
    writer = csv.writer(f, lineterminator=terminater)
    writer.writerows(FileList)

mBox.showinfo(tilte=None, message= '{0} is created'.format(logFile))
#mBox.Message(master='{0} OK'.format(logFile))

#print(logFile + " OK")
