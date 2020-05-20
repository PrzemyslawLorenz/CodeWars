class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n
        temp = []
        if L == None and R == None:
            print(n)
        else:
            temp.append(n)
        print(temp)


def tree_by_levels(node):
    return


# print(tree_by_levels(None))
print(tree_by_levels(Node(Node(None, Node(None, None, 4), 2),
                          Node(Node(None, None, 5), Node(None, None, 6), 3),
                          1)))
