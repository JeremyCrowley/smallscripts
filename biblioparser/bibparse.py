
import math
import numpy


def writeToFile(books, thesis, chapters, journals, conference, techreports, unpub):

	f = open("PublicationNumbers.tex", 'w')

	# write each list to the file omitting the brackets with [1:-1]

	f.write("\subsection{Book}\n")
	f.write("\cite{" + str(books)[1:-1] + "}\n\n")

	f.write("\subsection{Thesis and Dissertations}\n")
	f.write("\cite{" + str(thesis)[1:-1] + "}\n\n")

	f.write("\subsection{Peer-reviewed Book Chapters}\n")
	f.write("\cite{" + str(chapters)[1:-1] + "}\n\n")

	f.write("\subsection{Peer-reviewed Journal Publications}\n")
	f.write("\cite{" + str(journals)[1:-1] + "}\n\n")

	f.write("\subsection{Peer-reviewed Conference Publications (in proceedings)}\n")
	f.write("\cite{" + str(conference)[1:-1] + "}\n\n")

	f.write("\subsection{Technical Reports}\n")
	f.write("\cite{" + str(techreports)[1:-1] + "}\n\n")

	f.write("\subsection{Unpublished}\n")
	f.write("\cite{" + str(unpub)[1:-1] + "}\n\n")
	


def main():

	thes = []
	book = []
	chap = []
	jour = []
	conf = []
	tech = []
	unpub = []

	bibfile = open("Biblio-Bibtex.bib");

	for line in bibfile:

		if "@" in line:

			bracket = line.index("{")
			comma = line.index(",")

			# discard any entries without citation numbers
			if bracket+1 == comma:
				continue

			num = line[bracket+1:comma]


			if(num[0] == "-"):
				num = num[1:]

			# check that the num is a valid integer and positive 
			if num.isdigit():


				if "inbook" in line:
					chap.append(int(num))
				elif "book" in line:
					book.append(int(num))
				elif "article" in line:
					jour.append(int(num))
				elif "inproceedings" in line:
					conf.append(int(num))
				elif "thesis" in line:
					thes.append(int(num))
				elif "techreport" in line:
					tech.append(int(num))
				elif "unpublished" in line:
					unpub.append(int(num))
				else:
					print "type not found: " + line
			else:
				print num


	writeToFile(book, thes, chap, jour, conf, tech, unpub)


if __name__ == '__main__':
	main()



