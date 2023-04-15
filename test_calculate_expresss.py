from function_calculate_express import calculate_price
import pytest


#weight <0
@pytest.mark.validate
def test_weight_0_region_central():
  weight_product = 0
  region = "Central"
  expected_result = "invalid weight"
  actual_result = calculate_price(weight_product,region)
  assert expected_result == actual_result

#weight <0
@pytest.mark.validate
def test_weight_0_region_south():
  weight_product = 0
  region = "Eastern"
  expected_result = "invalid weight"
  actual_result = calculate_price(weight_product,region)
  assert expected_result == actual_result

#weight <0
@pytest.mark.validate
def test_weight_0_western():
  weight_product = 0
  region = "Western"
  expected_result = "invalid weight"
  actual_result = calculate_price(weight_product,region)
  assert expected_result == actual_result

#weight <0
@pytest.mark.validate
def test_weight_0_north():
  weight_product = 0
  region = "North"
  expected_result = "invalid weight"
  actual_result = calculate_price(weight_product,region)
  assert expected_result == actual_result

#weight <0
@pytest.mark.validate
def test_weight_0_north():
  weight_product = 0
  region = "Northeast"
  expected_result = "invalid weight"
  actual_result = calculate_price(weight_product,region)
  assert expected_result == actual_result

#weight <0
@pytest.mark.validate
def test_weight_0_north():
  weight_product = 0
  region = "Southern"
  expected_result = "invalid weight"
  actual_result = calculate_price(weight_product,region)
  assert expected_result == actual_result



#weight < -1
@pytest.mark.validate
def test_weight_product_minus_1():
  weight_product = -1
  region = "Central"
  expected_result = "invalid weight"
  actual_result = calculate_price(weight_product,region)
  assert expected_result == actual_result

#weight < -1
@pytest.mark.validate
def test_weight_product_minus_1():
  weight_product = -1
  region = "Eastern"
  expected_result = "invalid weight"
  actual_result = calculate_price(weight_product,region)
  assert expected_result == actual_result


#weight < -1
@pytest.mark.validate
def test_weight_product_minus_1():
  weight_product = -1
  region = "Western"
  expected_result = "invalid weight"
  actual_result = calculate_price(weight_product,region)
  assert expected_result == actual_result

#weight < -1
@pytest.mark.validate
def test_weight_product_minus_1():
  weight_product = -1
  region = "North"
  expected_result = "invalid weight"
  actual_result = calculate_price(weight_product,region)
  assert expected_result == actual_result

#weight < -1
@pytest.mark.validate
def test_weight_product_minus_1():
  weight_product = -1
  region = "Northeast"
  expected_result = "invalid weight"
  actual_result = calculate_price(weight_product,region)
  assert expected_result == actual_result


#weight < -1
@pytest.mark.validate
def test_weight_product_minus_1():
  weight_product = -1
  region = "Southern"
  expected_result = "invalid weight"
  actual_result = calculate_price(weight_product,region)
  assert expected_result == actual_result



#input all 0
@pytest.mark.validate
def test_weight_product_region_0():
  weight_product = 0
  region = 0
  expected_result = "All inputs are invalid"
  actual_result = calculate_price(weight_product,region)
  assert expected_result == actual_result

#input weight as string 
@pytest.mark.validate
def test_weight_input_a():
  weight_product = "a"
  region = "Central"
  expected_result = "Input weight as integer or float"
  actual_result = calculate_price(weight_product,region)
  assert expected_result == actual_result

#input weight as string 
@pytest.mark.validate
def test_weight_input_a():
  weight_product = "a"
  region = "Eastern"
  expected_result = "Input weight as integer or float"
  actual_result = calculate_price(weight_product,region)
  assert expected_result == actual_result

#input weight as string 
@pytest.mark.validate
def test_weight_input_a():
  weight_product = "a"
  region = "Western"
  expected_result = "Input weight as integer or float"
  actual_result = calculate_price(weight_product,region)
  assert expected_result == actual_result

#input weight as string 
@pytest.mark.validate
def test_weight_input_a():
  weight_product = "a"
  region = "North"
  expected_result = "Input weight as integer or float"
  actual_result = calculate_price(weight_product,region)
  assert expected_result == actual_result

#input weight as string 
@pytest.mark.validate
def test_weight_input_a():
  weight_product = "a"
  region = "Northeast"
  expected_result = "Input weight as integer or float"
  actual_result = calculate_price(weight_product,region)
  assert expected_result == actual_result

#input weight as string 
@pytest.mark.validate
def test_weight_input_a():
  weight_product = "a"
  region = "Southern"
  expected_result = "Input weight as integer or float"
  actual_result = calculate_price(weight_product,region)
  assert expected_result == actual_result

#input region as string 
@pytest.mark.validate
def test_region_integer():
  weight_product = 9
  region = 1
  expected_result = "Input region as string"
  actual_result = calculate_price(weight_product,region)
  assert expected_result == actual_result

#input region as invalid 
@pytest.mark.validate
def test_region_invalid():
  weight_product = 10
  region = "F"
  expected_result = "Input region as invalid"
  actual_result = calculate_price(weight_product,region)
  assert expected_result == actual_result

#input region as invalid 
@pytest.mark.validate
def test_weight_region_invalid():
  weight_product = -1
  region = "A"
  expected_result = "Input region and weight as invalid"
  actual_result = calculate_price(weight_product,region)
  assert expected_result == actual_result
