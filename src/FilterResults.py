from CalculateBandSizes import BandSizes
import csv


class FilterResults:
    def __init__(self):
        self.found_bindings = BandSizes()
        self.band_sizes_one_enzyme = self.found_bindings.calculate_band_sizes_one_enzyme()
        self.combined_bindings_list = self.found_bindings.combine_binding_sites_two_enzymes()
        self.band_sizes_two_enzymes = self.found_bindings.calculate_band_sizes_two_enzymes(self.combined_bindings_list)

    def filter_useful_results(self):
        rows = []
        for i in range(len(self.found_bindings.enzyme_list_filtered)):
            for j in range(len(self.found_bindings.enzyme_list_filtered[i].band_sizes)-1):
                bands_difference = self.found_bindings.enzyme_list_filtered[i].band_sizes[j+1] - self.found_bindings.enzyme_list_filtered[i].band_sizes[j]
                if bands_difference < 200 and self.found_bindings.enzyme_list_filtered[i].band_sizes[j] < 1000:
                    break
                elif bands_difference < 400 and self.found_bindings.enzyme_list_filtered[i].band_sizes[j] < 3000:
                    break
                elif bands_difference < 800 and self.found_bindings.enzyme_list_filtered[i].band_sizes[j+1] > 3000:
                    break
                elif len(self.found_bindings.enzyme_list_filtered[i].band_sizes) < 3:
                    break
                elif self.found_bindings.enzyme_list_filtered[i].band_sizes[0] < 300:
                    break
                else:
                    rows.append([self.found_bindings.enzyme_list_filtered[i].name,
                                 self.found_bindings.enzyme_list_filtered[i].cut,
                                 self.found_bindings.enzyme_list_filtered[i].type,
                                 self.found_bindings.enzyme_list_filtered[i].temperature,
                                 self.found_bindings.enzyme_list_filtered[i].buffer,
                                 self.found_bindings.enzyme_list_filtered[i].binding_sites,
                                 self.found_bindings.enzyme_list_filtered[i].band_sizes])
        return rows

    def export_results_to_csv(self, rows):
        fields = ["enzyme", "cut", "type", "temperature", "buffer", "binding sites", "band sizes"]
        filename = "C:\\Users\\julia\\Documents\\Python\\RestrictionOfCircularDNA\\data\\ResultsForOneEnzyme.csv"
        with open(filename, 'w') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(fields)
            csv_writer.writerows(rows)


filter = FilterResults()
useful_results = filter.filter_useful_results()
print(useful_results)
filter.export_results_to_csv(useful_results)
