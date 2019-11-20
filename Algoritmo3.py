def Algoritmo3(arr, an, al, la):
    nC = 1
    volumen = arr[0].Volumen()
    arr[0].C = nC
    
    xmax = arr[0].largo
    
    ymax = arr[0].ancho

    for i in range(1, len(arr)):
        
        volumen += arr[i].Volumen()
        
        if arr[i-1].x + arr[i].largo <= la:
            if  arr[i].ancho + arr[i-1].y <= an:
                if arr[i].alto + arr[i-1].z +arr[i-1].alto <= al:
                    arr[i].C = nC
                    if xmax < arr[i-1].x + arr[i].largo: xmax = arr[i-1].x + arr[i].largo
                    if ymax < arr[i-1].y + arr[i].ancho: ymax = arr[i-1].y + arr[i].ancho
                    arr[i].x = arr[i-1].x
                    arr[i].y = arr[i-1].y
                    arr[i].z = arr[i-1].z + arr[i-1].alto
                else:
                    if  arr[i].ancho + ymax <= an:  
                        arr[i].C = nC
                        arr[i].x = arr[i-1].x
                        arr[i].y = ymax
                        arr[i].z = 0 
                        ymax = arr[i].y + arr[i].ancho
                        if xmax < arr[i-1].x + arr[i].largo: xmax = arr[i-1].x + arr[i].largo
                        
                    else:
                        if xmax + arr[i].largo <= la:
                            arr[i].C = nC
                            arr[i].x = xmax
                            arr[i].y = 0
                            arr[i].z = 0
                            xmax = xmax + arr[i].largo
                            ymax = arr[i].ancho
                        else:
                            xmax = arr[i].largo
                            ymax = arr[i].ancho
                            nC += 1
                            arr[i].C = nC
                        
            else:
                if xmax + arr[i].largo <= la:
                    arr[i].C = nC
                    arr[i].x = xmax
                    arr[i].y = 0
                    arr[i].z = 0
                    xmax = xmax + arr[i].largo
                    ymax = arr[i].ancho
                else:
                    xmax = arr[i].largo
                    ymax = arr[i].ancho
                    nC += 1
                    arr[i].C = nC
        else:
            nC += 1
            arr[i].C = nC
            
    return arr, nC, volumen