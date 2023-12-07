#Built-in modules in Python
import platform

platformInfo = platform.system()
print(platformInfo)

platformFunctionsList = dir(platform)
for i in platformFunctionsList:
    print(i)
