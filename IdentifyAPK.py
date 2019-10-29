platform_file = open("Android-API-Files/android_platform_packages.txt", "r")
platform_lines = platform_file.read().splitlines()
platform_list = ["L" + p.replace('.', '/') for p in platform_lines]

support_file = open("Android-API-Files/android_support_packages.txt", "r")
support_lines = support_file.read().splitlines()
support_list = ["L" + s.replace('.', '/') for s in support_lines]

ignored_file = open("Android-API-Files/ignored.list", "r")
ignored_lines = ignored_file.read().splitlines()
ignored_list = ["L" + s.replace('.', '/') for s in support_lines]

api_candidates_with_L = platform_list + support_list + ignored_list
api_candidates = platform_lines + support_lines + ignored_lines


def filter_internal_classes(d):
    classes = d.get_classes()
    filtered_classes = []
    methods = 0

    # Check if the class is an Android library class
    for c in classes:
        c_methods = len(c.get_methods())
        methods += c_methods
        if not c.get_vm_class().get_name().startswith(tuple(api_candidates_with_L)):
                # and not c.is_external():
            filtered_classes.append(c)
            print(c)

    print("Number of classes in the app: ", len(classes))
    print("Number of methods in the app: ", methods)
    print("Number of filtered classes: ", len(filtered_classes))

    return filtered_classes, methods, len(classes)


def identify(a, d):

    filtered_classes, methods, orig_classes = filter_internal_classes(d)
    class_codes = []
    offloadables = []

    for c in filtered_classes:
        try:
            c.get_vm_class().get_source()
            class_codes.append(c.get_vm_class().get_source())
        except AttributeError:
            print("code not found for ", c.get_vm_class().get_name())
    print("Number of classes with codes: ", len(class_codes))

    for code in class_codes:
        codeArray = code.split(' ')

        # Check if it is class (not interface)
        if 'class' in codeArray:
            android_match = False
            for c in codeArray:
                if c.startswith(tuple(api_candidates)):
                    android_match = True
                    break

            if not android_match:
                offloadables.append(code)

    print("Number of offloadable classes: ", len(offloadables))
    return orig_classes, methods, len(filtered_classes), len(class_codes), offloadables

    # method_codes = []
    # offloadables = []
    #
    # for c in classes:
    #     methods = c.get_vm_class().get_methods()
    #     for m in methods:
    #         method_code = m.source()
    #         print(m, "\n", method_code)
    #         if method_code is not None:
    #             method_codes.append(method_code)
    #
    # print("Number of methods with codes: ", len(method_codes))
    #
    # for code in method_codes:
    #     if not code.contains(tuple(api_candidates)):
    #         offloadables.append(code)


def AnnotateOffloadables(a, offlodables):
    for off in offlodables:
        class_loc = off.find('class')
        if class_loc is not None:
            if off[class_loc-1] is "public" or off[class_loc-1] is "final":
                annotated_off = off[:class_loc-1] + "@Offloadable\n" + off[class_loc-1:]
            else:
                annotated_off = off[:class_loc] + "@Offloadable\n" + off[class_loc:]
            print(annotated_off)
