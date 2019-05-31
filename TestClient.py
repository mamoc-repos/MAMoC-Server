from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner

from os import environ


# class ClientComponent(ApplicationSession):
#
#     def __init__(self, config=None):
#         ApplicationSession.__init__(self, config)
#         self.traceback_app = True
#         self.rpcname = "uk.ac.standrews.cs.mamoc.SearchText.KMP"

# async def onJoin(self, details):
#     print("session ready!")
#
#     try:
#         res = await self.call(self.rpcname, ["hi"])
#         print("KMP: {}".format(res))
#
#     except Exception as e:
#         print("call error: {0}".format(e))
#         # if the RPC is not registered in the server, publish the source code
#         self.publish("uk.ac.standrews.cs.mamoc.offloading", "Android", self.rpcname, self.code, "large", ["hi"])
#
#     async def on_event(result, duration):
#         print("execution returned {} took {} seconds".format(result, duration))
#         await self.sub.unsubscribe()
#
#         self.sub = await self.subscribe(self.on_event, "uk.ac.standrews.cs.mamoc.offloadingresult")
#         print("Subscribed to uk.ac.standrews.cs.mamoc.offloading with {}".format(self.sub.id))
#
# def onDisconnect(self):
#     print("disconnected")


# if __name__ == '__main__':
#     import six
#
#     url = environ.get("MAMOC_ROUTER", u"ws://127.0.0.1:8080/ws")
#     # url = environ.get("MAMOC_ROUTER", u"wss://djs21.host.cs.st-andrews.ac.uk/offload/ws")
#     if six.PY2 and type(url) == six.binary_type:
#         url = url.decode('utf8')
#     realm = u"mamoc_realm"
#     runner = ApplicationRunner(url, realm)
#     runner.run(ClientComponent)


from autobahn.asyncio.component import Component, run

class_id = "uk.ac.standrews.cs.mamoc.SearchText.KMP"
class_code = """
package uk.ac.standrews.cs.mamoc_demo.SearchText;

import uk.ac.standrews.cs.mamoc_client.Annotation.Offloadable;

@Offloadable(resourceDependent = true, parallelizable = true)
public class KMP {

    String content, pattern;

    public KMP(String content, String pattern) {
        this.content = content;
        this.pattern = pattern;
    }

    public int run() {
        int matches = 0;
        int M = pattern.length();
        int N = content.length();

        // create lps[] that will hold the longest
        // prefix suffix values for pattern
        int lps[] = new int[M];
        int j = 0; // index for pat[]

        // Preprocess the pattern (calculate lps[] array)
        computeLPSArray(pattern, M, lps);

        int i = 0; // index for txt[]
        while (i < N) {
            if (pattern.charAt(j) == content.charAt(i)) {
                j++;
                i++;
            }
            if (j == M) {
                matches++;
                j = lps[j - 1];
            }

            // mismatch after j matches
            else if (i < N && pattern.charAt(j) != content.charAt(i)) {
                // Do not match lps[0..lps[j-1]] characters,
                // they will match anyway
                if (j != 0)
                    j = lps[j - 1];
                else
                    i = i + 1;
            }
        }

        return matches;
    }

    private void computeLPSArray(String pat, int M, int lps[])
    {
        // length of the previous longest prefix suffix
        int len = 0;
        int i = 1;
        lps[0] = 0; // lps[0] is always 0

        // the loop calculates lps[i] for i = 1 to M-1
        while (i < M) {
            if (pat.charAt(i) == pat.charAt(len)) {
                len++;
                lps[i] = len;
                i++;
            }
            else // (pat[i] != pat[len])
            {
                // This is tricky. Consider the example.
                // AAACAAAA and i = 7. The idea is similar
                // to search step.
                if (len != 0) {
                    len = lps[len - 1];

                    // Also, note that we do not increment
                    // i here
                }
                else // if (len == 0)
                {
                    lps[i] = len;
                    i++;
                }
            }
        }
    }
}
"""
method_id = "uk.ac.standrews.cs.mamoc.say_hello"
method_code = """
@Offloadable(resourceDependent = false, parallelizable = true)
public void say_hello(){
    String hello = "Hello, World";
    System.out.print(hello);
}
"""
component = Component(
    # you can configure multiple transports; here we use two different
    # transports which both exist in the mamoc router
    transports=[
        {
            u"type": u"websocket",
            u"url": u"ws://127.0.0.1:8080/ws",
            u"endpoint": {
                u"type": u"tcp",
                u"host": u"localhost",
                u"port": 8080,
            },
            # you can set various websocket options here if you want
            u"options": {
                u"open_handshake_timeout": 100,
            }
        },
    ],
    # authentication can also be configured (this will only work on
    # the demo router on the first transport above)
    # authentication={
    #     u"cryptosign": {
    #         u'authid': u'alice',
    #         # this key should be loaded from disk, database etc never burned into code like this...
    #         u'privkey': '6e3a302aa67d55ffc2059efeb5cf679470b37a26ae9ac18693b56ea3d0cd331c',
    #     }
    # },
    # must provide a realm
    realm=u"mamoc_realm",
)


@component.on_join
async def join(session, details):
    try:
        res = await session.call(class_id, ["hi"])
        if res[2] is None:
            print("output: {}".format(res[0]))
            print("duration: {}".format(res[1]))
        else:
            print("RPC execution error")

    except Exception as e:
        print("call error: {0}".format(e))
        # if the RPC is not registered in the server, publish the source code
        # Testing class offloading
        session.publish("uk.ac.standrews.cs.mamoc.offloading", "Android", class_id, class_code, "large", ["hi"])
        # Testing method offloading
        session.publish("uk.ac.standrews.cs.mamoc.offloading", "Android", method_id, method_code, "None", ["hi"])

    # async def on_event(result, duration):
    #     await self.sub.unsubscribe()
    #
    #     self.sub = await self.subscribe(self.on_event, )
    #     print("Subscribed to uk.ac.standrews.cs.mamoc.offloading with {}".format(self.sub.id))

    print("joined {}: {}".format(session, details))
    # await sleep(1)
    # print("Calling 'com.example'")
    # res = await session.call(u"example.foo", 42, something="nothing")
    # print("Result: {}".format(res))
    # await session.leave()


@component.subscribe("uk.ac.standrews.cs.mamoc.offloadingresult")
async def result_returned(result, duration):
    print("execution returned {} took {} seconds".format(result, duration))


if __name__ == "__main__":
    run([component])
