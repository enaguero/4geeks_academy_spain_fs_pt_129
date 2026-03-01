class Member:
    def __init__(self, member_id, first_name, age, lucky_numbers):
        self.id = member_id
        self.first_name = first_name
        self.age = age
        self.lucky_numbers = lucky_numbers

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "age": self.age,
            "lucky_numbers": self.lucky_numbers,
        }


class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self.members = []

    def _generate_id(self):
        current_id = self._next_id
        self._next_id += 1
        return current_id

    def add_member(self, first_name, age, lucky_numbers):
        member = Member(
            member_id=self._generate_id(),
            first_name=first_name,
            age=age,
            lucky_numbers=lucky_numbers,
        )
        self.members.append(member)
        return member

    def get_member(self, member_id):
        for member in self.members:
            if member.id == member_id:
                return member
        return None

    def delete_member(self, member_id):
        member = self.get_member(member_id)
        if member is None:
            return False
        self.members.remove(member)
        return True

    def get_all_members(self):
        return [member.to_dict() for member in self.members]


def demo():
    family = Family(last_name="Jackson")

    family.add_member("John", 33, [7, 13, 22])
    family.add_member("Jane", 31, [3, 9, 19])

    print("Initial family:")
    print(family.get_all_members())

    deleted = family.delete_member(1)
    print("Member with id=1 deleted?", deleted)

    print("Current family:")
    print(family.get_all_members())


if __name__ == "__main__":
    demo()
