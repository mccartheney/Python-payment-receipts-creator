#import date to get date
from datetime import date

#class to create html
class htmlGenerator :
    #init method to get shopping array
    def __init__ (self, array) :
        self.shoppingArray = array

    #method to get date
    def getDate (self) :
        return date.today()
    
    #method to get total value for all pursages
    def getTotalValue (self) :
        #initialize total value as 0
        totalValue = 0

        #loop trought shoppingArray
        for thing in self.shoppingArray :
            #get the value
            value = thing[1]

            #add value to total value
            totalValue += value

        #return total value
        return totalValue

    #method to generate ShoppingHtmlContent
    def generateShoppingHtmlContent (self) :
        #all all content as empty
        allTrContent = ""

        #loop trought shoppingArray
        for thing in self.shoppingArray :
            #get name
            name = thing[0]

            #get price
            price = thing[1]

            #create table html content
            trContent = f'''
            <tr>
                <td>{self.getDate()}</td>
                <td class="name">{name}</td>
                <td class="price">{price}</td>
            </tr>
            '''

            #add that content to all content
            allTrContent += trContent

        #return all content
        return allTrContent

    #method to create final html content
    def generateHtmlContent (self) :
        #create html content
        htmlContent = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <style>
        @import url('https://fonts.googleapis.com/css2?family=Anta&display=swap');


        body {
            height: 100vh;
            background-color: white;
            font-family: "Anta", sans-serif;
            font-weight: 400;
            font-style: normal;
        }

        table {
            width: 100%%;
            color: white;
            background-color: rgb(63, 29, 95);
        }

        td {
            padding: 10px;
        }

        .price {
            text-align: right;
        }

        .total {
            position: relative;
            height: 15px;
        }

        .totalString {
            position: absolute;
            left: 10px;
            top: 0px;

        }

        .totalValue {
            position: absolute;
            right: 10px;
            top: 0px;
        }
    </style>
</head>
<body>
    <table>
        <tr>
            <td>Date</td>
            <td class="name">Name</td>
            <td class="price">Price</td>
        </tr>

        %s

        <tr>
            <td colspan="3" class="total">
                <span class="totalString">
                    total
                </span>
                <span class="totalValue">
                    %d
                </span>
            </td>
        </tr>
    </table>
</body>
</html>
        ''' % (self.generateShoppingHtmlContent(), self.getTotalValue ())

        #return html content
        return htmlContent
