from textnode import *
from htmlnode import *


def main():
    text_node_one = TextNode("slurp", TextType.BOLD, "https//:www.boot.dev")
    text_node_one.__repr__()
    html_node_one = HTMLNode("slurped", "TextType.BOLD", "https//:www.boot.dev",)
    html_node_two = HTMLNode()
    html_node_two.__repr__()
    node7 = TextNode("This is a text node", TextType.TEXT, None)
    print (node7.text_node_to_html_node())

main()