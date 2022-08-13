from OpenAPE import OpenApeFile
from OpenEnzymeCSV import OpenEnzymeList
from OpenEnzymeCSV import FilterEnzymeListAllData
import re


class FindBindingSites:
    def __init__(self):
        self.open_ape = OpenApeFile()

    def open_ape_file(self):
        extract = self.open_ape.extract_sequence()
        sequence = self.open_ape.get_information_from_ape_file(extract)
        return sequence, self.open_ape

    def features_from_ape(self):
        labels, feature_locations = self.open_ape.get_features_from_ape_file()
        return labels, feature_locations

    def open_enzyme_csv(self):
        open_enzymes = OpenEnzymeList("C:\\Users\\julia\\Documents\\Python\\RestrictionOfCircularDNA\\data\\Enzymes.csv")
        enzymes = open_enzymes.open_csv()
        filter_enzyme_list_all_data = FilterEnzymeListAllData(enzymes)
        enzyme_list_filtered = filter_enzyme_list_all_data.execute_my_filter()
        # for item in enzyme_list_filtered:
            # print(item)
        return enzyme_list_filtered

    def fuse_beginning_end_of_sequence(self, sequence):
        return sequence[-10:] + sequence[0:10]

    def find_binding_sites(self, sequence, enzyme_list_filtered):
        splits_list = []
        for i in range(len(enzyme_list_filtered)):
            enzyme_binding = enzyme_list_filtered[i].cut.replace("^", "")
            cut = enzyme_list_filtered[i].cut.find("^")
            if "BglI" == enzyme_list_filtered[i].name:
                binding = re.compile(r'GCC\w{5}GGC')
            elif "BstXI" == enzyme_list_filtered[i].name:
                binding = re.compile(r'CCA\w{6}TGG')
            elif "DraIII-HF" == enzyme_list_filtered[i].name:
                binding = re.compile(r'CAC\w{3}GTG')
            elif "SfiI" == enzyme_list_filtered[i].name:
                binding = re.compile(r'GGCC\w{5}GGCC')
            elif "XcmI" == enzyme_list_filtered[i].name:
                binding = re.compile(r'CCA\w{9}TGG')
            else:
                binding = re.compile(enzyme_binding)
            append_splits = []
            for j in binding.finditer(sequence):
                append_splits.append(cut + j.start())
            splits_list.append(append_splits)
        return splits_list

    def calculate_final_bindings_list(self, splits_list, splits_list_2, enzyme_list_filtered, sequence):
        for i in range(len(splits_list_2)):
            if splits_list_2[i]:
                for j in range(len(splits_list_2[i])):
                    if int(splits_list_2[i][j]) < 10:
                        new = len(sequence) + (int(splits_list_2[i][j]) - 10)
                    else:
                        new = int(splits_list_2[i][j]) - 10
                    if new not in splits_list[i]:
                        splits_list[i].append(new)
                        splits_list[i].sort()
                    enzyme_list_filtered[i].binding_sites = splits_list[i]
            else:
                if splits_list:
                    enzyme_list_filtered[i].binding_sites = splits_list[i]
        return enzyme_list_filtered
