

class Transformer(object):

    def __init__(self, code, resourcename, params):
        self.code = code
        self.resourcename = resourcename
        self.params = params

    def start(self):
        code = self.code[self.code.find('import'):]  # remove the package name
        code = self.removeannotations(code)  # remove the annotations as we do need them anymore
        class_name = self.findclassname(code)  # identify the class name for javac command
        code = self.addmainmethod(class_name, code, self.resourcename, self.params)  # Add the main method for java command

        if self.resourcename != "None":
            code = "import java.nio.file.Files;\nimport java.nio.file.Paths;\nimport java.io.IOException;" + code
            code = self.addResourceCode(code)

        return code, class_name

    def findclassname(self, source):
        list_of_words = source.split()
        class_name = list_of_words[list_of_words.index("class") + 1]  # find the name of the class sent
        return class_name

    def removeannotations(self, code):
        code = code.replace("import uk.ac.st_andrews.cs.mamoc_client.Annotation.Offloadable;", "")
        code = code.replace("@Offloadable", "")
        code = code.replace("(resourceDependent = true, parallelizable = true)", "")

        code = code.replace("this = new Object();", "")  # remove this in constructor
        code = code.replace("new Object()", "this")  # sometimes the decompiler changes this to new Object()

        return code

    def addmainmethod(self, class_name, source, resourcename, params):
        firstopenbrace = source.find("{") + 1  # we want to place the main method after the first occurrence of braces

        mainmethod = f"\n\n\tpublic static void main(String[] args){{\n\t\t"

        return_type = source.split("run()", 1)[0].split(" ")[-2]  # get the return type of run() method

        if return_type != "void":
            mainmethod += "System.out.print("

        mainmethod += f"new {class_name}("

        if resourcename != "None":
            mainmethod += f"readResourceContent(\"../data/{resourcename}.txt\")"

        for index, param in enumerate(params):
            parser = self.getParser(param)

            if index > 0 or resourcename != "None":
                mainmethod += ", "

            if parser is None:
                mainmethod += f"args[{index}]"
            else:
                mainmethod += f"{parser}args[{index}])"

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

        resourcemethod = f"\n\n\tpublic static String readResourceContent(String filePath){{\n"
        resourcemethod += "\t\ttry {\n"
        resourcemethod += "\t\t\treturn new String(Files.readAllBytes(Paths.get(filePath)));\n"
        resourcemethod += "\t\t} catch (IOException e) {\n"
        resourcemethod += "\t\t\te.printStackTrace();\n"
        resourcemethod += "\t\t\treturn null;\t\t\n\t\t}\n\t}"

        return source[:firstopenbrace] + resourcemethod + source[firstopenbrace:]