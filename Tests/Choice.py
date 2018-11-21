def choice(rstart, nranks, criterion_n, imgs_path, ctrl_path, data_path, avoid_list=None):
    import pygame
    import os
    from PIL import Image
    import random
    import time
    
    def get_info(filename):
        with open(filename, "r") as data:
            lines = [a for a in data.readlines()]
            lastline = len(lines)
        info = list(lines[lastline - 1].split(", "))
        ranks = info[(rstart - 1):(rstart + nranks) - 1]
        return info, ranks, lastline
  
    #list of pics by rank
    def get_pics_by_rank(ranks):
        pxp = [list() for i in range(9)]
        for n, r in enumerate(ranks):
            if str(r) != "" and str(r) != " " and str(r) in "123456789":
                pxp[int(r) - 1].append(n + 1)
        return pxp
        
    def get_ranked_pair(rank, picsbyr):
        t = []        
        if len(picsbyr[rank - 1]) >= 2:
            n1 = random.randint(0, len(picsbyr[rank - 1]) - 1)
            t.append((rank, picsbyr[rank - 1][n1]))
            n2 = random.randint(0, len(picsbyr[rank - 1]) - 1)
            while n2 == n1:
                n2 = random.randint(0, len(picsbyr[rank - 1]) - 1) 
            t.append((rank, picsbyr[rank - 1][n2]))
            return t
        else:
            raise Exception("No 7/3 or 6/4 duplicates.")
            pygame.quit()
            return None
 
    def get_equal(pxp, criterion_n, ranks):
        if len(pxp[2]) >= 2 and len(pxp[6]) >= 2:
            if criterion_n == 0:
                equal = get_ranked_pair(3, pxp)         
            elif criterion_n == 1:
                equal = get_ranked_pair(7, pxp)
        elif len(pxp[3]) >= 2 and len(pxp[5]) >= 2:
            if criterion_n == 0:
                equal = get_ranked_pair(4, pxp)
            elif criterion_n == 1:
                equal = get_ranked_pair(6, pxp)
        else:
            print("Ranks:" + str(ranks))
            raise Exception("No 7/3 or 6/4 duplicates.")
            pygame.quit()
        return equal
        
    #get unequally ranked pics
    def get_dispar(pxp, ranks):
        dispar = []
        if len(pxp[7]) >= 1 and len(pxp[1]) >= 1:
            n1 = random.randint(0, len(pxp[7]) - 1)
            dispar.append((8, pxp[7][n1]))
            n2 = random.randint(0, len(pxp[1]) - 1)
            dispar.append((2, pxp[1][n2]))
        else:
            print("Ranks:" + str(ranks))
            raise Exception("No 8/2 duplicates.")            
            pygame.quit()
        random.shuffle(dispar)
        return dispar
    
    def load_imgs(picsids, path):
        imgs = []
        for e in picsids:
            for filename in os.listdir(path):
                    if filename == e + ".jpg":
                        name = e
                        i = Image.open(os.path.join(path + "/" + filename))
                        i.thumbnail((600, 600), Image.ANTIALIAS)
                        mode = i.mode
                        size = i.size
                        data = i.tobytes()
                        name = pygame.image.fromstring(data, size, mode)
                        name.convert()
                        imgs.append(name)
        return imgs
        
    def load_control_imgs(except_list):
        n_pics = len([name for name in os.listdir(ctrl_path)])
        i1, i2 = str(random.randint(1, n_pics)), str(random.randint(1, n_pics))
        while i1 in except_list:
            i1 = str(random.randint(1, n_pics))
        while i2 == i1 or i2 in except_list:
            i2 = str(random.randint(1, n_pics))
        parControl = [i1, i2]
        img_list = load_imgs(parControl, ctrl_path)           
        return img_list, parControl
        
    def load_critical_imgs(duplicates):
        chosenPair = [str(t[1]) for t in duplicates]
        imgs = load_imgs(chosenPair, imgs_path)
        return imgs, chosenPair

    def display_imgs(imgs):
        screen.fill(tkn)
        pygame.display.flip()
        count = 0
        for i in range(2):
            a = imgs.pop(0)
            if count == 0:
                screen.blit(a, ((0.5 * width - 0.5 * (0.5 * width - a.get_rect().width)) - a.get_rect().width, 0.5 * height - 0.5 * a.get_rect().height))
                count += 1
            elif count == 1:
                screen.blit(a, ((0.5 * width + 0.5 * (0.5* width - a.get_rect().width)), 0.5 * height - 0.5 * a.get_rect().height))
            else:
                raise Exception("Display err")
        pygame.event.clear()
        pygame.display.flip()
        t0 = time.clock()
        return t0

    def handlekey(event, chosenPair, t0, t1):
        tr = str(round((t1 - t0), 3))
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            chosen = chosenPair[1]
            print("Chosen:" + str(chosen))
            screen.fill(tkn)
            pygame.display.update(pygame.Rect(0, 0, screen.get_rect().width/2, screen.get_rect().height))
            pygame.time.delay(1000)            
            return chosen, tr
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            chosen = chosenPair[0]
            print("Chosen:" + str(chosen))
            screen.fill(tkn)
            pygame.display.update(pygame.Rect(screen.get_rect().width/2, 0, screen.get_rect().width, screen.get_rect().height))
            pygame.time.delay(1000)
            return chosen, tr
        else:
            pass

    def choose(criterion_n, ranks):
        if criterion_n == 0 or criterion_n == 1:
            print("Criterion: " + criterion_w[criterion_n])                
            equal_pics = get_equal(pxp, criterion_n, ranks)
            print("Duplicates (Rank, Id): " + str(equal_pics))
            try:
                imgs, chosenPair = load_critical_imgs(equal_pics)
                t0 = display_imgs(imgs)
                print("Chosen pair:" + str(chosenPair))
                return (str(equal_pics[0][0]), str(equal_pics[1][0])), chosenPair, t0
            except Exception as err:
                print("Error:" + str(err))                
                pygame.quit()
                time.sleep(2)
                exit()
        elif criterion_n == 3:
            print("Criterion: " + criterion_w[criterion_n])
            dispar = get_dispar(pxp, ranks)
            imgs, chosenPair = load_critical_imgs(dispar)
            t0 = display_imgs(imgs)
            print("Chosen High-Low: (Rank, Id): " + str(dispar))
            return (str(dispar[0][0]), str(dispar[1][0])), chosenPair, t0
        elif criterion_n == 4:
            imgs, parControl = load_control_imgs(avoid_list)
            t0 = display_imgs(imgs)
            print("Criterion: " + criterion_w[criterion_n])
            print("Par control: " + str(parControl))
            return ("c", "c"), parControl, t0
        else:
            raise Exception("Wrong criterion")
            pygame.quit()
            time.sleep(2)
            exit()
            
    pygame.init()
    tkn = (232, 232, 232)
    width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
    screen.fill(tkn)
    pygame.display.flip()
    pygame.display.set_caption("Choice")
    
    idinfo, ranks, lastline = get_info(data_path)
    pxp = get_pics_by_rank(ranks)
    criterion_w = {0 : "Low Pair", 1 : "High Pair", 3 : "High-Low Pair", 4 : "Control condition"}    

    start = False    
    if start == False:
        #fixation point
        pygame.draw.line(screen, (0, 0, 0), (width/2, height/2 - 20), (width/2, height/2 + 20), 2)
        pygame.draw.line(screen, (0, 0, 0), (width/2 - 20, height/2), (width/2 + 20, height/2), 2)
        pygame.display.flip()
        pygame.time.delay(random.randint(1800, 2200))
        preRank, chosenPair, t0 = choose(criterion_n, ranks)
        start = True
        
    while start:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and t0 != 0:
                if event.key != pygame.K_ESCAPE:
                    t1 = time.clock()
                    chosen_pic, tr = handlekey(event, chosenPair, t0, t1)
                    start = False                    
                else:
                    pygame.quit()
                    exit()
            else:
                pass
    data = []
    data.extend([str(criterion_n), preRank[0], chosenPair[0], preRank[1], chosenPair[1], chosen_pic, tr])                    
    
    print("Subject data: " + str(idinfo))
    print("Lifted Ranks:" + str(ranks))
    print("List of lists of PicIds by rank: " + str(pxp))
    print("Shown Pair (PicIds): " + str(chosenPair))
    print("Chosen Pic: " + str(chosen_pic))
    print("Choice data: " + str(data))
    return data

