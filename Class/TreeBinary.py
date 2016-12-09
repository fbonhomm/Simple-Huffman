
from Class.Array import Array as ArrayClass

class Node():

    def __init__(self, word, value, left=None, right=None):
        """
            __init__(word, value, left=None, right=None)
            - word = chararcter / caractere
            - value = occurences
            - left = left branch / branche de gauche
            - right = right branch / branche de droite
            [FR] Parametre le noeud
            [EN] Node setting
        """
        self.word = word
        self.value = value
        self.left = left
        self.right = right

class BinaryTree():

    def __init__(self):
        """
            __init__()
            [FR] Initialise la class array
            [EN] Initialize array class
        """
        self.sort = ArrayClass()

    def create(self, table):
        """
            create(table)
            - table = occurence table / table d'occurences
            [FR] Parametre les noeuds avec la table d'occurences et stocke les noeuds dans une liste/tableau
            [EN] Node setting with occurences table and node storage in list/array
        """
        tree = list()
        for cell in table:
            tree.append(Node(cell, table[cell]))
        return tree

    def build(self, tree):
        """
            build(tree)
            - tree = list containing leaf of binary tree and each node a constitute character:occurences /
                liste contenant les feuilles de l'arbre binaire et chaque noeud est constitutuer caractere:occurences
            [FR] Construit l'arbre binaire en creant un noeud avec les occurences les plus faible
            [EN] Build binary tree creating node with they lowest occurences
        """
        while len(tree) > 1:
            tree = self.sort.sortAscend(tree)
            tmp = Node(tree[0].word + tree[1].word, tree[0].value + tree[1].value, tree[0], tree[1])
            tree[1] = tmp
            tree.remove(tree[0])
        return tree[0]

    def setBinary(self, tree, table=dict(), code=''):
        """
            setBinary(tree, table=dict(), code='')
            - tree = binary tree / arbre binaire
            - table = table will contain all binary code of each character / table qui contiendra le code binaire de chaque caractere
            - code = binary code / code binaire
            [FR] Genere un code binaire pour les caractere en parcourant l'arbre , la branche gauche est 0 et la branche droite est 1
            [EN] Generate binary code for character coursing tree, left branch is 0 and right branch is 1
        """
        if tree:
            if tree.left:
                self.setBinary(tree.left, table, code + '0')
            if tree.right:
                self.setBinary(tree.right, table, code + '1')
            if tree.left == None and tree.right == None:
                table[tree.word] = code
        return table
