import struct
import os,re


import win32ui

def initial():
    
    f = open('data.txt','w')
    f.write("")

def write(filename):
    filepath= filename
    binfile = open(filepath, 'rb') #打开二进制文件
    
    size = os.path.getsize(filepath) #获得文件大小    
  
    f = open('data.txt','a')
    for i in range(size):
        data = binfile.read(1) #每次输出一个字节
        num = struct.unpack('B',data)

        num = num[0]
        num = "%02X" % num
        temp =  str(num)      
        
        print(temp)
        f.write(temp)       
        
    binfile.close()
    
    
    f.close()

def getfilename():
    
    dlg = win32ui.CreateFileDialog(1)


    dlg.SetOFNInitialDir('C:/')


    dlg.DoModal()
    


    filename = dlg.GetPathName()

    return filename

if __name__ == '__main__':

    initial()

    filename1 = getfilename()
    filename2 = getfilename()


    
    write(filename1)
    write(filename2)



