class TaxBand:
      def __init__(self, low, high, rate):
          self.low = low
          self.high = high
          self.rate = rate
          
def calculate_lbtt(property_value):
    
    tax_bands = [TaxBand(0,145000,0),TaxBand(145000,250000,0.02),TaxBand(250000,325000,0.05),TaxBand(325000,750000,0.1),TaxBand(750000,float('inf'),0.12)]
    bands = []
    tax = 0
    
    for band in tax_bands:
        if band.low < property_value:
            bands.append(band)
    
    for band in bands:
        if band.high < property_value:
            tax += (band.high-band.low)*band.rate
        else:
            tax += (property_value-band.low)*band.rate
    
    return round(tax,2)

def validateInput(property_value):
    print('okay')
    # check if a int or double
    # cheeck if a string
    # check if negative
    return True



if __name__ == "__main__":
    validated = False
    while not validated:
        property_value = input("House Cost: ")
        validated = validateInput(property_value)
        
    # poperty_value = 325000
    tax = calculate_lbtt(property_value)
    print(tax)


# def validateInput():
#     print('Please enter the cost of the house without any grammer.')
#     while True:
#         try:
#             property_value = float(input("House Cost: "))
#             if(property_value<0):
#                 print('You inputed a negative number.')
#             else:
#                 return property_value
#         except ValueError:
#             print('You inputed a string.')

# if __name__ == "__main__":
#     property_value = validateInput()
#     # poperty_value = 325000
#     tax = calculate_lbtt(property_value)
#     print(tax)


