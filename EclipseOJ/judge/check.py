import os
import subprocess
def bashfunc(filename,testcase,number):
    if filename.endswith('.cpp'):
        bashCommand = "g++ -std=c++14 {0}".format(filename)
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        if process.communicate()[1]:
            return "Compilation Error"
        else:
            inputs = testcase + "input_"
            outputs = testcase + "output_"
            correct = 0
            for i in range(number):
                inpi = inputs + str(i+1)
                outi = outputs + str(i+1)
                command1 = "./a.out < {0} > tempout.txt".format(inpi)
                command2 = "diff tempout.txt {0} > diff.txt".format(outi)
                os.system(command1)
                os.system(command2)
                if os.stat("diff.txt").st_size == 0:
                    correct += 1
                else:
                    return "Wrong Answer"
            return "Accepted"
    if filename.endswith('.py'):
        inputs = testcase + "input_"
        outputs = testcase + "output_"
        correct = 0
        for i in range(number):
            inpi = inputs + str(i+1)
            outi = outputs + str(i+1)
            command1 = "python3 {0} < {1} > tempout.txt".format(filename,inpi)
            command2 = "diff tempout.txt {0} > diff.txt".format(outi)
            os.system(command1)
            os.system(command2)
            if os.stat("diff.txt").st_size == 0:
                correct += 1
            else:
                return "Wrong Answer"
        return "Accepted"
    if filename.endswith('.java'):
        bashCommand = "javac {0}".format(filename)
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        if process.communicate()[1]:
            return "Compilation Error"
        else:
            inputs = testcase + "input_"
            outputs = testcase + "output_"
            correct = 0
            filei = filename[:-5]
            for i in range(number):
                inpi = inputs + str(i+1)
                outi = outputs + str(i+1)
                command1 = "java {0} < {1} > tempout.txt".format(filei,inpi)
                command2 = "diff tempout.txt {0} > diff.txt".format(outi)
                os.system(command1)
                os.system(command2)
                if os.stat("diff.txt").st_size == 0:
                    correct += 1
                else:
                    return "Wrong Answer"
            return "Accepted"
