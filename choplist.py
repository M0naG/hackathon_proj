def split(arr, size):
    if(size>=1):
        arrs = []
        while len(arr) > size:
            pice = arr[:size]
            arrs.append(pice)
            arr = arr[size:]
        arrs.append(arr)
    else: 
        arrs = [arr]
    return arrs

x=["hii", "bye"]

print(split(x, (int)(len(x)/2)))