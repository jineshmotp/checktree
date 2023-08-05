from tree import Tree

def example_data(root):
    """
        ['Child', 1] ['nChild', 1] ['nChild', 2]
        ['Child', 2] ['nChild', 1] ['nChild', 2]
        ['Child', 3] ['nChild', 1] ['nChild', 2]

    """
    root.create_data(["Root"])
    root.create_children(3)

    counter = 1
    for child in root.children:
        child.create_data(["Child", counter])
        child.create_children(2)
        counter += 1

        ncounter = 1
        for nchild in child.children:
            nchild.create_data(["nChild", ncounter])
            ncounter += 1

    return root

if __name__ == "__main__":
    root = example_data(Tree())
    root.display_data()