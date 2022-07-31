from OpenAPE import OpenApeFile
from OpenEnzymeCSV import OpenEnzymeList
from OpenEnzymeCSV import FilterEnzymeListAllData


# import re


class FindBindingSites:
    def open_ape_file(self):
        location = input("Where is the ape file saved?")
        open_ape = OpenApeFile(location)
        extract = open_ape.extract_sequence()
        sequence = open_ape.get_information_from_ape_file(extract)
        return sequence

    def open_enzyme_csv(self):
        open_enzymes = OpenEnzymeList("C:\\Users\\julia\\Documents\\Python\\RestrictionOfCircularDNA\\Enzyme.csv")
        enzymes = OpenEnzymeList.open_csv(open_enzymes)
        filter_enzyme_list_all_data = FilterEnzymeListAllData(enzymes)
        enzyme_list_filtered = filter_enzyme_list_all_data.execute_my_filter()
        for item in enzyme_list_filtered:
            print(item)
        return enzyme_list_filtered

    # def find_binding_sites(self, sequence, enzyme_list_filtered):


find_bindings = FindBindingSites()
open_ape_file = find_bindings.open_ape_file()
open_enzyme_csv = find_bindings.open_enzyme_csv()
# find_binding_sites = find_bindings.find_binding_sites(open_ape_file, open_enzyme_csv)
