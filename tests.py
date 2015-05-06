import unittest
from familytree import FamilyMember


class TestFamilyTree(unittest.TestCase):
    def test_init_of_family_member(self):
        member = FamilyMember('John')
        assert member.name == 'John'
        assert member.parent is None
        assert member.children == []


if __name__ == '__main__':
    unittest.main()
