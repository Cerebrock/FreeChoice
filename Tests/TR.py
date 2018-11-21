def TR(nTrials):
    import pygame
    import random 
    import time
    
    pygame.init()
    
    tkn = (212, 212, 212)
    width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
    
    try:
        screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
    except pygame.error:
        screen = pygame.display.set_mode((1360, 780), pygame.FULLSCREEN)
        print("display err")
    
    screen.fill(tkn)
    pygame.display.flip()
    pygame.display.set_caption("TRTest")
    data = []
    
    while True:
        start = False
        fnt = pygame.font.SysFont("Verdana", 23)
        instr = "Aparecerá un círculo rojo en la pantalla. Apenas aparezca, presione cualquier tecla LO MÁS RÁPIDO POSIBLE. \n Presione alguna para comenzar"        
        instructions = instr.split("\n")
        count = 1
        for inst in instructions:
            instruction = fnt.render(inst, 1, (0, 0, 0))
            screen.blit(instruction, ((width/2) - (instruction.get_rect().width/2), (100 + (instruction.get_rect().height+10)*count)))
            count += 1 
        pygame.display.flip()
        while not start:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    start = True
                    break
        
        if start == True:
            for x in range(nTrials): 
                screen.fill(tkn)
                pygame.draw.line(screen, (0, 0, 0), (width/2, height/2 - 20), (width/2, height/2 + 20), 2)    
                pygame.draw.line(screen, (0, 0, 0), (width/2 - 20, height/2), (width/2 + 20, height/2), 2)    
                pygame.display.flip()    
                pygame.time.delay(random.randint(2000, 4000))
                pygame.draw.circle(screen, (255, 0, 0), (int(width/2), int(height/2)), 200)
                pygame.display.flip()
                t0 = time.clock()
                pygame.event.clear()
                running = True        
                while running:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN and event.key != pygame.K_ESCAPE:
                            t1 = time.clock()
                            tr = (t1 - t0)
                            data.append(str(round(tr, 3)))
                            running = False
                        else:
                            pygame.quit()
                            exit()
        pygame.quit()
        return data
