from unittest import TestCase

from framework.lang.error import stacktrace


class TestError(TestCase):
    def test_stacktrace(self):
        expected = [
            'Traceback (most recent call last):\n',
            '  File "/opt/app/tests/unit/framework/lang/test_error.py", line 24, in test_stacktrace\n    raise TypeError(\'hogehoge\')\n',
            'TypeError: hogehoge\n',
            '\nThe above exception was the direct cause of the following exception:\n\n',
            'Traceback (most recent call last):\n',
            '  File "/opt/app/tests/unit/framework/lang/test_error.py", line 26, in test_stacktrace\n    raise ValueError(\'fugafuga\') from e\n',
            'ValueError: fugafuga\n',
            '\nThe above exception was the direct cause of the following exception:\n\n',
            'Traceback (most recent call last):\n',
            '  File "/opt/app/tests/unit/framework/lang/test_error.py", line 28, in test_stacktrace\n    raise Exception(\'piyopiyo\') from e\n',
            'Exception: piyopiyo\n',
        ]
        try:
            try:
                try:
                    raise TypeError('hogehoge')
                except Exception as e:
                    raise ValueError('fugafuga') from e
            except Exception as e:
                raise Exception('piyopiyo') from e
        except Exception as e:
            self.assertEqual(stacktrace(e), expected)