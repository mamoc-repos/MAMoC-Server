platform_file = open("Android-API-Files/android_platform_packages.txt", "r")
platform_lines = platform_file.read().splitlines()
platform_list = ["L" + p.replace('.', '/') for p in platform_lines]

# print(platform_list)

support_file = open("Android-API-Files/android_support_packages.txt", "r")
support_lines = support_file.read().splitlines()
support_list = ["L" + s.replace('.', '/') for s in support_lines]

api_candidates = platform_list + support_list


def filter_internal_classes(dx):
    classes = dx.get_classes()
    filtered_classes = []
    methods = 0

    # Check if the class is an Android library class
    for c in classes:
        c_methods = len(c.get_vm_class().get_methods())
        methods += c_methods
        if not c.get_vm_class().get_name().startswith(tuple(api_candidates)):
            filtered_classes.append(c)

    print("Number of classes in the app: ", len(classes))
    print("Number of methods in the app: ", methods)
    print("Number of filtered classes: ", len(filtered_classes))

    return filtered_classes


def identify(a, dx):

    classes = filter_internal_classes(dx)
    class_codes = []
    offloadables = []

    for c in classes:
        code = c.get_vm_class().get_source()

        if code is not None:
            class_codes.append(code)

    print("Number of classes with codes: ", len(class_codes))

    for code in class_codes:
        codeArray = code.split(' ')
        print(codeArray)
        android_match = False
        for c in codeArray:
            if c.startswith(tuple(api_candidates)):
                android_match = True
                break

        if not android_match:
            offloadables.append(code)

    print("Number of offloadable classes: ", len(offloadables))
    return offloadables

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
        annotated_off = "@Offloadable" + off[:]
