from pdfGenerator import pdfGenerator


def getPursages () :
    #set Pursages array as empty array
    pursagesArray = []

    #ask and get the quantity
    pursageNumber = int(input ("how many purchases will be on the receipt\n\n==>"))

    #get all Pursages with a loop
    for i in range(pursageNumber) :
        #get name
        name = input(f"What is the content of bought ({i+1})?\n\n==> ")

        #get price
        price = int(input("how much does it cost?\n\n==> "))

        #append this pursage to pursagesArray
        pursagesArray.append([name,price])

    #return Pursages array
    return pursagesArray

if __name__ == "__main__" :
    #get all pursages
    allPursages = getPursages()

    #create receipt pdf with allPursages data
    pdfGenerator(allPursages)