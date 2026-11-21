import images

def f(img):
    
    H = len(img)
    W = len(img[0])
    
    for riga in img:
        if riga[0] not in riga[1:]:
            return False
        
    return True
    
    
img = f(images.load("img.png"))
print(img)