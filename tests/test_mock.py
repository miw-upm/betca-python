from unittest import TestCase, mock
from unittest.mock import Mock

from tests import helper
from tests.actual import Clazz
from tests.helper import helper_method, HelperClass


def fake_method(arg):
    print('*** mock... arg:', arg)
    return -111


class TestDemo(TestCase):

    def test_one(self):
        helper_method()

    @mock.patch('tests.helper.method', return_value=0)  # en que lugar se realiza la llamada que queremos cambiar
    def test_two_a(self, mocked_method):
        helper_method()
        mocked_method.assert_called()  # assert_called_once(), assert_not_called()

    @mock.patch('tests.helper.method', side_effect=fake_method)
    def test_two_b(self, mocked_method):
        helper_method()
        mocked_method.assert_called_with(666)  # assert_called_once_with(), assert_any_call()

    def test_three_a(self):
        mocker = helper  # module or class
        mocker.method = Mock(return_value=0)
        helper_method()
        mocker.method.assert_called()

    def test_three_b(self):
        module = helper
        module.method = Mock(side_effect=fake_method)
        helper_method()
        module.method.assert_called()

    def test_four(self):
        HelperClass().helper()

    @mock.patch('tests.actual.Clazz.class_method', return_value=0)
    def test_five_a(self, mocked_method):
        HelperClass().helper()
        mocked_method.assert_called_once()

    @mock.patch('tests.actual.Clazz.class_method', side_effect=fake_method)
    def test_five_b(self, method):
        HelperClass().helper()
        method.assert_called_with(666)

    def test_six_a(self):
        mocker = Clazz  # module or class
        mocker.class_method = Mock(return_value=0)
        HelperClass().helper()
        mocker.class_method.assert_called_once()

    def test_six_b(self):
        mocker = Clazz  # module or class
        mocker.class_method = Mock(side_effect=fake_method)
        HelperClass().helper()
        mocker.class_method.assert_called_with(666)
