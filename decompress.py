from Class.TreeBinary import BinaryTree as TreeClass
from Class.Array import Array as ArrayClass
from Class.Decode import Decode as DecodeClass

import sys

Tree = TreeClass()
Decode = DecodeClass(sys.argv[1], sys.argv[2])

def decompress():
    Decode.setSizeFile(Decode.read(8))
    Decode.setSizeHead(Decode.read(2))
    head = Decode.character_frequency()
    tree = Tree.create(head)
    tree = Tree.build(tree)
    table = Tree.setBinary(tree)
    Decode.decodingTxt(tree)
    Decode.closeFd()

if __name__ == '__main__':
    decompress()
