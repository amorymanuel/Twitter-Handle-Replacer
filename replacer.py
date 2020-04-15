import csv
import sys

csvname = str(sys.argv[1])

with open(csvname) as handlelist:
	reader = csv.reader(handlelist)
	next(reader)
	for row in reader:
		newcode=""
		realname = row[0]
		handle = row[1]
		newcode = "    if (inputname == \"" + realname + "\") {" + "\n" + "    " + "    " + "newcell.setValue(\""
		if (row[2]=='x'):
		 	newcode += realname
		 	newcode += " "
		newcode += handle
		newcode += "\");\n    }\n\n"
		print(newcode)


