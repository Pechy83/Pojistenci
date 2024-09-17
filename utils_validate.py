#Obsahuje pomocné funkce pro validaci vstupu.

def get_input(prompt: str, validation_func=None) -> str:
    value = input(prompt).strip()
    if not value:
        print("Tento údaj je povinný!")
        return get_input(prompt, validation_func)
    if validation_func:
        try:
            value = validation_func(value)
        except ValueError as e:
            print(e)
            return get_input(prompt, validation_func)
    return value

def validate_name(name: str) -> str:
    if not name.isalpha():
        raise ValueError("Jméno musí obsahovat pouze písmena.")
    return name

def validate_age(age: str) -> int:
    try:
        age = int(age)
        if age < 0:
            raise ValueError("Věk musí být kladné číslo.")
        return age
    except ValueError:
        raise ValueError("Věk musí být celé číslo.")


def validate_phone(phone: str) -> str:
    # Odstraní případné bílé znaky na začátku a konci
    phone = phone.strip()

    # Uchová informaci, zda číslo začíná "+"
    has_plus = phone.startswith("+")

    # Pokud číslo začíná na "+", odstraní "+" pro účely další validace
    if has_plus:
        phone = phone[1:]

    # Kontrola, zda zbývající část obsahuje pouze číslice a má alespoň 7 číslic
    if not phone.isdigit() or len(phone) < 7:
        raise ValueError("Telefonní číslo musí obsahovat pouze číslice a mít alespoň 7 číslic.")

    # Vrátí telefonní číslo i s původním "+"
    return "+" + phone if has_plus else phone