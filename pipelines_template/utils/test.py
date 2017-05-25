"""Test helper functions."""
import os
import unittest

from resolwe.test import ProcessTestCase

TEST_FILES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tests', 'files'))
TEST_LARGE_FILES_DIR = os.path.join(TEST_FILES_DIR, 'large')


def skipUnlessLargeFiles(*files):  # pylint: disable=invalid-name
    r"""Skip decorated tests unless large files are available.

    :param list \*files: variable lenght files list, where each element
                         represents a large file path relative to the
                         ``TEST_LARGE_FILES_DIR`` directory

    """
    for file_ in files:
        file_path = os.path.join(TEST_LARGE_FILES_DIR, file_)
        if not os.path.isfile(file_path):
            return unittest.skip("File '{}' is not available".format(file_path))
        try:
            with open(file_path) as f:
                if f.readline().startswith('version https://git-lfs.github.com/spec/'):
                    return unittest.skip("Only Git LFS pointer is available "
                                         "for file '{}'".format(file_path))
        except UnicodeDecodeError:
            # file_ is a binary file (this is expected)
            pass
    return lambda func: func


class ExampleProcessTestCase(ProcessTestCase):
    """Test class for example processes."""

    def setUp(self):
        """Initialize test files path."""
        super(ExampleProcessTestCase, self).setUp()
        self.files_path = TEST_FILES_DIR
