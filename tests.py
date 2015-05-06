import unittest
import sys
from io import StringIO
from familytree import FamilyMember


class TestFamilyTree(unittest.TestCase):
    # def setUp(self):
    #    self.held, sys.stdout = sys.stdout, StringIO()

    def test_init_of_family_member(self):
        member = FamilyMember('John')
        assert member.name == 'John'
        assert member.parent is None
        assert member.children == []

    def test_adding_child_to_parent(self):
        '''
        This tests the add_child method of FamilyMember to make sure
        a child is successfully added to a member's children array.
        Tests a top-level child addition and a second-level child addition.
        '''
        tree_root = FamilyMember('John')
        c_add = tree_root.add_child('John', 'Jim')
        assert c_add is True
        assert tree_root.children[0].name == 'Jim'
        assert tree_root.children[0].parent.name == 'John'

        c_add2 = tree_root.add_child('Jim', 'Sally')
        assert c_add2 is True
        assert tree_root.children[0].children[0].name == 'Sally'
        assert tree_root.children[0].children[0].parent.name == 'Jim'

    def test_adding_child_with_no_parent_entry(self):
        '''
        This tests the add_child method when passed a parent name
        that does not exist in the tree. This should always return False.
        '''
        tree_root = FamilyMember('Jack')
        c_add = tree_root.add_child('John', 'Jim')
        assert c_add is False

    def test_finding_grandparent_valid(self):
        '''
        This tests the find_grandparent method when there is a valid
        grandparent present in the tree. Tests both one and two levels
        deep on the tree.
        '''
        tree_root = FamilyMember('Jack')
        tree_root.add_child('Jack', 'Sal')
        tree_root.add_child('Sal', 'Cynthia')
        grandparent = tree_root.find_grandparent('Cynthia')
        assert grandparent == 'Jack'

        tree_root.add_child('Cynthia', 'Sam')
        grandparent = tree_root.find_grandparent('Sam')
        assert grandparent == 'Sal'

    def test_finding_grandparent_invalid(self):
        '''
        This tests the find_grandparent method when there is no valid
        grandparent entry. Tests the tree root, a name that does exist
        and a name that doesn't exist in the tree.
        '''
        tree_root = FamilyMember('Jack')
        grandparent = tree_root.find_grandparent('Jack')
        assert grandparent is False

        tree_root.add_child('Jack', 'Sam')
        grandparent = tree_root.find_grandparent('Sam')
        assert grandparent is False

        grandparent = tree_root.find_grandparent('Hector')
        assert grandparent is False

    def test_printing_no_siblings(self):
        '''
        This tests that the names in the tree with no siblings
        are printed when running the has_no_siblings method.
        '''
        self.held, sys.stdout = sys.stdout, StringIO()
        tree_root = FamilyMember('Jack')
        tree_root.add_child('Jack', 'Donna')
        tree_root.add_child('Donna', 'Sam')
        tree_root.has_no_siblings()
        self.assertEqual(sys.stdout.getvalue(),'Donna\nSam\n')



if __name__ == '__main__':
    unittest.main()
