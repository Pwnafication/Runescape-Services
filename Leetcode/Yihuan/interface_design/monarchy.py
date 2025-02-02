class Person:
    def __init__(self, str_name):
        self.str_name = str_name  # Name of the person
        self.is_alive = True  # Whether the person is alive
        self.lst_children = []  # List of children (direct descendants)


class Monarchy:
    def __init__(self, king_name):
        # Initialize the monarchy with a king
        self.person_king = Person(king_name)  # The king (root of the monarchy tree)
        self.dct_persons = {self.person_king.str_name: self.person_king}  # Dictionary to store all persons

    def birth(self, child_name, parent_name):
        # Add a child to the parent in the monarchy
        parent = self.dct_persons.get(parent_name)
        if parent is None:
            raise ValueError(f"Parent '{parent_name}' does not exist.")
        
        child = Person(child_name)
        parent.lst_children.append(child)
        self.dct_persons[child_name] = child

    def death(self, name):
        # Mark a person as deceased
        person = self.dct_persons.get(name)
        if person is None:
            raise ValueError(f"Person '{name}' does not exist.")
        person.is_alive = False

    def get_order_of_succession(self):
        # Get the current order of succession
        lst_order_of_succession = []
        self._dfs(self.person_king, lst_order_of_succession)
        return lst_order_of_succession

    def _dfs(self, current_person, order):
        # Perform a depth-first search to determine the order of succession
        if current_person.is_alive:
            order.append(current_person.str_name)
        for child in current_person.lst_children:
            self._dfs(child, order)


# Create an object for the England Monarchy
EnglandMonarchyObject = Monarchy("King Arthur")

# Add children and descendants
EnglandMonarchyObject.birth("Child1", "King Arthur")
EnglandMonarchyObject.birth("Child2", "King Arthur")
EnglandMonarchyObject.birth("Grandchild1", "Child1")
EnglandMonarchyObject.birth("Grandchild2", "Child1")
EnglandMonarchyObject.birth("Grandchild3", "Child2")

# Mark someone as deceased
EnglandMonarchyObject.death("Child1")

# Get the order of succession
print(EnglandMonarchyObject.get_order_of_succession())  # Output: ['King Arthur', 'Grandchild1', 'Grandchild2', 'Child2', 'Grandchild3']
