"""
Re-open output.txt and append an additional line of your choice to the end of the file
on a new line
"""
outp = open("output.txt","a")
outp.write("\nHoladebola")
outp.close()
