class FamilyMember:
    def __init__(self, name):
        '''
        On intialization, each family member instance
        will have a name, an undefined parent and an empty
        array of children.
        '''
        self.name = name
        self.parent = None
        self.children = []

    def add_child(self, parent, name):
        '''
        This method adds a FamilyMember object to the children
        array of the parent when passed a parent name.
        It recursively goes through the tree to find a match of
        the parent's name. Returns True if the parent is found and
        the child object is created. Returns False if the parent is not
        found and no child object is created.
        '''
        current_member = self
        if current_member.name == parent:
            child = FamilyMember(name)
            child.parent = current_member
            current_member.children.append(child)
            return True
        for child in current_member.children:
            c_add = child.add_child(parent, name)
            if c_add is True:
                return True
        return False

    def find_grandparent(self, name):
        '''
        This method finds the grandparent of a name in
        the tree. If the grandparent is found, the name of the
        grandparent is returned. If the grandparent is not found
        or the relationship is invalid, it returns False.
        '''
        if self.name == name:
            if self.parent is not None and self.parent.parent is not None:
                return self.parent.parent.name
            else:
                return False
        for child in self.children:
            gpa = child.find_grandparent(name)
            if gpa is not False:
                return gpa
        return False
