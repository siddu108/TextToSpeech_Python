import pyttsx3
import PyPDF2
book = open('samplebook.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
page = pdfReader.getPage(0)
text=page.extractText()
#speaker.say("Hare Krishna Hare Krishna Krishna Krishna Hare Hare Hare Rama Hare Rama Rama Rama Hare Hare")
speaker.say(text)
speaker.runAndWait()
