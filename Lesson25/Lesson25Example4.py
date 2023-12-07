#Python supports multiple inheritance
class PythonDeveloper:
    def projectPython(self):
        print("Python coding in process.")
        
class JavaDeveloper:
    def projectJava(self):
        print("Java coding in process.")
        
class PythonJavaDeveloper(PythonDeveloper, JavaDeveloper):
    pass

developer1 = PythonJavaDeveloper()
developer1.projectPython()
developer1.projectJava()


