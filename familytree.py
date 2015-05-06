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