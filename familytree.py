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
