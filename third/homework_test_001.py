import sys
print(sys.path)


print(__file__)

try:
    import mommod
except ImportError:
    print("Didn’t work first time")
else:
    print("Worked first time")
sys.path.pop(0)
try:
    import homework_013
except ImportError:
    print("Didn’t work second time")
else:
    print("Worked second time")


