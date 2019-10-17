# from smalisca.core.smalisca_main import SmaliscaApp
# from smalisca.modules.module_smali_parser import SmaliParser
#
# import os
#
# app = SmaliscaApp()
# app.setup()
#
# # Set log level
# app.log.set_level('info')
#
# # Specify the location where your APK_files has been dumped
# location = '/Users/dawan/Dropbox/PhD/implementations/Android/PrimeCounter/app/build/outputs/apk/debug/app-debug/smali'
#
# print(os.path.exists(location))
#
# # Specify file name suffix
# suffix = 'smali'
#
# # Create a new parser
# parser = SmaliParser(location, suffix)
#
# # Go for it!
# parser.run()
#
# # Get results
# results = parser.get_results()
#
# print(results)