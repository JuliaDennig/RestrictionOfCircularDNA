class OpenApeFile:
    def __init__(self, location):
        self.location = location
        
    def extract_sequence(self):
        ape_lines = []
        with open(self.location, "r") as location:
            ape_lines.append(location.readlines())
        for elem in ape_lines[0]:
            if 'linear' in elem:
                print("\nThe sequence is linear.\n")
            elif 'circular' in elem:
                print("\nThe sequence is circular.\n")
        ape_lines = ape_lines[0]
        return ape_lines
    
    def get_information_from_ape_file(self, ape_lines):
        sequence_start = ape_lines.index("ORIGIN\n") + 1
        sequence = ''.join(ape_lines[sequence_start:])
        sequence = sequence.replace("\n", "").replace(" ", "").replace("\t", "").replace("/", "").upper()
        for j in range(0, 10):
            sequence = sequence.replace(str(j), "")
        return sequence

# C:\Users\julia\Documents\Python\RestrictionOfCircularDNA\data\p123.ape
# C:\Users\julia\Documents\Python\RestrictionOfCircularDNA\data\Testfile.ape
