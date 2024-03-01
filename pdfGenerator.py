#import class to generate html
from htmlGenerator import htmlGenerator

#import from_file to create pdf to a file
from pdfkit import from_file

#import os to delete file
import os

#function to create pdf
def pdfGenerator (array) :
    #open the html file
    htmlFile = open ("htmlFile.html", "w")

    #write in htmlFile the content gived from user and created by htmlGenerator
    htmlFile.write(htmlGenerator(array).generateHtmlContent())

    #close html file
    htmlFile.close()

    #from html file create pdf
    from_file("htmlFile.html", "paymentReceipt.pdf")
    
    #delete html file
    os.remove ("htmlFile.html")
