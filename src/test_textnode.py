import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        node3 = TextNode("This is a text node", TextType.ITALIC, "https:www.google.com")
        node4 = TextNode("This is a text node", TextType.ITALIC, "https:www.google.com")
        self.assertEqual(node3, node4)
        node5 = TextNode("This is a text node", TextType.CODE, None)
        node6 = TextNode("This is a text node", TextType.LINKS, None)
        self.assertNotEqual(node5, node6)
        
if __name__ == "__main__":
    unittest.main()