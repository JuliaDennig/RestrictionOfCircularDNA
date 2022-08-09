from CalculateBandSizes import BandSizes
import csv


class FilterResults:
    def __init__(self):
        self.found_bindings = BandSizes()
        self.band_sizes_one_enzyme = self.found_bindings.calculate_band_sizes_one_enzyme()
        self.combined_bindings_list = self.found_bindings.combine_binding_sites_two_enzymes()
        self.band_sizes_two_enzymes = self.found_bindings.calculate_band_sizes_two_enzymes(self.combined_bindings_list)
        self.labels, self.feature_locations = self.found_bindings.find_bindings.features_from_ape()
        self.cut_features_one_enzyme = \
            self.found_bindings.open_ape_file.check_for_cutting_in_features(self.found_bindings.enzyme_list_filtered, self.feature_locations, self.labels)
        self.cut_features_two_enzymes = self.found_bindings.open_ape_file.check_for_cutting_in_features(self.band_sizes_two_enzymes, self.feature_locations, self.labels)

    def filter_useful_results(self, list):
        if len(list.band_sizes) < 3:
            return False
        elif list.band_sizes[0] < 300:
            return False
        for j in range(len(list.band_sizes)-1):
            bands_difference = list.band_sizes[j+1] - list.band_sizes[j]
            if bands_difference < 200 and list.band_sizes[j] < 1000:
                return False
            elif bands_difference < 300 and list.band_sizes[j] < 3000:
                return False
            elif bands_difference < 800 and list.band_sizes[j+1] > 3000:
                return False

        return True

    def go_through_filter(self):
        rows = []
        for i in range(len(self.found_bindings.enzyme_list_filtered)):
            filter_for_useful_results_one_enzyme = FilterResults.filter_useful_results(self, self.found_bindings.enzyme_list_filtered[i])
            filter_for_useful_results_two_enzymes = FilterResults.filter_useful_results(self, self.band_sizes_two_enzymes[i])
            if filter_for_useful_results_one_enzyme:
                rows.append([self.found_bindings.enzyme_list_filtered[i].name,
                             self.found_bindings.enzyme_list_filtered[i].temperature,
                             self.found_bindings.enzyme_list_filtered[i].buffer,
                             self.found_bindings.enzyme_list_filtered[i].binding_sites,
                             self.found_bindings.enzyme_list_filtered[i].band_sizes,
                             self.cut_features_one_enzyme[i]])
            elif filter_for_useful_results_two_enzymes:
                rows.append([self.band_sizes_two_enzymes[i].enzyme_combination,
                             self.band_sizes_two_enzymes[i].temperature,
                             self.band_sizes_two_enzymes[i].buffer_1 + " bzw. "
                             + self.band_sizes_two_enzymes[i].buffer_2,
                             self.band_sizes_two_enzymes[i].binding_sites,
                             self.band_sizes_two_enzymes[i].band_sizes,
                             self.cut_features_two_enzymes[i]])
        return rows

    def export_results_to_csv(self, rows):
        fields = ["enzyme", "temperature in °C", "buffer", "binding sites", "band sizes", "feature"]
        filename = input("Where should the results be saved?")
        with open(filename, 'w') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=';')
            csv_writer.writerow(fields)
            csv_writer.writerows(rows)
        return filename


filter_results = FilterResults()
useful_results = filter_results.go_through_filter()
file_location = filter_results.export_results_to_csv(useful_results)
print("\nDone")


# results at: "C:\\Users\\julia\\Documents\\Python\\RestrictionOfCircularDNA\\data\\Results_pJD8.csv"
