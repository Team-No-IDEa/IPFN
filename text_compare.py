from difflib import SequenceMatcher


class TextCompare():
    """Initialise TextCompare class to match text."""

    def simple_text_compare(self, a, b):
        return SequenceMatcher(None, a, b).ratio()
