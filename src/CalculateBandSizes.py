from OpenEnzymeCSV import EnzymeListCombined
from FindBindingSites import FindBindingSites


class BandSizes:
    def __init__(self):
        self.find_bindings = FindBindingSites()
        self.sequence, self.open_ape_file = self.find_bindings.open_ape_file()
        self.open_enzyme_csv = self.find_bindings.open_enzyme_csv()
        self.generate_alternative_sequence = self.find_bindings.fuse_beginning_end_of_sequence(self.sequence)
        self.find_binding_sites = self.find_bindings.find_binding_sites(self.sequence, self.open_enzyme_csv)
        self.find_binding_sites_2 = self.find_bindings.find_binding_sites(self.generate_alternative_sequence,
                                                                          self.open_enzyme_csv)
        self.enzyme_list_filtered = self.find_bindings.calculate_final_bindings_list(self.find_binding_sites,
                                                                                     self.find_binding_sites_2,
                                                                                     self.open_enzyme_csv,
                                                                                     self.sequence)

    def calculate_band_sizes_one_enzyme(self):
        for i in range(len(self.enzyme_list_filtered)):
            band_sizes = []
            if len(self.enzyme_list_filtered[i].binding_sites) == 1:
                band_sizes.append(len(self.sequence))
                self.enzyme_list_filtered[i].band_sizes = band_sizes
            elif len(self.enzyme_list_filtered[i].binding_sites) == 0:
                band_sizes.append("none")
                self.enzyme_list_filtered[i].band_sizes = band_sizes
            else:
                for j in range(len(self.enzyme_list_filtered[i].binding_sites) - 1):
                    band = self.enzyme_list_filtered[i].binding_sites[j + 1] - \
                           self.enzyme_list_filtered[i].binding_sites[j]
                    band_sizes.append(band)
                band_sizes.append(len(self.sequence) - self.enzyme_list_filtered[i].binding_sites[-1] +
                                  self.enzyme_list_filtered[i].binding_sites[0])
                band_sizes.sort()
                self.enzyme_list_filtered[i].band_sizes = band_sizes
        #for item in self.enzyme_list_filtered:
            #print(item)

    def combine_binding_sites_two_enzymes(self):
        combined_enzymes_list = []
        two_enzymes_list = []
        for i in range(len(self.enzyme_list_filtered)):
            for j in range(len(self.enzyme_list_filtered)):
                two_enzymes = [self.enzyme_list_filtered[i].name, self.enzyme_list_filtered[j].name]
                unsorted_two_enzymes = str(two_enzymes[0]) + " + " + str(two_enzymes[1])
                two_enzymes.sort()
                sorted_two_enzymes = str(two_enzymes[0]) + " + " + str(two_enzymes[1])
                if self.enzyme_list_filtered[i].name != self.enzyme_list_filtered[j].name \
                        and self.enzyme_list_filtered[i].binding_sites != [] \
                        and self.enzyme_list_filtered[j].binding_sites != [] \
                        and sorted_two_enzymes not in two_enzymes_list:
                    two_enzymes_list.append(sorted_two_enzymes)
                    combined_bindings = self.enzyme_list_filtered[i].binding_sites + self.enzyme_list_filtered[
                        j].binding_sites
                    combined_bindings.sort()
                    combined_enzymes = EnzymeListCombined(unsorted_two_enzymes, "", self.enzyme_list_filtered[i].buffer, self.enzyme_list_filtered[j].buffer, combined_bindings, "")
                    if self.enzyme_list_filtered[i].temperature == self.enzyme_list_filtered[j].temperature:
                        combined_enzymes.temperature = self.enzyme_list_filtered[i].temperature
                    else:
                        combined_enzymes.temperature = "not compatible"
                    combined_enzymes_list.append(combined_enzymes)
        # for item in combined_enzymes_list:
            # print(item)
        return combined_enzymes_list

    def calculate_band_sizes_two_enzymes(self, combined_enzymes_list):
        for i in range(len(combined_enzymes_list)):
            band_sizes = []
            if len(combined_enzymes_list[i].binding_sites) == 1:
                band_sizes.append(len(self.open_ape_file))
                combined_enzymes_list[i].band_sizes = band_sizes
            elif len(combined_enzymes_list[i].binding_sites) == 0:
                band_sizes.append("none")
                combined_enzymes_list[i].band_sizes = band_sizes
            else:
                for j in range(len(combined_enzymes_list[i].binding_sites) - 1):
                    band = combined_enzymes_list[i].binding_sites[j + 1] - combined_enzymes_list[i].binding_sites[j]
                    band_sizes.append(band)
                band_sizes.append(len(self.sequence) - combined_enzymes_list[i].binding_sites[-1] +
                                  combined_enzymes_list[i].binding_sites[0])
                band_sizes.sort()
                combined_enzymes_list[i].band_sizes = band_sizes
        #for item in combined_enzymes_list:
            #print(item)
        return combined_enzymes_list
