import images

# es9(W, H, x, y, w, h, colore, pieno)

def cf(W, H):
    img = []
    for _ in range(H):
        row = []
        for _ in range(W):
            row.append((255, 255, 255))
            
        img.append(row)
        
    return img
        
def f(img, x, y, w, h, color, fill):
    H = len(img)
    W = len(img[0])
    
    for i in range(y, y+h):
        for j in range(x, x+w):
            
            if 0<=i<H and 0<=j<W:
                if fill or i == y or i == y + h - 1 or j == x or j == x + w - 1:
                    img[i][j] = color
                    
    return img
    
imgwhite = cf(10, 10)
images.save(imgwhite, "imgwhite.png")

imgrectangle = f(images.load("imgwhite.png"), 2, 2, 7, 3, (0, 0, 0), True)
images.save(imgrectangle, "imgwhite.png")