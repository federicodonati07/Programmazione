import images

def f(img):
    H = len(img)
    W = len(img[0])
    
    for i in range(H):
        for j in range(W):
            for _ in range(len(img[i][j])):
                r = img[i][j][0]    
                g = img[i][j][1] 
                b = img[i][j][2]
                
                m = (r+g+b)//3
                
                gray = (m, m, m)
                
            img[i][j] = gray
            
    return img
    
img = f(images.load("img.png"))
images.save(img, "grayscale.png")