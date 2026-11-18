#!/usr/bin/env python

import images

def im(W, H):
    img = []
    white = (255, 255, 255)
    
    for i in range(H):
        riga = []
        for j in range(W):
            riga.append(white)
        img.append(riga)
        
    return img

immagine = im(300, 300)
images.save(immagine, "test.png")

