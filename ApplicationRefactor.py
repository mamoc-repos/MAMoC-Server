import time
from androguard.misc import AnalyzeAPK, sign_apk

import IdentifyAPK
from download_apk import download_apk

apk_list = ['org.moire.opensudoku']


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

        # Annotate the offloadables
        IdentifyAPK.AnnotateOffloadables(a, offloadbables)

        # compile and sign the APK_files
        # sign_apk(a)

        time_spent = time.time() - tic

        print(time_spent)


for apk in apk_list:
    ApplicationRefactor.refactor(apk)