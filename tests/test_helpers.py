"""Test helpers for the django coverage plugin."""

import unittest

from django_template_coverage.plugin import make_line_map, get_line_number


class HelperTest(unittest.TestCase):
    def test_line_maps(self):
        line_map = make_line_map("Hello\nWorld\n")
                                # 012345 6789ab
        self.assertEqual(get_line_number(line_map, 0), 1)
        self.assertEqual(get_line_number(line_map, 1), 1)
        self.assertEqual(get_line_number(line_map, 5), 1)
        self.assertEqual(get_line_number(line_map, 6), 2)
        self.assertEqual(get_line_number(line_map, 7), 2)
        self.assertEqual(get_line_number(line_map, 11), 2)
        self.assertEqual(get_line_number(line_map, 12), -1)