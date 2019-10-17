import time
from androguard.misc import AnalyzeAPK, sign_apk

import IdentifyAPK
from download_apk import download_apk

apk_ids = []
apk_list = open("top100.txt", "r")
lines = apk_list.read().splitlines()
for line in lines:
    apk_ids.append(line.split(' ')[-1])

output_file =

class ApplicationRefactor:

    @classmethod
    def refactor(cls, app_id):
        tic = time.time()

        # Download the APK file
        download_apk(app_id)

        # Analyze the APK_files in the /APK_files folder
        a, d, dx = AnalyzeAPK('APK_files/{}.apk'.format(app_id))

        # Identify Offloadables
        offloadbables = IdentifyAPK.identify(a, dx)

        # Annotate the offloadables and
        # IdentifyAPK.AnnotateOffloadables(a, offloadbables)

        # compile and sign the APK_files
        # sign_apk(a)

        time_spent = time.time() - tic

        print('{:4f}'.format(time_spent))


def main():
    for apk in apk_ids:
        ApplicationRefactor.refactor(apk)


if __name__ == '__main__':
    main()