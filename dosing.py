"""dosing.py
    Example program of calculating first-day dose of medicine for pediatric
        patients.
    NOTE:  This is a programming example, and should not be used for any
             type of medical treatment or diagnostics.
"""

# Program Driver (kind of like the main function) (the order you call all funcs)
def dose_amount():
    diag, w_input = get_user_input()
    wt, dose_1 = calculate_dosage(diag, w_input)
    output_results(w_input, dose_1)
    
# Input function    
def get_user_input():
    print("Day One Dosing Guidelines")
    print("")
    print("Choose diagnosis:")
    print("1 - Acute otitis media")
    print("2 - Acute bacterial sinusitis")
    print("3 - Community-acquired pneumonia")
    print("4 - Pharyngitis/tonsilitis")
    diagnosis = int(input("Enter a number: "))
    
    print("PATIENT WEIGHT")
    print("Enter patient weight followed by units of kg or lb.")
    print("Examples:  65.3 lb      21.0 kg")
    weight_input = input("Enter weight: ")
    
    weight_data = weight_input.split(" ")
    weight = float(weight_data[0])
    units = weight_data[1]
    if units == "lb":
        weight = weight / 2.205
    #calculate_dosage(diagnosis, weight)
    return diagnosis, weight #instead of call all these functions, return the outputs!!!
    
# Calculations function (can be further break into unit conversion and calculation)
def calculate_dosage(diagnosis, weight):
    dosages_mg_per_kg = [30, 10, 10, 12]
    dosage_mg_per_kg = dosages_mg_per_kg[diagnosis-1]
    dosage_mg_first_day = weight * dosage_mg_per_kg
    #output_results(weight, dosage_mg_first_day)
    return weight, dosage_mg_first_day
 
# Output fucntion   
def output_results(weight, dosage_mg_first_day):
    print("CORRECT DOSAGE")
    print("For a patient weighing {:.1f} kg,".format(weight))
    print("  the correct dosage is {:.1f} mg the first day"
          .format(dosage_mg_first_day))

# To be testable:
if __name__ == '__main__':  
    dose_amount() #the program driver
