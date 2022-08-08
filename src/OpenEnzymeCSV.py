TOP_ENZYMES_RESTRICTION = [
    "AgeI-HF",
    "AscI",
    "BamHI-HF",
    "BglI",
    "BglII",
    "BstXI",
    "ClaI",
    "DraI",
    "DraIII-HF",
    "EcoRI-HF",
    "EcoRV-HF",
    "HindIII-HF",
    "KpnI-HF",
    "MfeI-HF",
    "MscI",
    "NarI",
    "NcoI",
    "NdeI",
    "NotI-HF",
    "PacI",
    "PstI-HF",
    "PvuI-HF",
    "PvuII-HF",
    "SacI-HF",
    "SacII",
    "SalI-HF",
    "ScaI-HF",
    "SfiI",
    "SpeI-HF",
    "SphI-HF",
    "SspI-HF",
    "XbaI",
    "XcmI",
    "XhoI",
    "XmaI"
]


class EnzymeList:
    def __init__(self, name, cut, type, buffer, temperature, binding_sites, band_sizes):
        self.name = name
        self.cut = cut
        self.type = type
        self.temperature = temperature
        self.buffer = buffer
        self.binding_sites = binding_sites
        self.band_sizes = band_sizes

    def __str__(self):
        return "enzyme: " + self.name + ", cut: " + self.cut + ", type: " + self.type + ", temperature: " + self.temperature + "°C, buffer: " + self.buffer + ", binding site(s): " + str(self.binding_sites) + ", band size(s): " + str(self.band_sizes)


class OpenEnzymeList:
    def __init__(self, save_place):
        self.save_place = save_place

    def open_csv(self):
        f = open(self.save_place, "r")
        enzyme_list = f.readlines()
        enzyme_list_all_data = []
        for i in range(1, len(enzyme_list)):
            el = enzyme_list[i].replace("\n", "").split(";")
            enzyme_list_all_data.append(EnzymeList(el[0], el[1], el[2], el[3], el[4], "", ""))
        return enzyme_list_all_data


class FilterEnzymeListAllData:
    def __init__(self, enzyme_list_all_data):
        self.enzyme_list_all_data = enzyme_list_all_data

    def execute_my_filter(self):
        return list(filter(lambda enzyme: enzyme.name in TOP_ENZYMES_RESTRICTION, self.enzyme_list_all_data))


class EnzymeListCombined:
    def __init__(self, enzyme_combination, temperature, buffer_1, buffer_2, binding_sites, band_sizes):
        self.enzyme_combination = enzyme_combination
        self.temperature = temperature
        self.buffer_1 = buffer_1
        self.buffer_2 = buffer_2
        self.binding_sites = binding_sites
        self.band_sizes = band_sizes

    def __str__(self):
        return "enzymes: " + str(self.enzyme_combination) + ", temperature: " + str(self.temperature) + " °C, buffer 1: " + str(self.buffer_1) + ", buffer 2: " + str(self.buffer_2) + ", binding site(s): " + str(self.binding_sites) + ", band size(s): " + str(self.band_sizes)
