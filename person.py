class Person:
  def __init__(self, name, email, phone):
    self.name = name
    self.email = email
    self.phone = phone
    self.friends = []
    self.greeting_count = 0

  def greet(self, other_person):
    print(f"Hello {other_person.name}, I am {self.name}!")

  def print_contact_info(self):
    print(f"{self.name}'s email: {self.email}")
    print(f"{self.name}'s email: {self.email}")

  def add_friend(self, other_person):
    self.friends.append(other_person)
    print(f"{other_person.name}")