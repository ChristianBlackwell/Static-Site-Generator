from enum import Enum
from inline_markdown import text_to_textnodes
from textnode import TextNode, TextType,text_node_to_html_node
from htmlnode import ParentNode

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    lines = block.split("\n")
    if lines[0].startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    
    if lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    #Split markdown into blocks
    blocks = markdown_to_blocks(markdown)
    #List of child nodes that represent each block
    block_children = []
    #Loop over each block
    for block in blocks:
        #Based on block type - create a htmlnode with the proper data
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                lines = block.split("\n")
                paragraph_text = " ".join(lines)
                children = text_to_children(paragraph_text)
                node = ParentNode("p", children)
                block_children.append(node)
            
            case BlockType.HEADING:
                level = 0
                for char in block:
                    if char == "#":
                        level += 1
                    else:
                        break
                content = block[level + 1:] 
                tag = f"h{level}"
                children = text_to_children(content)
                node = ParentNode(tag, children)
                block_children.append(node)
            
            case BlockType.CODE:
                content = block[4:-3]
                # 1. Create the leaf node for the text
                text_node = TextNode(content, TextType.TEXT) # Use "text" here so it doesn't add extra tags
                html_node = text_node_to_html_node(text_node)
                # 2. Wrap the leaf in <code>
                code_node = ParentNode("code", [html_node])
                # 3. Wrap the <code> in <pre>
                pre_node = ParentNode("pre", [code_node])
                block_children.append(pre_node)
            
            case BlockType.QUOTE:
                lines = block.split("\n")
                new_lines = []
                for line in lines:
                    new_lines.append(line.lstrip(">").strip())
                content = " ".join(new_lines)
                children = text_to_children(content)
                node = ParentNode("blockquote", children)
                block_children.append(node)
            
            case BlockType.UNORDERED_LIST:
                lines = block.split("\n")
                list_items = []
                for line in lines:
                    # Strip the marker (e.g., "- " or "* ")
                    content = line[2:]
                    # Get the inline children for this list item
                    children = text_to_children(content)
                    # Wrap those children in an <li> node
                    list_items.append(ParentNode("li", children))
                # Wrap all <li> nodes in a <ul> node
                node = ParentNode("ul", list_items)
                block_children.append(node)
            
            case BlockType.ORDERED_LIST:
                lines = block.split("\n")
                list_items = []
                for line in lines:
                    # Find the first space and take everything after it
                    content = line[line.find(" ") + 1:]
                    children = text_to_children(content)
                    list_items.append(ParentNode("li", children))
                node = ParentNode("ol", list_items)
                block_children.append(node)

    return ParentNode("div", block_children)

#Helper function for markdown_to_html_node()
def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children