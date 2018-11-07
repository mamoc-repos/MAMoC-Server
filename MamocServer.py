from os import environ

import psutil as psutil
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner

from java_classes.JavaExecutor import JavaExecutor


def main():
    import six

    url = environ.get("MAMOC_ROUTER", u"ws://localhost:8080/ws")
    if six.PY2 and type(url) == six.binary_type:
        url = url.decode('utf8')
    realm = u"mamoc_realm"
    runner = ApplicationRunner(url, realm)
    runner.run(MamocServer)


class MamocServer(ApplicationSession):

    def __init__(self, config=None):
        ApplicationSession.__init__(self, config)
        self.traceback_app = True

    async def onJoin(self, details):
        print("Mamoc Server attached on {}".format(details.session))

        cpu = psutil.cpu_freq().max * psutil.cpu_count()
        mem = round(psutil.virtual_memory().total / 1000000)
        battery = psutil.sensors_battery().percent

        print("total max cpu freq: ",  cpu)
        print("memory: ", mem)
        print("battery: ", battery)

        self.publish('uk.ac.standrews.cs.mamoc.stats', cpu, mem, battery)
        print("published server stats")

        async def on_offloding_event(source, rpcname, code, resourcename, params):
            print("Received from: {} app".format(source))
            print("Received RCP name: {}".format(rpcname))
            print("Received the source code: {}".format(code))
            print("Received params: {}".format(params))

            if source == "Android":
                code = code[code.find('import'):]  # remove the package name
                code = self.removeannotations(code)  # remove the annotations as we do need them anymore
                class_name = self.findclassname(code)  # identify the class name for javac command
                code = self.addmainmethod(class_name, code, resourcename, params)  # Add the main method for java command

                if resourcename != "None":
                    code = "import java.nio.file.Files;\nimport java.nio.file.Paths;\nimport java.io.IOException;" + code
                    code = self.addResourceCode(code)

                with open("java_classes/{}.java".format(class_name), "w") as java_file:
                    print("{}".format(code), file=java_file)

                executor = JavaExecutor()
                result = executor.startExecuting(class_name, "{}.java".format(class_name), params)

                print(result)

                if result:  # if building and execution were successful
                    # send back output and duration in seconds
                    output = result[0]
                    duration = result[1]

                    if output == b'':  # empty byte array
                        output = "nothing"
                    else:
                        output = output.decode("utf-8")

                    self.publish('uk.ac.standrews.cs.mamoc.offloadingresult', output, duration)

                    # register the procedure for next time rcp request
                    await self.register(executor.execute_java(class_name, params), rpcname)
                    print("ServerComponent: {}  registered!".format(rpcname))

            elif source == "iOS":
                print("received from iOS app")
            else:
                print("unrecognized source!")

        sub = await self.subscribe(on_offloding_event, "uk.ac.standrews.cs.mamoc.offloading")
        print("Subscribed to uk.ac.standrews.cs.mamoc.offloading with {}".format(sub.id))

    def onDisconnect(self):
        print("disconnected")
        # if reactor.running:
        #     reactor.stop()

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


if __name__ == '__main__':
    main()
