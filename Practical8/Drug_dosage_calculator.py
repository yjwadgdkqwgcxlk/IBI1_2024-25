# exclude values not in the range
# determine recommanded dose
# determine required dose considering the strength
# calculate volume  

def calculate_paracetamol_volume(weight, strength):
    # exclude values not in the range
    if not (10 <= weight <= 100):
        raise ValueError("Weight should be between 10 and 100 kg")
    if strength not in [120, 250]:
        raise ValueError("Invalid paracetamol strength")
    # exclude values not in the range
    recommended_dose = 15  # mg/kg
    required_dose = weight * recommended_dose
    # exclude values not in the range
    if strength == 120:
        concentration = 120
    else:
        concentration = 250 
    # exclude values not in the range
    volume = required_dose / concentration
    return volume

# an example
vol = calculate_paracetamol_volume(50, 120)
print (vol)
# the result is vol = 6.25