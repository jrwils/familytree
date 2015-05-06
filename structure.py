from familytree import FamilyMember


def create_tree_structure():
    tree_root = FamilyMember('Nancy')
    tree_root.add_child('Nancy', 'Adam')
    tree_root.add_child('Nancy', 'Jill')
    tree_root.add_child('Nancy', 'Carl')
    tree_root.add_child('Carl', 'Catherine')
    tree_root.add_child('Carl', 'Joseph')
    tree_root.add_child('Jill', 'Kevin')
    tree_root.add_child('Kevin', 'Samuel')
    tree_root.add_child('Kevin', 'George')
    tree_root.add_child('Kevin', 'James')
    tree_root.add_child('Kevin', 'Aaron')
    tree_root.add_child('James', 'Mary')
    tree_root.add_child('George', 'Patrick')
    tree_root.add_child('George', 'Robert')
    return tree_root


if __name__ == '__main__':
    mytree = create_tree_structure()
    print("Kevin's grandparent:")
    print(mytree.find_grandparent('Kevin'))
    print("Family members without siblings:")
    mytree.has_no_siblings()
    print("Family members without children:")
    mytree.has_no_children()
