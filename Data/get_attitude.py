def get_info(filename):
    with open(filename, "r") as data:
        lines = [a.strip() for a in data.readlines()]
        d = []        
        for l in lines:        
            l = l.split(", ")
            d.append(l)
    return d

def get_cambiodeactitud(dat):
    cambios = []
    for data in dat:
        print(data)
        if len(data) > 3:
            subj_id = [data[0]]
            data_TR = data[1:6]
            data_rankA = data[6:36]
            data_tr_rank = data[36:66]
            data_choiceA = data[66:87]
            data_rankB = data[87:117]
            data_tr_rankB = data[117:147]
            data_choiceB = data[147:168]
            rotter = data[168:197]
            staiA = data[197:217]
            staiB = data[217:237]
            bdi = data[237:258]
            sociodemo = data[258:264]
            condition = [data[264]]        
            
            data_choiceA0 = data_choiceA[0:7]
            data_choiceA1 = data_choiceA[7:14]
            data_choiceA2 = data_choiceA[14:21]
            
            data_choiceB0 = data_choiceB[0:7]
            data_choiceB1 = data_choiceB[7:14]
            data_choiceB2 = data_choiceB[14:21]
            ch1 = []
            ch2 = []
            ch1.append(data_choiceA0)
            ch1.append(data_choiceA1)
            ch1.append(data_choiceA2)
            ch2.append(data_choiceB0)
            ch2.append(data_choiceB1)
            ch2.append(data_choiceB2)
            ch1.sort()
            ch2.sort()
            
            if ch1[0][0] == "4":
                pass
            else:
                c = ch1[:]
                ch1 = ch2 
                ch2 = c
            camb = []
            #ch1 = control
            for ch in ch2:
                print(ch)
                if "n" in ch:
                    if ch[0] != "3":
                        camb.append(["n", "n"])                    
                    else:
                        camb.append(["n", "n", "n"])
                else:    
                    chosen = ch[5]
                    if ch[2] == chosen:
                        preCh = ch[1]
                        nonCh = ch[4]
                        preNon = ch[3]
                    elif ch[4] == chosen:
                        preCh = ch[3]
                        nonCh = ch[2]
                        preNon = ch[1]
                    else:
                        print("Err.")
                    try:
                        postCh = data_rankB[int(chosen) - 1]
                        postNon = data_rankB[int(nonCh) - 1]                                                
                        cambioCh = int(preCh) - int(postCh)
                        cambioNon = int(preNon) - int(postNon)
                    except:
                        postCh = "x"
                    try:
                        postCh = data_rankB[int(chosen) - 1]
                        postNon = data_rankB[int(nonCh) - 1]
                        cambioCh = int(preCh) - int(postCh)
                        cambioNon = int(preNon) - int(postNon)                        
                    except:                        
                        postCh = "x"
                    if ch[0] != "3":
                        camb.append([cambioCh, cambioNon])
                    else:
                        if preCh == "8":
                            high_chosen = 1
                        else:
                            high_chosen = 0
                        camb.append([cambioCh, cambioNon, high_chosen])
            cambios.extend([camb])
    return cambios
    #min, max, dispar

import os, sys

data_path = os.path.join(os.path.dirname(sys.argv[0]) + r"/data.txt")
data = get_info(data_path)
cambios = get_cambiodeactitud(data)
with open("cambios.txt", "a+") as out:
    for s in cambios:
        for par in s:
            for v in par:
                out.write(str(v) + ", ")
        out.write("\n")
