class TaxBand:
    '''A model to store a tax band.'''
    def __init__(self, low, high, rate):
        self.low = low
        self.high = high
        self.rate = rate


def calculate_lbtt(property_value):  
    '''Function that calculates the LBBT cost. Must be given a number and returns a number.'''
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

def user_input():
    '''Function that takes user input and validates it. Returns a number.'''
    while True:
        try:
            property_value = float(input("House Cost: "))
            if(property_value<0):
                print('You inputed a negative number.')
            else:
                return property_value
        except ValueError:
            print('Please only input numbers.')

if __name__ == "__main__":
    # User input with validation
    property_value = user_input()
    
    # User input without validation
    # property_value = float(input("House Cost: "))
    
    # Hard coded value
    # property_value = 325000
    
    tax = calculate_lbtt(property_value)
    print(tax)