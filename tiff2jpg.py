# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 17:12:47 2018

@author: 455495
"""

import sys
import os
from os.path import isfile, join, splitext
from PIL import Image, ImageSequence


if __name__ == "__main__":
    
    if len(sys.argv)>1:
        root = sys.argv[1:][0] 
    else:
        root = "./"
    
    files = [f for f in os.listdir(root) if (isfile(join(root,f)) and '.tif' in f)]
    
    for f in files:
        outfilename, _ = splitext(f)
        img = Image.open(f)

        i = 0
        while True:
            try:
                img.seek(i)
                img.thumbnail(img.size)
                img.save("%s_page%d.jpg"%(outfilename,i), "JPEG", quality=100)
                i +=1
            except Exception, e:
                break
            
        print "%s page(s) derived from %s" % (i, f)
 
        


    
    
        
    
    
    