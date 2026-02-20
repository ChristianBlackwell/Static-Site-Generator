import unittest
from htmlnode import HtmlNode, LeafNode


class TestHtmlNode(unittest.TestCase):
    def test_props_none(self):
        node = HtmlNode(props=None)
        self.assertEqual(node.props_to_html(), "")

    def test_props_empty(self):
        node = HtmlNode(props={})
        self.assertEqual(node.props_to_html(), "")

    def test_props_multiple(self):
        node = HtmlNode(props={"href": "https://boot.dev", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://boot.dev" target="_blank"')
    
class TestLeafNode(unittest.TestCase):
    def test_value_is_none_raises(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_tag_is_none_returns_raw_text(self):
        node = LeafNode(None, "value text")
        self.assertEqual(node.to_html(), "value text")
    
    def test_props_render_correctly(self):
        node = LeafNode("a", "Click", {"href": "https://boot.dev"})
        self.assertEqual(node.to_html(), '<a href="https://boot.dev">Click</a>')

if __name__ == "__main__":
    unittest.main()