# -*- coding: utf-8 -*-
import os
path = 'DIV2K_train_HR'
num = 1

for file in os.listdir(path):
    nn = str(num).zfill(4)
    os.rename(os.path.join(path,file),os.path.join(path,nn+".png"))
    num+=1

