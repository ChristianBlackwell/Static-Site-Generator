# Static Site Generator

A powerful Python tool that transforms Markdown files into a fully structured HTML website. This project handles complex nested structures, including headers, code blocks, lists, and quotes, while maintaining inline styles like bold and italic text.

## Features

- **Block Parsing**: Automatically detects and handles Paragraphs, Headings (H1-H6), Code blocks, Blockquotes, and both Ordered/Unordered lists.
- **Inline Styling**: Full support for **bold**, _italic_, `inline code`, links, and images.
- **Recursive Tree Building**: Converts Markdown into a custom `HTMLNode` tree before rendering to final HTML strings.
- **Extensible**: Built with a modular architecture using Enums and specialized node classes.

_Step to update the site are in update.md_
