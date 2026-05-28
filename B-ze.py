#!/usr/bin/env python3
import sys
#Funciones
def count_gc(seq_p):
        if len(seq_p) == 0:
            return 0.0
        g = seq_p.count("G")
        c = seq_p.count("C")
        total = len(seq_p)
        gc = (g + c) / total *100
        return gc
#Lógica principal
if len(sys.argv) != 2:
    print ("Cantidad de archivos incorrecta")
    sys.exit(1)
else: 
    file = sys.argv[1]
    with open(file, "r") as seq:
        seq_p = seq.read().strip()
        long = len(seq_p)
        a = seq_p.count ("A")
        t = seq_p.count ("T")
        c = seq_p.count ("C")
        g = seq_p.count ("G")
        arn = seq_p.replace("T", "U")
        print("Secuencia procesada")
        print("Longitud: ", long)
        print(f'A: {a}, T: {t}, C: {c}, G: {g}')
        print(f'Contenido GC:  {count_gc(seq_p)} %')
        print(arn)