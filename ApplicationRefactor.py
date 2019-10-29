import time
# Uncomment if you want to use the JADX decompiler instead of the built-in decompiler provided by Androguard
# import pyjadx
# from androguard.core.analysis.analysis import Analysis
# from androguard.core.androconf import show_logging
# from androguard.core.bytecodes.apk import APK
# from androguard.core.bytecodes.dvm import DalvikVMFormat
# from androguard.decompiler.decompiler import DecompilerJADX

from androguard.misc import AnalyzeAPK

import IdentifyAPK
from download_apk import download_apk

apk_ids = []
apk_list = open("top100.txt", "r")
#apk_list = open("apps_list.txt", "r")
output_file = open("output/refactor_results.txt", "w")
output_file.write("APP_ID" + " " + "Classes" + " " + "Methods" + " " + "Filtered" + " " + "Has_Code" + " " + "Offloadables" + " " + "Time\n")
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

        # Uncomment if you want to use the JADX decompiler instead of the built-in decompiler provided by Androguard
        # jadx = pyjadx.Jadx()
        # app = jadx.load('APK_files/{}.apk'.format(app_id))
        #
        # for cls in app.classes:
        #     print(cls.code)

        # # Load our example APK
        # a = APK('APK_files/{}.apk'.format(app_id))
        # # Create DalvikVMFormat Object
        # d = DalvikVMFormat(a)
        # # Create Analysis Object
        # dx = Analysis(d)
        # # Load the decompiler
        # # Make sure that the jadx executable is found in $PATH
        # # or use the argument jadx="/path/to/jadx" to point to the executable
        # decompiler = DecompilerJADX(d, dx, keepfiles=True)
        # # propagate decompiler and analysis back to DalvikVMFormat
        # d.set_decompiler(decompiler)
        # d.set_vmanalysis(dx)
        #
        # for c in d.get_classes():
        #     # print(c)
        #     print(decompiler.get_source_class(c))

        # Identify Offloadables
        classes, methods, filtered_classes, class_codes, offloadables = IdentifyAPK.identify(a, dx)
        # output_file.write(str(classes) + " " + str(methods) + " " + str(filtered_classes) + " " + str(class_codes) + " " + str(len(offloadables)) + "\n")

        # Annotate the offloadables and
        # IdentifyAPK.AnnotateOffloadables(a, offloadbables)

        # compile and sign the APK_files
        # sign_apk(a)

        time_spent = time.time() - tic

        print('{:4f}'.format(time_spent))
        output_file.write(str(classes) + " " + str(methods) + " " + str(filtered_classes) + " " + str(class_codes) + " " + str(len(offloadables)) + " " + str('{:2f}'.format(time_spent)) + "\n")

def main():
    for apk in apk_ids:
        output_file.write(apk + " ")
        ApplicationRefactor.refactor(apk)


if __name__ == '__main__':
    main()
