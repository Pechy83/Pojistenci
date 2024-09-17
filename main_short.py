from insured import Insured
from insured_manager import InsuredManager
from utils_validate import validate_phone, validate_name, validate_age, get_input


def main_short():
    manager = InsuredManager([])
    options = {
        # Použití validace pro každý vstup při přidávání pojištěného
        '1': lambda: manager.add_insured(
            Insured(get_input("Jméno: ", validate_name),
                get_input("Příjmení: ", validate_name),
                int(get_input("Věk: ", validate_age)),
                get_input("Telefon: ", validate_phone)
            )
        ),
        # Zobrazení seznamu pojištěných
        '2': lambda: print("\n".join(map(str, manager.list_insured())) if manager.list_insured() else "Seznam prázdný."),
        # Vyhledání pojištěného podle jména a příjmení
        '3': lambda: print("\n".join(map(str, manager.find_insured(get_input("Jméno: "), get_input("Příjmení: ")))) or "Nenalezen."),
        # Ukončení programu
        '4': exit
    }

    while True:
        print("\n1. Přidat pojištěného\n2. Zobrazit pojištěné\n3. Vyhledat pojištěného\n4. Konec")
        options.get(input("Vyberte možnost: "), lambda: print("Neplatná volba"))()

if __name__ == "__main__":
    main_short()