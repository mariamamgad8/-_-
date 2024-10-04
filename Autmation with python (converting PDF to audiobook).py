import pyttsx3  
import PyPDF2

# Get the PDF path from the user
pdf_path = input("Enter the path to the PDF file: ")

# Read the PDF file
pdf_file = open(pdf_path, 'rb')  # User provided path
reader = PyPDF2.PdfReader(pdf_file)

# Count the number of pages in the document
number_of_pages = len(reader.pages)

# Initialize pyttsx3 engine
engine = pyttsx3.init()

# Set audio speed and volume
newspeed = 200  # Set the speed of the speech
engine.setProperty('rate', newspeed)

newvolume = 1.0  # Volume should be between 0.0 and 1.0
engine.setProperty('volume', newvolume)

# Variable to store the full text of the PDF
full_text = ""

# Iterate over all pages and extract text
for i in range(number_of_pages):
    page = reader.pages[i]
    page_content = page.extract_text()
    full_text += page_content

# Speak the text (optional)
engine.say(full_text)

# Save the audio to a file
engine.save_to_file(full_text, "pdf_audio.mp3")

# Run the engine
engine.runAndWait()

# Close the PDF file
pdf_file.close()

print("The PDF has been converted to audio and saved as 'pdf_audio.mp3'.")
