class FullName:
    def __init__(self, fname, lname) -> None:
        self.fname = fname
        self.lname = lname
    def get_name(self):
        return f"""
==========================
|| Name:    {self.fname}  ||
|| Surname: {self.lname} ||
==========================
"""

        
a = 'Nusratillo'
b = 'Xursanjonov'

f = FullName(a, b)

print(f.get_name())