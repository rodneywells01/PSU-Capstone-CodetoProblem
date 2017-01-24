"""
Ideas:
- Ensure valid python syntax before parse (Compile script and ensure validity)
-
"""


"""Converts Code to a Word Problem"""
class Converter:

    def __init__(self, file):
        # Open and read file.
        self.originalcontent = self.obtain_lines(file)

        print self.originalcontent

    def obtain_lines(self, file):
        """Create a list of whitespace purged lines from file"""
        return [line.strip() for line in open(file, 'r') if len(line.strip()) > 0]


d = Converter("sampleprograms/sampleprogram.py")