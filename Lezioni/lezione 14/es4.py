import images

def create_image(W, H):
    white = (255, 255, 255)
    img = []
    for _ in range(H):
        riga = []
        for _ in range(W):
            riga.append(white)
            
        img.append(riga)
        
    return img

def img_rettangolo(img, W, H, X, Y, colore, riempimento): # W e H sono le dimensioni del rettangolo da disegnare non di img
    for i in range(Y, Y+H):
        for j in range(X, X+W):
            img[i][j] = colore
            
    return img

img = create_image(10, 10)
images.save(img, "image.png")

imgr = img_rettangolo(img, 5, 5, 5, 1, (0, 0, 0), False)
images.save(imgr, "image.png")