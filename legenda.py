#!/usr/bin/python3

import sys
import re


# Script que lê um arquivo srt e retira acentuações da língua portuguesa.
# Pois alguns dispositivos não conseguem mostrá-los apropriadamente.

def substituir(texto):
    substitutos = {
        'ç': 'c', 'Ç': 'C',
        'â': 'a', 'Â': 'A',
        'ê': 'e', 'Ê': 'E',
        'ô': 'o', 'Ô': 'O',
        'ã': 'a', 'Ã': 'A',
        'õ': 'o', 'Õ': 'O',
        'á': 'a', 'Á': 'A',
        'é': 'e', 'É': 'E',
        'í': 'i', 'Í': 'I',
        'ó': 'o', 'Ó': 'O',
        'ú': 'u', 'Ú': 'U',
        'à': 'a', '^': ' ',
        '~': ' ',
    }

    for antigo, novo in substitutos.items():
        texto = texto.replace(antigo, novo)

    return texto

def main():
    if len(sys.argv) != 2:
        print("Uso: python script.py arquivo.srt")
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, 'r', encoding='utf-8') as file:
        srt_cont = file.read()

    srt_cont = substituir(srt_cont)

    with open(input_file, 'w', encoding='utf-8') as file:
        file.write(srt_cont)

if __name__ == "__main__":
    main()
