#!/usr/bin/env python
import os 

with open("text.txt") as f:
    lines = f.read().splitlines()
    
    res = []
    for i in range(len(lines)):
        words = lines[i].split()
        res.append([])
        
        for w in words:
            res[i].append(w)
        
    res = [tuple(element) for element in res]
    
    res = sorted(res, key=lambda x: (-int(x[2]), x[0].lower(), x[1].lower(), x[3]))
        
            
            
    print(res)
            