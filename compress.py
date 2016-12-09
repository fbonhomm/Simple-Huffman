from Class.TreeBinary import BinaryTree as TreeClass
from Class.Array import Array as ArrayClass
from Class.Encode import Encode as EncodeClass

import sys

Tree = TreeClass()
Encode = EncodeClass(sys.argv[1], sys.argv[2])

def compress():
    txt = Encode.fdin.read()
    head = Encode.character_frequency(txt)
    Encode.setSizeFile(len(txt))
    Encode.setSizeHead(len(head))
    tree = Tree.create(head)
    tree = Tree.build(tree)
    table = Tree.setBinary(tree)
    Encode.encodingHead(head)
    Encode.encodingTxt(txt, table)
    Encode.closeFd()

if __name__ == '__main__':
    compress()
