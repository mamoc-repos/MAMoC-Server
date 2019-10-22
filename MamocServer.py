from os import environ, path

from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner
from autobahn.wamp import ApplicationError, RegisterOptions

from JavaExecutor import JavaExecutor
from StatsCollector import StatsCollector
from Transformer import Transformer


def main():
    import six

    host = "127.0.0.1"
    port = "8080"

    url = environ.get("MAMOC_ROUTER", u"ws://"+host+":"+port+"/ws")
    if six.PY2 and type(url) == six.binary_type:
        url = url.decode('utf8')
    realm = u"mamoc_realm"
    runner = ApplicationRunner(url, realm)
    try:
        runner.run(MamocServer)
    except OSError:
        print("Failed to connect to Router!")
        print("Are you sure there is a router component running at: " + host + " at port: " + port + "?")


class MamocServer(ApplicationSession):

    def __init__(self, config=None):
        ApplicationSession.__init__(self, config)
        self.traceback_app = True
        self.executor = JavaExecutor()
        self.class_name = ""
        self.params = ""

    async def onJoin(self, details):
        print("Mamoc Server attached on {}".format(details.session))
        cpu, mem, battery = StatsCollector.fetchstats()

        self.publish('uk.ac.standrews.cs.mamoc.stats', cpu, mem, battery)
        print("published server stats")

        async def on_offloding_event(source, rpcname, code, resourcename, params):
            print("Received from: {} app".format(source))
            print("Received RCP name: {}".format(rpcname))
            print("Received the source code: {}".format(code))
            print("Received params: {}".format(params))

            if source == "Android":
                self.params = params

                # Java file already cached in MAMoC Repository
                if path.exists("java_classes/{}.java".format(self.class_name)):
                    result = self.executor.startExecuting(self.class_name, "{}.java".format(self.class_name), params)

                else:
                    # if it is a class, it must start with package keyword
                    if code.strip().split(' ', 1)[0] == "package":
                        code, self.class_name = Transformer(code, resourcename, params).start()
                    else:
                        code, self.class_name = Transformer(code, resourcename, params).start(type="method")

                    with open("java_classes/{}.java".format(self.class_name), "w") as java_file:
                        print("{}".format(code), file=java_file)

                    result = self.executor.startExecuting(self.class_name, "{}.java".format(self.class_name), params)

                print(result)

                if result:  # if building and execution were successful, send back output and duration in seconds
                    output = result[0]
                    duration = result[1]

                    output = self.decode_bytes(output)

                    self.publish('uk.ac.standrews.cs.mamoc.offloadingresult', output, duration)

                    # register the procedure for next time rpc request
                    try:
                        re = await self.register(self.execute_java, rpcname, options=RegisterOptions(invoke=u'roundrobin'))
                    except ApplicationError as e:
                        print("could not register procedure: {0}".format(e))
                    else:
                        print("{} endpoints registered".format(re))

            elif source == "iOS":
                print("received from iOS app")
            else:
                print("unrecognized source!")

        sub = await self.subscribe(on_offloding_event, "uk.ac.standrews.cs.mamoc.offloading")
        print("Subscribed to uk.ac.standrews.cs.mamoc.offloading with {}".format(sub.id))

    def execute_java(self, input):
        print("execute_java {} {}".format(self.class_name, input))
        output, duration, errors = self.executor.execute_java(self.class_name, input)
        output = self.decode_bytes(output)
        return output, duration, errors

    def decode_bytes(self, encoded):
        if encoded == b'':  # empty byte array
            encoded = "nothing"
        else:
            encoded = encoded.decode("utf-8")
        return encoded

    def onDisconnect(self):
        print("disconnected")


if __name__ == '__main__':
    main()
