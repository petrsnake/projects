#import modulu
import Turtle                   #import celého modulu
from Turtle import turtle       #import funkce z modulu
from Turtle import turtle as TT #import f. jako objekt 'TT'

#zajímavý modul o čase
from time import sleep
sleep(2)       #např. tato funkce čeká 2s.

#vypíše všechny aktuální moduly
import os
dir(os)
