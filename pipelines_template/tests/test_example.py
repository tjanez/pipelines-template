# pylint: disable=missing-docstring
from pipelines_template.utils.test import ExampleProcessTestCase


class SimpleProcessorTestCase(ExampleProcessTestCase):

    def test_example(self):
        example = self.run_process('pipelines-example', {'src': 'example.txt'})
        self.assertFile(example, 'dst', 'example.txt')
