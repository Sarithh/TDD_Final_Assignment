def validate_input(weight_product, region):
    if type(weight_product) == str:
        if region == "Central" or region == "Eastern" or region == "Western" or region == "North" or region == "Northeast" or region == "Southern":
            return "Input weight as integer or float"
        else:
            return ""
    elif type(region) != str:
        if weight_product < 0:
            return "All inputs are invalid"
        else:
            return "Input region as string"
    elif (type(weight_product) == float or type(weight_product) == int) and type(region) == str:
        if weight_product >= 0 and (region == "Central" or region == "Eastern" or region == "Western" or region == "North" or region == "Northeast" or region == "Southern"):
            return weight_product, region
    elif weight_product >= 0 and (region != "Central" and region != "Eastern" and region != "Western" and region != "North" and region != "Northeast" and region != "Southern"):
        return "Input region is invalid"
    else:
        if weight_product < 0 and (region != "Central" and region != "Eastern" and region != "Western" and region != "North" and region != "Northeast" and region != "Southern"):
            return "Input region and weight as invalid"
        else:
            return "invalid weight"


def calculate_price(weight_product, region):
    validated = validate_input(weight_product, region)
    if (type(weight_product) == float or type(weight_product) == int) and type(region) == str:
        if weight_product >= 0 and (region == "Central" or region == "Eastern" or region == "Western" or region == "North" or region == "Northeast" or region == "Southern"):
            if weight_product > 20:
                price = 500
            elif weight_product >= 10:
                if region == "Central" or region == "Eastern" or region == "Western":
                    price = 420
                else:
                    price = 460
            elif weight_product > 0:
                if region == "Central" or region == "Eastern" or region == "Western":
                    price = 200
                else:
                    price = 240
            elif weight_product == 0:
                price = 0
            return price
        else:
            return validated
    else:
        return validated
