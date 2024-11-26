class Person:
    def __init__(self, str_name):
        self.str_name = str_name  # The person's name
        self.is_alive = True  # Whether the person is alive
        self.lst_children = []  # List of children (direct descendants)

class Monarchy:
    def __init__(self, str_king_name):
        self.person_king = Person(str_king_name)  # The king (root of the monarchy tree)
        self.dct_persons = {self.person_king.str_name: self.person_king}  # Dictionary to store all persons by name

    def birth(self, str_child_name, str_parent_name):
        person_parent = self.dct_persons.get(str_parent_name)
        if person_parent is None:
            raise ValueError(f"Parent '{str_parent_name}' does not exist.")
        person_child = Person(str_child_name)
        person_parent.lst_children.append(person_child)
        self.dct_persons[str_child_name] = person_child

    def death(self, str_name):
        person = self.dct_persons.get(str_name)
        if person is None:
            raise ValueError(f"Person '{str_name}' does not exist.")
        person.is_alive = False

    def get_order_of_succession(self):
        lst_order_of_succession = []
        self._dfs(self.person_king, lst_order_of_succession)
        return lst_order_of_succession

    def _dfs(self, person_current, lst_order_of_succession):
        if person_current.is_alive:
            lst_order_of_succession.append(person_current.str_name)
        for person_child in person_current.lst_children:
            self._dfs(person_child, lst_order_of_succession)

# Example usage:
monarchy = Monarchy("King Arthur")  # Initialize the monarchy with King Arthur as the king
monarchy.birth("Child1", "King Arthur")  # King Arthur has Child1
monarchy.birth("Child2", "King Arthur")  # King Arthur has Child2
monarchy.birth("Grandchild1", "Child1")  # Child1 has Grandchild1
monarchy.birth("Grandchild2", "Child1")  # Child1 has Grandchild2
monarchy.birth("Grandchild3", "Child2")  # Child2 has Grandchild3

monarchy.death("Child1")  # Child1 is now deceased

print(monarchy.get_order_of_succession())  # Output: ['King Arthur', 'Grandchild1', 'Grandchild2', 'Child2', 'Grandchild3']

# dct_persons = {
#     "King Arthur": <Person Object for "King Arthur">,
#     "Child1": <Person Object for "Child1" (is_alive=False)>,
#     "Child2": <Person Object for "Child2">,
#     "Grandchild1": <Person Object for "Grandchild1">,
#     "Grandchild2": <Person Object for "Grandchild2">,
#     "Grandchild3": <Person Object for "Grandchild3">
# }

# King Arthur.lst_children = [<Person Object for "Child1">, <Person Object for "Child2">]
# Child1.lst_children = [<Person Object for "Grandchild1">, <Person Object for "Grandchild2">]
# Child2.lst_children = [<Person Object for "Grandchild3">]
# Grandchild1.lst_children = []
# Grandchild2.lst_children = []
# Grandchild3.lst_children = []