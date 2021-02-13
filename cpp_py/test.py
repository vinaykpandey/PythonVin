import subprocess

print("Inside Python file")
subprocess.call(["g++", "vins_test.cpp", "-o", "vins_test.out"])
subprocess.call("./vins_test.out")
print("Task is done in Python")
