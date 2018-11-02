from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner

from os import environ


class ClientComponent(ApplicationSession):

    def __init__(self, config=None):
        ApplicationSession.__init__(self, config)
        self.traceback_app = True
        self.rpcname = "uk.ac.standrews.cs.mamoc.SearchText.KMP"

    async def onJoin(self, details):
        print("session ready!")

        try:
            res = await self.call(self.rpcname, 13)
            print("Queens: {}".format(res))

        except Exception as e:
            print("call error: {0}".format(e))

        async def on_event(result, duration):
            print("execution returned {} took {} seconds".format(result, duration))
            await self.sub.unsubscribe()

        # try:
        #     res = await self.call('uk.ac.standrews.cs.mamoc.search', "large", "hi")
        #     print("Search: {}".format(res))
        #
        # except Exception as e:
        #     print("call error: {0}".format(e))

        self.publish("uk.ac.standrews.cs.mamoc.offloading",
                     "Android",
                     self.rpcname,
                     """
package uk.ac.standrews.cs.mamoc.SearchText;

import uk.ac.st_andrews.cs.mamoc_client.Annotation.Offloadable;
import uk.ac.st_andrews.cs.mamoc_client.Annotation.Parallelizable;
import uk.ac.st_andrews.cs.mamoc_client.Annotation.ResourceDependent;

@Offloadable
@Parallelizable
@ResourceDependent
public class KMP {

    String content;
    String pattern;

    public KMP(String content, String pat) {
        this.content = content;
        this.pattern = pat;
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
                        """,
                     "large",
                     ["hell"])

        self.sub = await self.subscribe(on_event, "uk.ac.standrews.cs.mamoc.offloadingresult")
        print("Subscribed to uk.ac.standrews.cs.mamoc.offloading with {}".format(self.sub.id))

    def onDisconnect(self):
        print("disconnected")
        # reactor.stop()


if __name__ == '__main__':
    import six

    url = environ.get("MAMOC_ROUTER", u"ws://127.0.0.1:8080/ws")
    if six.PY2 and type(url) == six.binary_type:
        url = url.decode('utf8')
    realm = u"mamoc_realm"
    runner = ApplicationRunner(url, realm)
    runner.run(ClientComponent)
