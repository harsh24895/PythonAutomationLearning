import re
def validate_postal_code(postal_code):

    postal_code_pattern = r'^[A-Za-z]\d[A-Za-z] \d[A-Za-z]\d$|^[A-Za-z]\d[A-Za-z]\d[A-Za-z]\d$'
    return bool(re.match(postal_code_pattern,postal_code))

def get_province(province_code):
    provinces = {
        "AB":  "Alberta",
        "BC": "British Columbia",
        "ON": "Ontario",
        "NS": "Nova Soctia"
    }
    return provinces.get(province_code,"Unknown")

def formate_address(street, city, province, postal_code):
    return f"{street},{city},{province},{postal_code}"
