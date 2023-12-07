#isinstance function helps to check object type
class PythonDeveloper:
    def projectPython(self):
        print("Python coding in process.")
        
class JavaDeveloper:
    def projectJava(self):
        print("Java coding in process.")
        
developer1 = JavaDeveloper()

if isinstance(developer1,PythonDeveloper):
    print("This is PythonDeveloper object.")
    
elif isinstance(developer1, JavaDeveloper):
    print("This is JavaDeveloper object.")
    
else:
    print("Unknown object type.")

