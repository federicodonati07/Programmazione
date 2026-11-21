import images

def f(W, H, c1, c2):
    img = []
    for i in range(H):
        row = []
        for j in range(W):
            if (i+j)%2 == 0:
                row.append(c1)
                
            else:
                row.append(c2)
        img.append(row)
    return img
        
    
    
img = f(10, 10, (0, 0, 0), (0, 255, 0))
images.save(img, "chess.png")