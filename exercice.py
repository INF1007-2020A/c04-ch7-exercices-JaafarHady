#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici

from math import pi

import sys
sys.path.insert(1, "C:\Users\hadyj\PycharmProjects\c04-ch6-exercices-JaafarHady")
from exercice2 import frequence



# TODO: Définissez vos fonction ici

def ellipsoide(a,b,c,mv):

    volume = ((4*pi*a*b*c))/3

    masse =  volume*mv

    return (volume,masse)



if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    a,b,c,mv= 2,4,2,10
    ellipsoide(a,b,c,mv)
    print(f"Le volume et la masse somt : {ellipsoide(a,b,c,mv)}")

    frequence("phraseeeee")





    pass
