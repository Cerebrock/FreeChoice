#!/usr/bin/env python3
import TR
import Rank
import Choice
import os
import random
import sys
import time
from Question import question_w_entry, question_w_options
from instruct import instruct

def write_data(it, path):
    with open(path, "a") as data:    
        for i in it:
            data.write(str(i) + ", ")

data_path = os.path.join(os.path.dirname(sys.argv[0]) + r"\data.txt")
log_path = os.path.join(os.path.dirname(sys.argv[0]) + r"\log.txt")
imgs_path = os.path.join(os.path.dirname(sys.argv[0]) + r"\A")
ctrl_path = os.path.join(os.path.dirname(sys.argv[0]) + r"\B")
sys.stdout = open(log_path, "a")

date = str(time.strftime(r"%d/%m/%y")) + ", " + str(time.strftime("%X"))
print("Date, Start Time: " + str(date))
instruct("Lea atentamente todas las instrucciones del experimento. \n Presione una tecla para comenzar")
data_demog = question_w_entry("sociodemo.txt")

try:
    if not (18 <= int(data_demog[0]) < 40): 
        print("Subject excluded, age not in range.")    
        instruct("Terminado! Aprete una tecla para cerrar.")
        exit()
    elif data_demog[3] not in "SisiSIsí":
        print("Subject excluded, isn't student.")        
        instruct("Terminado! Aprete una tecla para cerrar.")
        exit() 
    elif data_demog[4] in "SisiSIsí":
        print("Subject excluded, drug user.")
        instruct("Terminado! Aprete una tecla para cerrar.")
        exit()
    elif data_demog[5] in "SisiSIsí":
        print("Subject excluded, diagnosed with mental condition.")
        instruct("Terminado! Aprete una tecla para cerrar.")
        exit()
except Exception as err:
    print("Bad input: " + str(err))
    pass

with open(data_path, "r+") as data:
    subj_id = len([l for l in data.readlines()]) + 1
    data.write(str(subj_id) + ", ")

print("Subject Id: " + str(subj_id))

instr_rank1 = ["Verá una serie de pinturas. \n Puntúelas con el teclado del 1 (MUY POCO) al 9 (MUCHO) según cuanto le gusten.\n Presione Enter y espere para comenzar."]
instr_rank2 = ["Verá una serie de pinturas. \n Puntúelas con el teclado del 1 (MUY POCO) al 9 (MUCHO) según cuanto le gusten. \n Presione Enter", "No es una prueba de memoria, puntúe independientemente de su puntuación anterior, \n según su preferencia EN ESTE MOMENTO. \n Presione Enter y espere."]
    
data_TR = TR.TR(5)
write_data(data_TR, data_path)
print("TR: " + str(data_TR))
data_rank = Rank.rank(imgs_path, data_path, instr_rank1)
print("Ranks: " + str(data_rank))
write_data(data_rank, data_path)

if random.getrandbits(1):
    data_critico = Choice.critico(imgs_path, ctrl_path, data_path)          #criterio, preRank, PicId, preRank, PicId, chosenId, TR
    write_data(data_critico, data_path)
    data_rank2 = Rank.rank(imgs_path, data_path, instr_rank2)        
    write_data(data_rank2, data_path)
    data_choice = Choice.control(imgs_path, ctrl_path, data_path)
    write_data(data_choice, data_path)    
else:
    data_control = Choice.control(imgs_path, ctrl_path, data_path)    
    write_data(data_control, data_path)    
    data_rank2 = Rank.rank(imgs_path, data_path, instr_rank2)
    write_data(data_rank2, data_path)
    data_critico = Choice.critico(imgs_path, ctrl_path, data_path)
    write_data(data_critico, data_path)

d1 = question_w_options("ROTTER.txt", 2)
write_data(d1, data_path)
print("Rotter: " + str(d1))
d2 = question_w_options("STAIa.txt", 4)
write_data(d2, data_path)
print("STAIa: " + str(d2))
d3 = question_w_options("STAIb.txt", 4)
write_data(d3, data_path)
print("STAIb: " + str(d3))
d4 = question_w_options("BDI.txt", 4)
write_data(d4, data_path)
print("BDI: " + str(d4))

write_data(data_demog, data_path)
print("Socio-demographic: " + str(data_demog))

with open(data_path, 'rb+') as file:
    file.seek(-2, os.SEEK_END)
    file.truncate()
    file.write(b"\n")

print("Done.")
print("':.:"*121 + "\n")
instruct("Terminado! Aprete una tecla para cerrar.")
exit()