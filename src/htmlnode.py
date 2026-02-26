class HtmlNode():

    #Constructor Attribute Details
        #tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        #value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
        #children - A list of HTMLNode objects representing the children of this node
        #props - A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    #Child classes will override this method to render themselves as HTML.
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    #Return a formatted string representing the HTML attributes of the node
        #For example, if self.props is:
            #{"href": "https://www.google.com", "target": "_blank",}
        #Then self.props_to_html() should return:
            # href="https://www.google.com" target="_blank"
    def props_to_html(self):
        if not self.props:
            return ""
        out = ""
        for key, val in self.props.items():
            out += f' {key}="{val}"'
        return out
    
    def __repr__(self): 
        return f"HtmlNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

# A LeafNode represents an HTML tag that has no children.
# It contains a single value (usually text) inside its opening and closing tags.
class LeafNode(HtmlNode):
    # Initializes a leaf node with a tag, a required value, and optional properties
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    # Renders the leaf node as an HTML string.
    # If there is no tag, it simply returns the raw value as text.
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value.")
        elif self.tag is None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self): 
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

# A ParentNode handles the nesting of HTML nodes inside one another.
# It is defined by having a tag and a list of children, but no direct value.
class ParentNode(HtmlNode):
    # Initializes a parent node with a required tag and a required list of children.
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    # Recursively renders the parent node and all of its children into one HTML string.
    # This method iterates over the children and calls their respective to_html methods.
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag.")
        elif self.children is None:
            raise ValueError("ParentNode child is missing a value.")
        else:
            all_children_html = ""
            for child in self.children:
                all_children_html += child.to_html()
            return f'<{self.tag}{self.props_to_html()}>{all_children_html}</{self.tag}>'
        