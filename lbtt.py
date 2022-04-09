# Model to hold the tax data
class TaxBand:
      def __init__(self, low, high, rate):
          self.low = low
          self.high = high
          self.rate = rate

# Function that calculates the LBBT cost
# Must be given a number (int or double) and returns a number
def calculate_lbtt(property_value):  
    tax_bands = [TaxBand(0,145000,0),TaxBand(145000,250000,0.02),TaxBand(250000,325000,0.05),TaxBand(325000,750000,0.1),TaxBand(750000,float('inf'),0.12)]
    bands = []
    tax = 0
    
    # Loop that removes tax bands from calculation that aren't needed
    for band in tax_bands:
        if band.low < property_value:
            bands.append(band)
    
    # Loop that goes through the tax bands and calculates the tax
    for band in bands:
        if band.high < property_value:
            tax += (band.high-band.low)*band.rate
        else:
            tax += (property_value-band.low)*band.rate
    
    return round(tax,2)

# Basic user input with validation
def user_input():
    print('Please enter the cost of the house without any grammer.')
    while True:
        try:
            property_value = float(input("House Cost: "))
            if(property_value<0):
                print('You inputed a negative number.')
            else:
                return property_value
        except ValueError:
            print('You inputed a string.')

if __name__ == "__main__":
    # User input with validation
    property_value = user_input()
    
    # User input without validaiton
    # property_value = float(input("House Cost: "))
    
    # Hard coded value
    # property_value = 325000
    
    tax = calculate_lbtt(property_value)
    
    # Print the return on its own or in a sentance
    print(tax)
    # print("The LBTT cost is £{:.2f}".format(tax))