# Pseudocode:
# * Define a function that calculates paracetamol volume based on weight and drug strength
# * Check if the weight is within 10–100 kg
# * Check if strength is 120 mg/5ml or 250 mg/5ml
# * Convert strength to mg/ml
# * Calculate the total dose as 15 mg/kg
# * Calculate the required volume (dose / concentration)
# * Return the volume rounded to 2 decimal places
# * Demonstrate the function using a sample input and print result

def calculate_paracetamol_volume(weight, strength):
    if not (10 <= weight <= 100):
        raise ValueError("Weight should be between 10 and 100 kg")
    if strength not in ["120 mg/5ml", "250 mg/5ml"]:
        raise ValueError("Strength must be '120 mg/5ml' or '250 mg/5ml'")

    if strength == "120 mg/5ml":
        concentration = 120 / 5  # = 24 mg/ml
    else:
        concentration = 250 / 5  # = 50 mg/ml

    dose = weight * 15  # 15 mg/kg
    volume = dose / concentration
    return round(volume, 2)

# Example usage
try:
    vol = calculate_paracetamol_volume(25, "120 mg/5ml")
    print(f"Required volume: {vol} ml")
except ValueError as e:
    print(f"Error: {e}")