def critico(imgs_path, ctrl_path, data_path):
    import random
    import pygame
    import instruct    
    inst = "Elija entre las siguientes imagenes según su preferencia, usando las teclas izquierda y derecha. \n Presione cualquier tecla para comenzar"
    instruct.instruct(inst)    
    order = [0, 1, 3]
    random.shuffle(order)
    choice_data = []    
    for i in range(3):    
        try:
            d1 = choice(7, 30, order[i], imgs_path, ctrl_path, data_path)
            choice_data.extend(d1)
        except Exception as err:
            print("Error: " + str(err))
            choice_data.append(str(order[i]))          
            for n in range(6):
                choice_data.append("n")
            pass
        print("----")
    pygame.quit()
    return choice_data
    
def control(imgs_path, ctrl_path, data_path):
    import pygame
    from instruct import instruct
    inst = "Elija entre las siguientes imagenes según su preferencia, usando las teclas izquierda y derecha. \n Presione cualquier tecla para comenzar"
    instruct(inst)
    avoid = []
    choice_data = []
    for i in range(3):    
        try:
            d1 = choice(7, 30, 4, imgs_path, ctrl_path, data_path, avoid)
            choice_data.extend(d1)
            avoid.extend([d1[2], d1[4]])
        except Exception as e:
            print("Error: " + str(e))
            pass    
        print("----")
    pygame.quit()
    return choice_data