print("Hello, Work!")

# переменные
school = "ШВА"
SCHOOL_NAME = "ШВА"

# нейминг переменных
# school_name - переменные 
# SCHOOL_NAME - константы

school  = "dsadsa" #dsadasda

"""
dsadsadasd
"""

# типы данных
school = 1 # 1
school = str(school) # "1"
school = -2.3
school2 = "dsadas"
school = "d"
school = True
school = ["dsa", 312]
school[1]
school = {"dsa": "dsad", "dsadasd": 231}
school["dsadasd"]
school = ["dsa", 312, 321, 312]
school = set(school)


# циклы
for i in range(10):
    print(i)

schools = ["dsa", 312, 321, 312]
for school in schools:
    print(school)
        

# while True:
#     print("привет!")


schools_atmo = [
    "шва19", "шва20", "шва21", 
    "шва22", "шва23",
    "шва24"
]
dsa = [school[3:] for school in schools_atmo]
print(dsa)
dsa = [school[3:] for school in schools_atmo if int(school[3:]) >=20]
print(dsa)

# условия 
if "шва19" in schools_atmo:
    print("шва19 in schools_atmo")
    
new_var = "Yes" if "шва19" in schools_atmo else "No"
print(new_var)

# булен операторы
# or and not

# функции и типы
new_var: int
new_var: int = 10


def our_fun(text1, text: str = None) -> None:
    print(text1, text)
    return "dsa"
val = our_fun("не хай", 1)
val = our_fun("не хай")
print(val)


# классы
class MyClass:
    var2: str
    
    def __init__(self, var: str):
        self.var = var
    def another_fun(self):
        print("i'm another_fun")

myClass = MyClass(var="321312")
myClass.another_fun()