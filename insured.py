#Třída reprezentující pojištěného. Validuje, aby jméno a příjmení nebyly prázdné.

class Insured:
    def __init__(self, first_name: str, last_name: str, age: int, phone: str):
        # Ověření, že jméno a příjmení nejsou prázdné
        if not first_name or not last_name:
            raise ValueError("Jméno a příjmení nesmí být prázdné.")

        # Nastavení atributů objektu Insured
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone = phone

    # Metoda pro vrácení reprezentace objektu Insured ve formě řetězce
    def __str__(self):
        # Vrací jméno, příjmení, věk a telefon pojištěného ve formátovaném řetězci
        return f"{self.first_name} {self.last_name}, věk: {self.age}, telefon: {self.phone}"