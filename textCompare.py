from difflib import SequenceMatcher
class textComparison():
    def simpleTextCompare(a, b):
        return SequenceMatcher(None, a, b).ratio()