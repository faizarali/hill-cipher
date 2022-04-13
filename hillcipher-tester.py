import sys
import subprocess
import shlex

def compile_c(c_file):
    cmd = 'gcc ' + c_file
    process = subprocess.Popen(shlex.split(cmd))
    process.wait()
    return './a.out'

def compile_cpp(cpp_file):
    cmd = 'g++ ' + cpp_file
    process = subprocess.Popen(shlex.split(cmd))
    process.wait()
    return './a.out'

def compile_java(java_file):
    cmd = 'javac ' + java_file
    process = subprocess.Popen(shlex.split(cmd))
    process.wait()
    return 'java hillcipher'

def compile_go(go_file):
    cmd = 'go build ' + go_file
    process = subprocess.Popen(shlex.split(cmd))
    process.wait()
    return './hillcipher'

def compile_py(py_file):
    return 'python3 hillcipher.py'

if len(sys.argv) != 2:
    print('Usage: python3 hillcipher-tester.py [filename]')
    sys.exit(1)

arg = sys.argv[1]

if arg == 'hillcipher.c':
    EXE = compile_c(arg)
elif arg == 'hillcipher.cpp':
    EXE = compile_cpp(arg)
elif arg == 'hillcipher.java':
    EXE = compile_java(arg)
elif arg == 'hillcipher.go':
    EXE = compile_go(arg)
elif arg == 'hillcipher.py':
    EXE = compile_py(arg)
else:
    print('Invalid source file name')
    sys.exit(1)

test_case_num = 7

# Accounts for seven test cases
for i in range(1, test_case_num + 1):
    print(f'Case #{i}')
    input = EXE + f' k{i}.txt p{i}.txt'
    command = shlex.split(input)
    with open(f'myOutput{i}.txt', 'w') as outfile:
        p = subprocess.Popen(command, stdout=outfile)
        p.wait()
    input = f'diff myOutput{i}.txt sample_output/k{i}p{i}.txt'
    p = subprocess.Popen(shlex.split(input))
    p.wait()
    print(f'Case #{i} - complete')
