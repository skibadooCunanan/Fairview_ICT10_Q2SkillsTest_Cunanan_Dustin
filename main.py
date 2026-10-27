from pyscript import document

Elements = {
    "H": ("Hydrogen", 1, 1.008),
    "He": ("Helium", 2, 4.003),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "F": ("Fluorine", 9, 18.998),
    "Ne": ("Neon", 10, 20.180),
    "P": ("Phosphorus", 15, 30.974),
    "S": ("Sulfur", 16, 32.060),
    "Cl": ("Chlorine", 17, 35.450),
    "Ar": ("Argon", 18, 39.948),
    "Se": ("Selenium", 34, 78.971),
    "Br": ("Bromine", 35, 79.904),
    "Kr": ("Krypton", 36, 83.798),
    "I": ("Iodine", 53, 126.904),
    "Xe": ("Xenon", 54, 131.293),
    "At": ("Astatine", 85, 210),
    "Rn": ("Radon", 86, 222),
    "Ts": ("Tennessine", 117, 294),
    "Og": ("Oganesson", 118, 294)
} # List of elements

def find_element(event):
    Element1 = document.getElementById("Element1").value.strip().capitalize()

    result = Elements.get(
        Element1,
        ("Element not found", "-", "-")
    )

    document.getElementById("symbol_output").innerText = Element1
    document.getElementById("name_output").innerText = result[0]
    document.getElementById("number_output").innerText = result[1]
    document.getElementById("mass_output").innerText = result[2]