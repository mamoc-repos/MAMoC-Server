import time
from androguard.misc import AnalyzeAPK, sign_apk

import IdentifyAPK
from download_apk import download_apk

apk_ids = []
apk_list = open("top100.txt", "r")
output_file = open("output/refactor_results.txt", "w")
output_file.write("APP_ID" + " " + "Classes" + " " + "Methods" + " " + "Filtered" + " " + "Has_Code" + " " + "Offloadables\n")
lines = apk_list.read().splitlines()
for line in lines:
    apk_ids.append(line.split(' ')[-1])

class ApplicationRefactor:

    @classmethod
    def refactor(cls, app_id):
        tic = time.time()

        # Download the APK file
        download_apk(app_id)

        # Analyze the APK_files in the /APK_files folder
        a, d, dx = AnalyzeAPK('APK_files/{}.apk'.format(app_id))

        # Identify Offloadables
        classes, methods, filtered_classes, class_codes, offloadables = IdentifyAPK.identify(a, dx)
        output_file.write(str(classes) + " " + str(methods) + " " + str(filtered_classes) + " " + str(class_codes)
                          + " " + str(len(offloadables)) + "\n")

        # Annotate the offloadables and
        # IdentifyAPK.AnnotateOffloadables(a, offloadbables)

        # compile and sign the APK_files
        # sign_apk(a)

        time_spent = time.time() - tic

        print('{:4f}'.format(time_spent))


def main():
    for apk in apk_ids:
        output_file.write(apk + " ")
        ApplicationRefactor.refactor(apk)


if __name__ == '__main__':
    main()