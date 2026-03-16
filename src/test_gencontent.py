import unittest
from gencontent import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_basic_title(self):
        self.assertEqual(extract_title("# Hello"), "Hello")
    
    def test_no_h1_raises(self):
        self.assertRaises(Exception, extract_title, "## Hello")