import os; 
import PyPDF2
import argparse

 
def set_password(input_file, user_pass, owner_pass):
    path, filename = os.path.split(input_file)
    output_file = os.path.join(path, "temp_" + filename)
 
    output = PyPDF2.PdfFileWriter()
 
    input_stream = PyPDF2.PdfFileReader(open(input_file, "rb"))
 
    for i in range(0, input_stream.getNumPages()):
        output.addPage(input_stream.getPage(i))
 
    outputStream = open(output_file, "wb")
 
    output.encrypt(user_pass, owner_pass, use_128bit=True)
    output.write(outputStream)
    outputStream.close()
    os.rename(output_file, input_file)
 
 
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_pdf', required=True,
                        help='Input pdf file')
    parser.add_argument('-p', '--user_password', required=True,
                        help='output CSV file')
    parser.add_argument('-o', '--owner_password', default=None,
                        help='Owner Password')
    args = parser.parse_args()
    set_password(args.input_pdf, args.user_password, args.owner_password)
 
if __name__ == "__main__":
    main()
