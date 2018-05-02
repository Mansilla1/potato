#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
from potato import potato

# imprimir salida en formato csv
def print_csv(tipo, *mensaje):
    salida = potato.evidencia + 'output.csv'
    with open(salida, tipo) as output:
        writer = csv.writer(output, delimiter=";", quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        for i in mensaje:
            writer.writerow(i)