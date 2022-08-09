import re


class OpenApeFile:
    def __init__(self):
        self.location = input("Where is the ape file saved?")
        
    def extract_sequence(self):
        ape_lines = []
        with open(self.location, "r") as location:
            ape_lines.append(location.readlines())
        ape_lines = ape_lines[0]
        return ape_lines
    
    def get_information_from_ape_file(self, ape_lines):
        sequence_start = ape_lines.index("ORIGIN\n") + 1
        sequence = ''.join(ape_lines[sequence_start:])
        sequence = sequence.replace("\n", "").replace(" ", "").replace("\t", "").replace("/", "").upper()
        for j in range(0, 10):
            sequence = sequence.replace(str(j), "")
        return sequence

    def get_features_from_ape_file(self):
        ape_lines = OpenApeFile.extract_sequence(self)
        features = []; feature_location = []; labels = []
        sequence_start = ape_lines.index("ORIGIN\n") + 1
        feature_start = ape_lines.index("FEATURES             Location/Qualifiers\n") + 1
        for k in range(feature_start, sequence_start-1):
            features.append(ape_lines[k])
        for o, elem in enumerate(features):
            if '..' in elem:
                feature_location.append(o)
            if '/label=' in elem:
                labels.append(o)
        label_list = []; feature_location_list = []
        for m in range(0, len(feature_location)):
            binding_site = re.sub('\D', ' ', features[feature_location[m]])
            binding_sites = binding_site.split(" ")
            binding_sites = list(filter(None, binding_sites))
            label = features[labels[m]].replace("/label=", "").replace("\n", "").replace(" ", "").replace('"', "").replace("\\"," ")
            label_list.append(label)
            feature_location_list.append(binding_sites)
        return label_list, feature_location_list

    def check_for_cutting_in_features(self, list, feature_locations, labels):
        bound_in_feature_per_enzyme = []
        for i in range(len(list)):
            bound_in_feature = []
            for j in range(len(list[i].binding_sites)):
                for k in range(len(feature_locations)):
                    if int(list[i].binding_sites[j]) > int(feature_locations[k][0]) \
                            and int(list[i].binding_sites[j]) < int(feature_locations[k][1]):
                        bound_in_feature.append(labels[k])
            bound_in_feature_per_enzyme.append(bound_in_feature)
        return bound_in_feature_per_enzyme

# C:\Users\julia\Documents\Python\RestrictionOfCircularDNA\data\p123.ape
# C:\Users\julia\Documents\Python\RestrictionOfCircularDNA\data\Testfile.ape
# C:\Users\julia\Documents\Python\RestrictionOfCircularDNA\data\pJD8.ape
