from CalculateBandSizes import BandSizes
import csv


class FilterResults:
    def __init__(self):
        self.found_bindings = BandSizes()
        self.found_bindings.calculate_band_sizes(True)
        self.band_sizes_two_enzymes = self.found_bindings.calculate_band_sizes(False)
        self.labels, self.feature_locations = self.found_bindings.find_bindings.features_from_ape()
        self.cut_features_one_enzyme = \
            self.found_bindings.open_ape_file.check_for_cutting_in_features(self.found_bindings.enzyme_list_filtered, self.feature_locations, self.labels)
        self.cut_features_two_enzymes = self.found_bindings.open_ape_file.check_for_cutting_in_features(self.band_sizes_two_enzymes, self.feature_locations, self.labels)

    def filter_useful_results(self, input_list):
        if len(input_list.band_sizes) < 3 or input_list.band_sizes[0] < 300:
            return False
        for j in range(len(input_list.band_sizes) - 1):
            bands_difference = input_list.band_sizes[j + 1] - input_list.band_sizes[j]
            if bands_difference < 200 and input_list.band_sizes[j] < 1000 \
                    or bands_difference < 300 and input_list.band_sizes[j] < 3000 \
                    or bands_difference < 800 and input_list.band_sizes[j + 1] > 3000:
                return False
        return True

    def go_through_filter(self):
        rows = []
        for i in range(len(self.found_bindings.enzyme_list_filtered)):
            objects_one_enzyme = self.found_bindings.enzyme_list_filtered[i]
            if FilterResults.filter_useful_results(self, objects_one_enzyme):
                rows.append([objects_one_enzyme.name,
                             objects_one_enzyme.temperature,
                             objects_one_enzyme.buffer,
                             objects_one_enzyme.binding_sites,
                             objects_one_enzyme.band_sizes,
                             self.cut_features_one_enzyme[i]])
        for k in range(len(self.band_sizes_two_enzymes)):
            objects_two_enzymes = self.band_sizes_two_enzymes[k]
            if FilterResults.filter_useful_results(self, objects_two_enzymes):
                rows.append([objects_two_enzymes.enzyme_combination,
                             objects_two_enzymes.temperature,
                             objects_two_enzymes.buffer_1 + " bzw. " + objects_two_enzymes.buffer_2,
                             objects_two_enzymes.binding_sites,
                             objects_two_enzymes.band_sizes,
                             self.cut_features_two_enzymes[k]])
        return rows

    def export_results_to_csv(self, rows):
        fields = ["enzyme", "temperature in °C", "buffer", "binding sites", "band sizes", "feature"]
        while True:
            filename = input("Where should the results be saved?")
            if filename.endswith(".csv"):
                try:
                    with open(filename, 'w') as csv_file:
                        csv_writer = csv.writer(csv_file, delimiter=';')
                        csv_writer.writerow(fields)
                        csv_writer.writerows(rows)
                    break
                except Exception:
                    print("Please give a valid path.")
            else:
                print("The path has to be a .csv file. Please give a valid path.")


filter_results = FilterResults()
useful_results = filter_results.go_through_filter()
filter_results.export_results_to_csv(useful_results)
print("\nDone")


# results at: "C:\\Users\\julia\\Documents\\Python\\RestrictionOfCircularDNA\\data\\Results_pJD8.csv"
