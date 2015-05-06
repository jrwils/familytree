import unittest
from familytree import FamilyMember


class TestFamilyTree(unittest.TestCase):
    def test_init_of_family_member(self):
        member = FamilyMember('John')
        assert member.name == 'John'
        assert member.parent is None
        assert member.children == []

    def test_adding_child_with_parent(self):
        '''
        This tests the add_child method of FamilyMember to make sure
        a child is successfully added to a member's children array.
        Tests a top-level child addition and a second-level child addition.
        '''
        tree_root = FamilyMember('John')
        c_add = tree_root.add_child('John', 'Jim')
        assert c_add is True
        assert tree_root.children[0].name == 'Jim'

        c_add2 = tree_root.add_child('Jim', 'Sally')
        assert c_add2 is True
        assert tree_root.children[0].children[0].name == 'Sally'


if __name__ == '__main__':
    unittest.main()
