from insured import Insured
#třída pro správu pojištěných. Obsahuje metody pro přidání, výpis a vyhledání pojištěných.

class InsuredManager:
    def __init__(self, insured_list):
        # Inicializace prázdného seznamu, který bude obsahovat všechny pojištěné osoby
        self.insured_list = insured_list

    # Metoda pro přidání nové pojištěné osoby do seznamu
    def add_insured(self, insured: Insured):
        self.insured_list.append(insured)

    # Metoda pro zobrazení seznamu pojištěných osob ve formě řetězců
    def list_insured(self):
        return [str(insured) for insured in self.insured_list]

    # Metoda pro vyhledání pojištěné osoby podle jména a příjmení
    def find_insured(self, first_name: str, last_name: str):
        # Vyhledání všech pojištěných osob, které mají zadané jméno a příjmení
        return [insured for insured in self.insured_list if insured.first_name == first_name and insured.last_name == last_name]