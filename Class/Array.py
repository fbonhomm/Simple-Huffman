
class Array():

    def sortAscend(self, tree):
        """
            sortAscend(tree)
            - tree = table containing node of the tree / tableau contenant les noeuds de l'arbre
            [FR] Trie le tableau de noeud par ordre croissant
            [EN] Sort table containing node per ascend order
        """
        for i in range(1, len(tree)):
            node = tree[i]
            while i > 0 and tree[i - 1].value >= node.value:
                if tree[i - 1].value == node.value and tree[i - 1].word <= node.word:
                    break
                tree[i] = tree[i - 1]
                i -= 1
            tree[i] = node
        return tree

    def sortDescend(self, tree):
        """
            sortDescend(tree)
            - tree = table containing node of the tree / tableau contenant les noeuds de l'arbre
            [FR] La fonction trie le tableau de noeud par ordre decroissant
            [EN] Sort table containing node per descend order
        """
        for i in range(1, len(tree)):
            node = tree[i]
            while i > 0 and tree[i - 1].value <= node.value:
                if tree[i - 1].value == node.value and tree[i - 1].word >= node.word:
                    break
                tree[i] = tree[i - 1]
                i -= 1
            tree[i] = node
        return tree
