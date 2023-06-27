import pytest

import calculationPython


class TestCal(object):


    @classmethod
    def setup_class(cls):
        print('start')
        cls.cal = calculationPython.Call()


    @classmethod
    def teardown_class(cls):
        print('end')
        del cls.cal

    def setUp_method(self, method):
        print('method={}'.format(method.__name__))

    def tearDown_method(self, method):
        print('method={}'.format(method.__name__))

    def test_add_num_and_double(self, request):
        os_name=  request.config.getoption('--os-name')
        print(os_name)
        if os_name == 'mac':
            print('ls')
        elif os_name == 'windows':
            print('dir')
        assert self.cal.add_num_add_double(1, 1) == 4

    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num_add_double('1', '1')
