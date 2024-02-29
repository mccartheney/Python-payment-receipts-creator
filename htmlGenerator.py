from datetime import date

class htmlGenerator :
    def __init__ (self) :
        pass

    def getDate (self) :
        return date.today
    

    def generateHtmlContent (self) :
        #create html content
        htmlContent = f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            
        </body>
        </html>
        '''

        #return html content
        return htmlContent
    