from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generate_id(self):
        return randint(0, 99999999)

    def add_member(self, member):
        if "id" not in member:
            member["id"] = self._generate_id()
        self._members.append(member)

    def delete_member(self, id):
        self._members = [member for member in self._members if member["id"] != id]

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return None
    

    def get_all_members(self):
        return self._members
