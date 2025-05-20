class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        
    def get_info(self):
        return f"{self.name}"
   
class Member(Person):
    def __init__(self, name, email, mem_id):
        super().__init__(name, email)
        self.mem_id = mem_id

    def get_info(self):
        return f"My name is {self.name}"
        
                     
member = Member("Farhat", "farhatnaz@hotmail.com", 1)
print(member.mem_id)
print(member.name)  
print(member.get_info())                  