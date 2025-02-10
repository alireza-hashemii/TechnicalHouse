class Contact:
    contact_list : set["Contact"] = list()
    
    def __init__(self, name:str, email:str) -> None:
        self.name = name
        self.email = email

        if not self in Contact.contact_list:
            Contact.contact_list.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.email})"

cnt1 = Contact("Ali", "ali_000@gmail.com")
cnt2 = Contact("Amir", "amir_000@gmail.com")

print(cnt1.contact_list)
print(set(Contact.contact_list))
print(len(Contact.contact_list))