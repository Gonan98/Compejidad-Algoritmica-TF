def NFDH(arr, an, al, la):
    nC = 1
    volumen = arr[0].Volumen()
    arr[0].C = nC
    xmax = arr[0].largo
    xant = 0
    zn = arr[0].alto
    zant = 0
    for i in range(1, len(arr)):
        volumen += arr[i].ancho * arr[i].alto * arr[0].largo 
        w = arr[i-1].y + arr[i-1].ancho + arr[i].ancho
        if xant + arr[i].largo <= la:
            arr[i].C = nC
            if w <= an:
                if xmax < xant + arr[i].largo: xmax = xant + arr[i].largo
                arr[i].x = xant
                arr[i].y = arr[i-1].y + arr[i-1].ancho
                arr[i].z = zant
            elif arr[i].largo+xmax <= la:
                arr[i].x = xmax
                xant = xmax
                arr[i].y = 0
                arr[i].z = zant
                xmax = xmax + arr[i].largo
            elif arr[i].alto + zn <= al:
                arr[i].x = 0
                arr[i].y = 0
                zant = zn
                arr[i].z = arr[i].alto + zn
                zn = arr[i].z
                arr[i].C = nC
            else:
                nC += 1
                arr[i].C = nC
                xmax = arr[i].largo
                xant = 0
                zn = arr[i].alto
                zant = 0
        elif arr[i].alto + zn <= al:
            arr[i].x = 0
            arr[i].y = 0
            zant = zn
            arr[i].z = arr[i].alto + zn
            zn = arr[i].z
            arr[i].C = nC
        else:
            nC += 1
            arr[i].C = nC
            xmax = arr[i].largo
            xant = 0
            zn = arr[i].alto
            zant = 0
            
    return arr, nC, volumen