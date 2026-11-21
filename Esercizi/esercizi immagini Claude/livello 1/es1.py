import images

def f(W, H, color):
    img = []

    for _ in range(H):
        row = []
        for _ in range(W):
            row.append(color)
            
        img.append(row)
        
    print(img)
    return(img)

img = f(10, 8, (255, 0, 0))
images.save(img, "img1.png")
