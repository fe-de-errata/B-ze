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
#Menú
print("Gracias por usar mi programa <3 \n")
#Filtro del archivo y selección de proceso
if len(sys.argv) != 2:
    print ("Cantidad de archivos incorrecta")
    sys.exit(1)
else:
    while True:
        try:
            proceso = int(input(f'¿Qué proceso quiéres hacer? \n Conteo de bases: 1  \n Tamaño de tu secuencia: 2 \n Convertir a ARN: 3 \n Conteo de N: 4 \n Conteo GC: 5 \n'))
            if proceso in (1, 2, 3, 4, 5):
                break
            print ("Opción no válida. Elige 1, 2, 3, 4 o 5.")
        except ValueError:
            print("Escribe un número, no texto.")    
    file = sys.argv[1]
#Apertura y lectura del archivo
    with open(file, "r") as seq:
        linea = seq.readlines()
        while True:
            try: 
                file_type = int(input ("¿Tu archivo es .fasta? \n Si: 1 \n No: 2 \n"))
                if file_type in (1, 2):
                    break
                print ("Intenta de nuevo")
            except ValueError:
                print ("Intenta de nuevo")
    if file_type == 1:
        seq_q = "".join(line.strip() for line in linea if not line.startswith(">"))
    else:
        seq_q = "".join(line.strip() for line in linea[1:])
#Procesamiento
    if proceso == 1:
        a = seq_q.count ("A")
        t = seq_q.count ("T")
        c = seq_q.count ("C")
        g = seq_q.count ("G")
        print("Secuencia procesada")
        print(f'A: {a}, T: {t}, C: {c}, G: {g}')
    elif proceso == 2:
        long = len(seq_q)
        print("Secuencia procesada")
        print("Longitud: ", long)
    elif proceso == 3:
        arn = seq_q.replace("T", "U")
        print("Secuencia procesada")
        print(arn)
    elif proceso == 4:
        posicion = [i+1 for i, base in enumerate(seq_q) if base == "N"]
        n = len(posicion)
        if n != 0:
            print (f'Número de N:  {n} \n Posiciones: {posicion}')
        else:
            print ("Número de N: 0")
    elif proceso == 5:
        gc = count_gc(seq_q)
        at = 100 - gc
        ratio = at/gc if gc > 0 else "indefinido"
        print (f'Contenido GC: {gc : .2f} %')
        print (f'Contenido AT: {at : .2f} %')    
        print (f'Ratio AT/GC: {ratio}')
print ("Gracias <3")