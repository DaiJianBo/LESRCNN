from PIL import Image
import os
# path = 'DIV2K_train_HR'
path = 'qietu'
file_list = os.listdir(path)
for file in file_list:
    I = Image.open(path+"/"+file)
    L = I.convert('L')
    L.save(path+"/"+file)
    print(file)