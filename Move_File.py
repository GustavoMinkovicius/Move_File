import os
import shutil

path = input ('Qual é o caminho até a pasta?')
lista = os.listdir(path)
for i in lista:
    name,ext = os.path.splitext(i)
    ext = ext[1:]
    if ext == '':
        continue
    if os.path.exists(path+'/'+ext):
        print("Movendo arquivos")
        shutil.move(path+'/'+ i, path+'/'+ext+'/'+i)
    else: 
        os.mkdir(path+'/'+ext)
        shutil.move(path+'/'+ i, path+'/'+ext+'/'+i)