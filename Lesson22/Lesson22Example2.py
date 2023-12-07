#During work with files exceptions are possible.
#You can use try except blocks to handle such issues.
try:
    file2 = open("file2.txt", "w")
    try:
        file2.write("Python is a solid choice.")
    except Exception as exInner:
        print(exInner)
    finally:
        file2.close()
except Exception as exOuter:
    print(exOuter)


