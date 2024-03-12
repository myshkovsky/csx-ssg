class TextNode:
    def __init__(self, text="", text_type="", url=None):
        self.text = text
        self.text_type = text_type
        self.url = url


    def __eq__(self, other) -> bool:
        return self.text == other.text


    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
