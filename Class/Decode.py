
from struct import *
import sys

class Decode():

    def __init__(self, input, output):
        """
            __init__(input, output)
            - input = compressed file / fichier compresser
            - output = decompressed file / fichier decompresser
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

    def character_frequency(self):
        """
            character_frequency()
            [FR] Recupere la table d'occurence dans le fichier compresser
            [EN] Recover occurences table on compressed file
        """
        table = dict()
        i = 0
        while i < self.sizeHead:
            c = self.read(1)
            nb = self.read(4)
            table[c] = nb
            i += 1
        return table

    def read(self, nbr):
        """
            read(nbr)
            - nbr = octet number / nombre octet
            [FR] Lit le/les octet du fichier
            [EN] Read byte on file
        """
        txt = self.fdin.read(nbr)
        if nbr == 1:
            types = "B"
        elif nbr == 2:
            types = "H"
        elif nbr == 4:
            types = "I"
        elif nbr == 8:
            types = "L"
        else:
            types = "B"
        return unpack(types, txt)[0]

    def write(self, char):
        """
            write(char)
            - char = character / caractere
            [FR] Ecrit un caractere dans le fichier de sortie et soustrait un a la taille du fichier original
            [EN] Write one character on output file and decremente one in size original file
        """
        self.sizeFile -= 1
        self.fdout.write(pack('B', char))

    def getChar(self):
        """
            getChar()
            [FR] Ecrit un caractere dans le fichier de sortie et soustrait un a la taille du fichier original
            [EN] Write one character on output file and decremente one in size original file
        """
        c = bin(self.read(1))[2:]
        while len(c) < 8:
            c = '0' + c
        return c

    def decodingTxt(self, tree):
        """
            decodingTxt(tree, table)
            - tree = binary tree / arbre binaire
            [FR] Parcour l'arbre binaire en fonction du code binaire et affichage le chararcter quand une feuille est atteinte
            [EN] Course binary tree according of binary code and display a character when leaf
        """
        char = ''
        while self.sizeFile > 0:
            char += self.getChar()
            tmpTree = tree
            c = ''
            for bit in char:
                if tmpTree.left == None and tmpTree.right == None:
                    self.write(tmpTree.word)
                    tmpTree = tree
                    char = char[len(c):]
                    c = ''
                    if self.sizeFile <= 0:
                        break

                if bit == '0':
                    tmpTree = tmpTree.left
                else:
                    tmpTree = tmpTree.right

                c += bit
