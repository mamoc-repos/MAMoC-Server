from sys import exit
import asyncio

from autobahn.asyncio.component import Component, run
from autobahn.wamp import CallOptions

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
public void say_hello () {
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
            # u"url": u"wss://djs21.host.cs.st-andrews.ac.uk/offload/ws/", # Connecting to student host
            # u"endpoint": {
            #     u"type": u"tcp",
            #     u"host": u"djs21.host.cs.st-andrews.ac.uk/offload/ws",
            #     u"port": 3004,
            # },
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

    print("joined {}: {}".format(session, details))

    def on_progress(i):
        print("Progress: {}".format(i))

    res = await session.call(u'uk.ac.standrews.cs.mamoc.sendfile', 3, options=CallOptions(on_progress=on_progress))

    print("Final: {}".format(res))

    while True:
        choice = present_menu()

        if choice == 1:
            await class_offloading(session)
        elif choice == 2:
            await method_offloading(session)
        elif choice == 3:
            exit()


def present_menu():
    print(""""
    1. Class offloading\t2. Method offloading\t3. Quit
    """)

    choice = int(input("\nPlease select one of the three options: \n"))

    while choice < 1 or choice > 3:
        print("The selection provided is invalid.")
        choice = int(input("\nPlease select one of the three options: \n"))

    return choice


async def class_offloading(session):
    try:
        await print_result(class_id, session)
    except Exception as e:
        print("class call error: {0}".format(e))
        # if the RPC is not registered in the server, publish the source code
        session.publish("uk.ac.standrews.cs.mamoc.offloading", "Android", class_id, class_code, "large", ["hi"])
        # await print_result(class_id, session)


async def print_result(passed_id, session):
    print("called ID: ", passed_id)

    res = await session.call(passed_id, ["hi"])
    if res[2] is None:
        print("output: {}".format(res[0]))
        print("duration: {}".format(res[1]))
    else:
        print("RPC execution error")


async def method_offloading(session):
    try:
        await print_result(method_id, session)
    except Exception as e:
        print("method call error: {0}".format(e))
        # if the RPC is not registered in the server, publish the source code
        session.publish("uk.ac.standrews.cs.mamoc.offloading", "Android", method_id, method_code, "None", ["hi"])
        # await print_result(method_id, session)


@component.subscribe("uk.ac.standrews.cs.mamoc.offloadingresult")
async def result_returned(result, duration):
    print("execution returned {} took {} seconds".format(result, duration))


@component.on_disconnect
async def disconnected():
    print("Disconnected from the server!")
    asyncio.get_event_loop().stop()

if __name__ == "__main__":
    run([component])
