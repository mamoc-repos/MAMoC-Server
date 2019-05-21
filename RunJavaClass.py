import os
# try:
import jpype

# KeyError:
#     os.environ['JDK_HOME'] = "/Library/Java/JavaVirtualMachines/1.6.0.jdk"
#     os.environ['JAVA_HOME'] = "/Library/Java/JavaVirtualMachines/1.6.0.jdk"

import time


class RunJavaClass:

    def run(self):
        # cpopt = "-Djava.class.path=%s" % './java_classes'
        jpype.startJVM(jpype.get_default_jvm_path(), '-ea',
                       '-Djava.class.path=/Users/dawan/PycharmProjects/mamoc_server/java_classes')

        # print(jpype.get_default_jvm_path())

        # hey = jpype.java.lang.System.out.println("hello world")
        # print(hey)

        # testPkg = jpype.JPackage('uk').standrews.cs.mamoc

        quick = jpype.JClass("QuickSort")

        tic = time.time()

        text_file = "./data/" + "medium" + ".txt"
        with open(text_file, "r") as file:
            content = file.read().split(" ")

        quick.quickSort(content)  # uk.ac.standrews.cs.mamoc.NQueens

        duration = time.time() - tic
        print(duration)

        return duration


if __name__ == "__main__":
    RunJavaClass().run()

