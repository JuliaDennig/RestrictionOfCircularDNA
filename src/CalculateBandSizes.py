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
        self.combined_bindings_list = self.combine_binding_sites_two_enzymes()

    def calculate_band_sizes(self, is_one_enzyme):
        instance_var = self.enzyme_list_filtered if is_one_enzyme else self.combined_bindings_list
        for i in range(len(instance_var)):
            band_sizes = []
            amount_binding_sites = len(instance_var[i].binding_sites)
            if amount_binding_sites == 1:
                band_sizes.append(len(self.sequence))
                instance_var[i].band_sizes = band_sizes
            elif amount_binding_sites == 0:
                band_sizes.append("none")
                instance_var[i].band_sizes = band_sizes
            else:
                for j in range(amount_binding_sites - 1):
                    band = instance_var[i].binding_sites[j + 1] - \
                           instance_var[i].binding_sites[j]
                    band_sizes.append(band)
                band_sizes.append(len(self.sequence) - instance_var[i].binding_sites[-1] +
                                  instance_var[i].binding_sites[0])
                band_sizes.sort()
                instance_var[i].band_sizes = band_sizes
        # for item in instance_var:
            # print(item)
        return instance_var

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
                    combined_bindings = self.enzyme_list_filtered[i].binding_sites + self.enzyme_list_filtered[j].binding_sites
                    combined_bindings.sort()
                    combined_enzymes = EnzymeListCombined(unsorted_two_enzymes, "", self.enzyme_list_filtered[i].buffer,
                                                          self.enzyme_list_filtered[j].buffer, combined_bindings, "")
                    if self.enzyme_list_filtered[i].temperature == self.enzyme_list_filtered[j].temperature:
                        combined_enzymes.temperature = self.enzyme_list_filtered[i].temperature
                    else:
                        combined_enzymes.temperature = "not compatible"
                    combined_enzymes_list.append(combined_enzymes)
        # for item in combined_enzymes_list:
            # print(item)
        return combined_enzymes_list
