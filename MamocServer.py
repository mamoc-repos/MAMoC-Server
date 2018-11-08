from os import environ

from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner

from java_classes.JavaExecutor import JavaExecutor
from StatsCollector import StatsCollector
from Transformer import Transformer


def main():
    import six

    url = environ.get("MAMOC_ROUTER", u"ws://127.0.0.1:8080/ws")
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
        cpu, mem, battery = StatsCollector.fetchstats()

        self.publish('uk.ac.standrews.cs.mamoc.stats', cpu, mem, battery)
        print("published server stats")

        async def on_offloding_event(source, rpcname, code, resourcename, params):
            print("Received from: {} app".format(source))
            print("Received RCP name: {}".format(rpcname))
            print("Received the source code: {}".format(code))
            print("Received params: {}".format(params))

            if source == "Android":
                code, class_name = Transformer(code, resourcename, params).start()

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

                    # register the procedure for next time rpc request
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


if __name__ == '__main__':
    main()
