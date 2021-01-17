from tests.actual import method, Clazz


def helper_method():
    print('--- helper:', method(666))


class HelperClass:
    def helper(self):
        print('helper:', Clazz(111).class_method(666))
