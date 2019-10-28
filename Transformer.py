
class Transformer(object):

    def __init__(self, code, resourcename, params):
        self.code = code
        self.resourcename = resourcename
        self.params = params

    def start(self, type="class"):
        if type == "class":
            code = self.code[self.code.find('import'):]  # remove the package name
            code = self.removeannotations(code)  # remove the annotations as we do need them anymore
            class_name = self.findclassname(code)  # identify the class name for javac command
            code = self.addmainmethod(class_name, code, self.resourcename, self.params)  # Add the main method for java command

            if self.resourcename is not None:
                code = "import java.nio.file.Files;\nimport java.nio.file.Paths;\nimport java.io.IOException;" + code
                code = self.addResourceCode(code)

            return code, class_name
        elif type == "method":
            code = self.removeannotations(self.code)  # remove the annotations as we do need them anymore
            method_name = self.findmethodname(code)
            code, method_class_name = self.generateclass(code, method_name)

            if self.resourcename is not None:
                code = "import java.nio.file.Files;\nimport java.nio.file.Paths;\nimport java.io.IOException;" + code
                code = self.addResourceCode(code)

            return code, method_class_name
        else:
            print("Unknown offloading type!")
            return

    def findclassname(self, source):
        list_of_words = source.split()
        class_name = list_of_words[list_of_words.index("class") + 1]  # find the name of the class sent
        return class_name

    def removeannotations(self, code):
        code = code.replace("import uk.ac.standrews.cs.mamoc_client.Annotation.Offloadable;", "")
        annotation_line = code.split("@Offloadable")[-1].split("\n", 1)[0]
        code = code.replace("@Offloadable", "")
        code = code.replace(annotation_line, "")

        code = code.replace("this = new Object();", "")  # remove this in constructor added by dex decompiler
        code = code.replace("new Object()", "this")  # sometimes the dex decompiler changes this to new Object()

        return code

    def addmainmethod(self, class_name, source, resourcename, params):
        firstopenbrace = source.find("{") + 1  # we want to place the main method after the first occurrence of braces

        mainmethod = f"\n\n\tpublic static void main(String[] args){{\n\t\t"

        return_type = source.split("run()", 1)[0].split(" ")[-2]  # get the return type of run() method

        if return_type != "void":
            mainmethod += "System.out.print("

        mainmethod += f"new {class_name}("
        addargs = 0
        if resourcename is not None:
            mainmethod += f"readResourceContent(\"../data/\" + args[0])"
            addargs += 1

        for index, param in enumerate(params):
            parser = self.getParser(param)

            if index > 0 or resourcename is not None:
                mainmethod += ", "

            if parser is None:
                mainmethod += f"args[{index + addargs}]"
            else:
                mainmethod += f"{parser}args[{index + addargs}])"

        mainmethod += ").run()"

        if return_type != "void":
            mainmethod += ");\n\t}"  # end the system print out statement
        else:
            mainmethod += ";\n\t}"

        return source[:firstopenbrace] + mainmethod + source[firstopenbrace:]

    def getParser(self, param):
        if type(param) is float:
            return "Double.ParseDouble("
        elif type(param) is int:
            return "Integer.parseInt("

    def addResourceCode(self, source):
        firstopenbrace = source.find("{") + 1  # we want to place the resource method after the first occurrence of braces

        resourcemethod = """\n\n\tpublic static String readResourceContent(String filePath){\n
        \t\ttry {\n
        \t\t\treturn new String(Files.readAllBytes(Paths.get(filePath)));\n
        \t\t} catch (IOException e) {\n
        \t\t\te.printStackTrace();\n
        \t\t\treturn null;\t\t\n\t\t}\n\t}"""

        return source[:firstopenbrace] + resourcemethod + source[firstopenbrace:]

    def findmethodname(self, source):
        list_of_words = source.split()
        print(list_of_words)
        method_name = list_of_words[list_of_words.index("void") + 1]  # find the name of the method sent
        print(method_name)
        return method_name

    def generateclass(self, source, method_name):
        class_name = method_name + "Class"

        class_header = f"public class {class_name}{{\n\t"
        mainmethod = f"\n\n\tpublic static void main(String[] args){{\n\t\t"

        # return_type = source.split(f"{method_name}", 1)[0].split(" ")[-2]  # get the return type of the method

        mainmethod += f"new {class_name}().{method_name}(); \n\t}}"

        return class_header + mainmethod + source + "\n}", class_name
