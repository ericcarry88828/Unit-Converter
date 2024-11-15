
def get_differ_units(unit):
    if unit == "length":
        length = {"mm": 1, "cm": 0.1, "m": 0.001, "km": 0.000001, "inch": 0.0393701,
                  "foot": 0.0032808404, "yard": 0.0010936124, "mile": 39.370046}
        return length
    elif unit == "weight":
        weight = {"mg": 1, "g": 0.001, "kg": 0.000001,
                  "oz": 0.00003527396, "lb": 0.00003527396}
        return weight
    elif unit == "temperature":
        temperature = {"c": {"f": [1.8, 32], "k": 273.15},
                       "f": {"k": [5, 9, 32, 273.15], "c": [5, 9, 32]},
                       "k": {"f": [1.8, 459.67], "c": 273.15}}
        return temperature
    return False


def units_of_length(number, convert_from, convert_to):
    unit = get_differ_units("length")
    convert_from_scale = unit[convert_from]
    convert_to_scale = unit[convert_to]
    cal = (float(number) / convert_from_scale) * convert_to_scale
    res = str(number) + f" {convert_from} = " + f"{cal}{convert_to}"
    return res


def units_of_weight(number, convert_from, convert_to):
    unit = get_differ_units("weight")
    convert_from_scale = unit[convert_from]
    convert_to_scale = unit[convert_to]
    cal = (float(number) / convert_from_scale) * convert_to_scale
    res = str(number) + f" {convert_from} = " + f"{cal}{convert_to}"
    return res


def units_of_temperature(number, convert_from, convert_to):
    unit = get_differ_units("temperature")
    if convert_from == "c":
        if convert_to == "f":
            cal = (float(number) * unit["c"]["f"][0]) + unit["c"]["f"][1]
        else:
            cal = float(number) + unit["c"]["k"]
    elif convert_from == "f":
        if convert_to == "c":
            cal = (float(number) - unit["f"]["c"][2]) * \
                unit["f"]["c"][0] / unit["f"]["c"][1]
        else:
            cal = (float(number) - unit["f"]["k"][2]) * \
                unit["f"]["k"][0] / unit["f"]["k"][1] + unit["f"]["k"][3]
    else:
        if convert_to == "c":
            cal = float(number) - unit["k"]["c"]
        else:
            cal = (float(number) * unit["k"]["f"][0]) - unit["k"]["f"][1]
    res = str(number) + f" {convert_from} = " + f"{cal}{convert_to}"
    return res


def check_valid_input(unit: str, input_colunm_lists: list[str] = None):
    units = get_differ_units(unit)
    if not all(input_colunm_lists):
        return False, "All input boxes cannot be empty!"

    if not input_colunm_lists[0].isdigit():
        return False, f"This first input box must be a number!"
    elif input_colunm_lists[1] not in units:
        return False, f"{input_colunm_lists[1]} is not a unit of {unit}"
    elif input_colunm_lists[2] not in units:
        return False, f"{input_colunm_lists[2]} is not a unit of {unit}"
    return True, "All input is valid"
