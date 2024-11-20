


class HTMLNode:
    def __init__(self = None, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        raise NotImplementedError 

    def props_to_html(self):
        x = ""
        if self.props == None:
            return x
        for key, value  in self.props.items():
            x += f' {key}="{value}"' 
        return x
    
    def __repr__(self):
        return (f"HTMLNode ({self.tag}, {self.value}, {self.children}, {self.props})")