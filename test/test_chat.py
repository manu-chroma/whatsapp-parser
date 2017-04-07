import sys
import unittest

from wp_parser.wp_chat import main as parser

# for capturing print() output
from contextlib import contextmanager
try:
    from StringIO import StringIO
except ImportError: #python3
    from io import StringIO


@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class TestChat(unittest.TestCase):
    def test_chat_1(self):
        # out_filename = str(tmpdir.join("abc"))
        # out_filename = ""

        for case in ['One', 'Two']:
            # creating mock args
            args = "-f test/testChat2.txt --root Username{}".format(case).split()

            with captured_output() as (result, err):
                parser(args)

            expected_file = 'test/out/testChat2_Username{}.out'.format(case)
            with open(expected_file) as fh:
                expected = fh.read()

            self.assertEqual(result.getvalue().strip(), expected)
