
from struct import *

class Encode():

    def __init__(self, input, output):
        """
            __init__(input, output)
            - input = orirginal file / fichier original
            - output = compressed file / fichier compresser
            [FR] Parametre les fichiers d'entrer et de sortie
            [EN] Setting input file and output file
        """
        self.fdin = open(input, 'rb')
        self.fdout = open(output, 'w+b')

    def closeFd(self):
        """
            closeFd()
            [FR] Ferme les fd des fichier
            [EN] Close file descriptor
        """
        self.fdin.close()
        self.fdout.close()

    def setSizeFile(self, size):
        """
            setSizeFile(size)
            - size = size original file / taille du fichier original
            [FR] Initialise la taille du fichier original
            [EN] Initialize original file
        """
        self.sizeFile = size

    def setSizeHead(self, size):
        """
            setSizeHead(size)
            - size = size occurences table / taille de la table d'occurence
            [FR] Initialise la taille de la table d'occurence
            [EN] Initialize size occurences table
        """
        self.sizeHead = size

    def character_frequency(self, txt):
        """
            character_frequency(txt)
            - txt = texte
            [FR] Calcule les occurences dans un texte
            [EN] Occurences calculated in the texte
        """
        table = dict()
        for c in txt:
            if c in table:
                table[c] += 1
            else:
                table[c] = 1
        return table


    def write(self, types, octet):
        """
            write(types, octet)
            - types = represent character a number byte / caractere qui represente le nombre d'octet
            - octet = character / caractere
            [FR] Ecrit un caractere dans le fichier de sortie
            [EN] Write one character on output file
        """
        self.fdout.write(pack(types, octet))

    def encodingTxt(self, txt, head):
        """
            encodingTxt(txt, head)
            - txt = texte
            - head = occurences table / table d'occurences
            [FR] Concatene les code binaire genere par l'arbre binaire et quand l'octet est plaine, on l'ecrit dans le fichier
            [EN] Concate binary code generate on binary tree and when full byte, write in file
        """
        octet = ''
        for c in txt:
            i = 0
            while i < len(head[c]):
                octet += head[c][i]
                if len(octet) >= 8:
                    self.write("B", *bytearray([int(octet, 2)]))
                    octet = ''
                i += 1

        while len(octet) < 8:
            octet += '0'
        self.write("B", *bytearray([int(octet, 2)]))

    def encodingHead(self, head):
        """
            encodingHead(head)
            - head = occurences table / table d'occurences
            -- header format: <sizeOriginalSize><sizeHead><character><occurence><character><occurence> ...
            [FR] Ecrit la table d'occurences au debut du fichier compresser
            [EN] Write occurence table on begin compressed file
        """
        self.write("L", self.sizeFile)
        self.write("H", self.sizeHead)
        for cell in head:
            self.write("B", *bytearray([cell]))
            self.write("I", head[cell])
