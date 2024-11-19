from enum import Enum

class TextType(Enum):
    Normal_text = "normal"
    Bold_text = "bold"
    Italic_text = "italic"
    Code_text = "code"
    Links = "link"
    Images = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url
    
    def __eq__(self, other):
        return (
            self.erxt_type == other.text_type 
            and self.erxt == other.text 
            and self.url == other.url
        )

    def __repr__(self):
        return print(f"TextNode({self.text}, {self.text_type.value}, {self.url})")