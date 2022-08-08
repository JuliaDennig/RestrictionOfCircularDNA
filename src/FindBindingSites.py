from OpenAPE import OpenApeFile
from OpenEnzymeCSV import OpenEnzymeList
from OpenEnzymeCSV import FilterEnzymeListAllData
import re


class FindBindingSites:
    def open_ape_file(self):
        location = input("Where is the ape file saved?")
        open_ape = OpenApeFile(location)
        extract = open_ape.extract_sequence()
        sequence = open_ape.get_information_from_ape_file(extract)
        return sequence

    def open_enzyme_csv(self):
        open_enzymes = OpenEnzymeList("C:\\Users\\julia\\Documents\\Python\\RestrictionOfCircularDNA\\data\\Enzymes.csv")
        enzymes = OpenEnzymeList.open_csv(open_enzymes)
        filter_enzyme_list_all_data = FilterEnzymeListAllData(enzymes)
        enzyme_list_filtered = filter_enzyme_list_all_data.execute_my_filter()
        # for item in enzyme_list_filtered:
            # print(item)
        return enzyme_list_filtered

    def fuse_beginning_end_of_sequence(self, sequence):
        alternative_sequence = sequence[-10:] + sequence[0:10]
        return alternative_sequence

    def find_binding_sites(self, sequence, enzyme_list_filtered):
        splits_list = []
        for i in range(len(enzyme_list_filtered)):
            enzyme_binding = enzyme_list_filtered[i].cut.replace("^", "")
            cut = enzyme_list_filtered[i].cut.find("^")
            binding = re.compile(enzyme_binding)
            append_splits = []
            for j in binding.finditer(sequence):
                split = cut + j.start()
                append_splits.append(split)
            if "DraIII-HF" == enzyme_list_filtered[i].name:
                binding = re.compile(r'CAC\w{3}GTG')
                for m in binding.finditer(sequence):
                    split = cut + m.start()
                    append_splits.append(split)
            elif "XcmI" == enzyme_list_filtered[i].name:
                binding = re.compile(r'CCA\w{9}TGG')
                for n in binding.finditer(sequence):
                    split = cut + n.start()
                    append_splits.append(split)
            elif "BglI" == enzyme_list_filtered[i].name:
                binding = re.compile(r'GCC\w{5}GGC')
                for o in binding.finditer(sequence):
                    split = cut + o.start()
                    append_splits.append(split)
            elif "BstXI" == enzyme_list_filtered[i].name:
                binding = re.compile(r'CCA\w{6}TGG')
                for p in binding.finditer(sequence):
                    split = cut + p.start()
                    append_splits.append(split)
            elif "SfiI" == enzyme_list_filtered[i].name:
                binding = re.compile(r'GGCC\w{5}GGCC')
                for q in binding.finditer(sequence):
                    split = cut + q.start()
                    append_splits.append(split)
            splits_list.append(append_splits)
        return splits_list

    def calculate_final_bindings_list(self, splits_list, splits_list_2, enzyme_list_filtered, sequence):
        for q in range(len(splits_list_2)):
            if splits_list_2[q]:
                for r in range(len(splits_list_2[q])):
                    if int(splits_list_2[q][r]) < 10:
                        new = len(sequence) + (int(splits_list_2[q][r]) - 10)
                    else:
                        new = int(splits_list_2[q][r]) - 10
                    if new not in splits_list[q]:
                        splits_list[q].append(new)
                        splits_list[q].sort()
                        enzyme_list_filtered[q].binding_sites = splits_list[q]
                    else:
                        enzyme_list_filtered[q].binding_sites = splits_list[q]
            else:
                if splits_list:
                    enzyme_list_filtered[q].binding_sites = splits_list[q]
        return enzyme_list_filtered
