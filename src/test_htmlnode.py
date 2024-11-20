import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_html_to_props(self):
        node = HTMLNode("1", "2", "3", {
                            "href": "https://www.google.com", 
                            "target": "_blank",
                        })
        node2 = HTMLNode()
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
        self.assertEqual(node2.props_to_html(), "")
        node.__repr__()
        self.assertEqual(node2.__repr__(), "HTMLNode (None, None, None, None)")
        self.assertEqual(node.__repr__(), "HTMLNode (1, 2, 3, {'href': 'https://www.google.com', 'target': '_blank'})")

        # self.assertEqual(node.__repr__(),"HTMLNode (1, 2, 3, {'href': 'https://www.google.com', 'target': '_blank'})")
                        
        # node3 = HTMLNode()
        # node4 = HTMLNode()
        # node6 = HTMLNode()
        # self.html_to_props(node5)

        
if __name__ == "__main__":
    unittest.main()