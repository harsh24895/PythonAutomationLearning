from coverage.files import actual_path

from practice_class12.address_helper import validate_postal_code,get_province,formate_address
import pytest
def test_address():
    valid_address = "M5P 1T5"
    expected_result = True

    compare_output = validate_postal_code(valid_address)
    assert compare_output == expected_result


#here we are using the decoder to compare the province code
@pytest.mark.parametrize('province_code,expected_value',[
                         ("AB", "Alberta"),
                         ("BC", "British Columbia"),
                         ("ON", "Ontario"),
                         ("NB", "New Brunswick")])
def test_province_name(province_code,expected_value):

    province = get_province(province_code)

    assert province == expected_value


def test_fulladdress():
    city = "Edmonton"
    street = "155 Main St"
    province = "AB"
    postal_code = "E5P 15Y"

    expected_output = "155 Main St,Edmonton,AB,E5P 15Y"
    #Act
    actual_output = formate_address(street,city,province,postal_code)
    #Assert
    assert actual_output == expected_output

#Testing Invalid postal code
def test_invalid_postalcode():
    invalid_postalcode = "M555 IP"

    actual_postal = validate_postal_code(invalid_postalcode)

    assert actual_postal == True

#Missing postalcode
def test_missing_postalcode():
    #Arrange
    missing_postalcode = " "
    expected_output = False

    #act
    actual_output = validate_postal_code(missing_postalcode)

    with pytest.raises(TypeError):
        validate_postal_code()

    #Assert
    assert actual_output == expected_output

#incorrect characters in the postalcode
def test_incorrect_characters_in_postalcode():
    #Arrange
    actual_input = "npr "
    expected = False
    #Act
    actual_output = validate_postal_code(actual_input)

    #Assert
    assert actual_output == expected
