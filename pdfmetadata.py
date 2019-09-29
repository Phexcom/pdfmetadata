
#!/usr/bin/env python3

from PyPDF2 import PdfFileReader, PdfFileWriter
import pprint
import pickle

def get_metadata(filename):
    # reading data from pdf file
    fin = open(filename, 'rb')

    # initializing  pyPDF2
    reader = PdfFileReader(fin)

    metadata = reader.getDocumentInfo()
    number_of_pages = reader.getNumPages()

    # Preparing data
    author = metadata.author
    creator = metadata.creator
    producer = metadata.producer
    subject = metadata.subject
    title = metadata.title
    pages = number_of_pages



    with open(filename + "_Output.txt", "w") as text_file:
        # print(metadata, file=text_file)
        pickle.dump(metadata, text_file)
    fin.close()
    pprint.pprint(metadata)
    print("Metadata has been saved to " + filename + "_Output.txt")

# Modifying the metadata of a pdf file
def modify_metadata(filename):
    fin = open(filename, 'rb')
    reader = PdfFileReader(fin)
    writer = PdfFileWriter()

    writer.appendPagesFromReader(reader)
    metadata = reader.getDocumentInfo()
    writer.addMetadata(metadata)

    # Write your custom metadata here:
    author = input("Author name: \n")
    creator = input("Creator: \n")
    producer = input("Producer: \n")
    subject = input("Subject: \n")
    title = input("Title: \n")

    writer.addMetadata({
        '/Title': title,
        '/Author': author,
        '/Creator': creator,
        '/Producer': producer,
        '/Subject': subject
    })

    fout = open(file, 'ab')
    writer.write(fout)

    print("Metadata has been modified")
    fin.close()
    fout.close()

    get_metadata(filename)


if __name__ == '__main__':
    while True:
        option = input("1. Get PDF Metadata\n2. Modify PDF Metadata\n")

        if  option == "1":
            file = input('Enter pdf file path to get metadata (ex. book.pdf)\n')
            get_metadata(file)
        elif option == "2":
            file = input('Enter pdf file path to modify metadata (ex. book.pdf)\n')
            modify_metadata(file)
        else:
            print("Invalid input!!!")
            exit(0)

