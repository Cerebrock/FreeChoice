def instruct(instr):
        import pygame
        pygame.init()
        tkn = (232, 232, 232)
        width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
        screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
        screen.fill(tkn)
        pygame.display.flip()
        pygame.display.set_caption("Instruccion")
        fnt = pygame.font.SysFont("Verdana", 25)
        instructions = instr.split("\n")
        count = 1
        for inst in instructions:
            instruction = fnt.render(inst, 1, (0, 0, 0))
            screen.blit(instruction, (((width/2) - (instruction.get_rect().width)/2), (100 + (instruction.get_rect().height+10)*count)))
            count += 1 
        pygame.display.flip()        
        c = True
        while c == True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key != pygame.K_ESCAPE:
                        c = False
                        pygame.quit()
                    else:
                        pygame.quit()
                        exit()
    
