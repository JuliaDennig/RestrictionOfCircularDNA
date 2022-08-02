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

    def find_binding_sites(self, sequence, enzyme_list_filtered):
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
                for m in binding.finditer(sequence):
                    split = cut + m.start()
                    append_splits.append(split)
            elif "BglI" == enzyme_list_filtered[i].name:
                binding = re.compile(r'GCC\w{5}GGC')
                for n in binding.finditer(sequence):
                    split = cut + n.start()
                    append_splits.append(split)
            elif "BstXI" == enzyme_list_filtered[i].name:
                binding = re.compile(r'CCA\w{6}TGG')
                for o in binding.finditer(sequence):
                    split = cut + o.start()
                    append_splits.append(split)
            elif "SfiI" == enzyme_list_filtered[i].name:
                binding = re.compile(r'GGCC\w{5}GGCC')
                for p in binding.finditer(sequence):
                    split = cut + p.start()
                    append_splits.append(split)
            if append_splits != []:
                enzyme_list_filtered[i].binding_sites = append_splits
            else:
                enzyme_list_filtered[i].binding_sites = "none"
        for item in enzyme_list_filtered:
            print(item)



find_bindings = FindBindingSites()
open_ape_file = find_bindings.open_ape_file()
open_enzyme_csv = find_bindings.open_enzyme_csv()
find_binding_sites = find_bindings.find_binding_sites(open_ape_file, open_enzyme_csv)
