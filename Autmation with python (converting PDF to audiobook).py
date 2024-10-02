import pyttsx3  
#pyttsx3 is a python library that convert text to speech
# install it first "pip install pyttsx3"
import PyPDF2
#PyPDF2 is a python library that extracts text from a PDF
# install it first "pip install PyPDF2"


#Read the PDF file 
#'rb' means we are reading the file in binary mode
#'strict = false ' helps with potential error handling in the PDF reading 

pdf_file=open(r"D:\Downloads\Alice In Wonderland.pdf" , 'rb') #replace it with your actual PDF path 
reader= PyPDF2.PdfReader(pdf_file , strict=False )

#count the number of pages in our chosen document 
number_of_pages= len(reader.pages)

#init function to begin engine instance
#iterate for loop over selected PDF pages 

engine=pyttsx3.init()

for i in range (0, number_of_pages):

    page = reader.pages[i]
  
    #extract the text from the selected pdf page 
    page_content=page.extract_text()

    #set the audio speed and volume 
    newspeed= 200
    engine.setProperty('rate' , newspeed)

    newvolume=200
    engine.setProperty('volume', newvolume)


    engine.say(page_content)

    #run and wait method to process voice command 
    engine.save_to_file(page_content , "pdf_audio.mp3")
    engine.runAndWait()
    engine.stop()





