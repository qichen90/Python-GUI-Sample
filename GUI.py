## Python GUI Programming - string edit distance QI CHEN 10/16/2014
## use greedy algorithm to compute string edit distance, time O(nm)

from Tkinter import *
import tkFont
import os.path

#########################################################create the application ##########################
class Application(Frame):
	# GUI application
	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.create_userinterface()

    ##################################################### create widgets part ###############################
	def create_userinterface(self):

		# display instruction label
		Label(self, 
			text = "Enter information for computing string edit distance"
			).grid(row = 0, column = 0, columnspan = 2, sticky = W)

		# display useful notes for users
		Label(self, 
			text = "Notes: All costs are postive integer values."
			).grid(row = 1, column = 0, columnspan = 2, sticky = W)

		Label(self, 
			text = "Make sure that files are under the directory then you can specify a text file name for each string."
			).grid(row = 2, column = 0, columnspan = 2, sticky = W)

		
		# create a label and text entry for cdel
		Label(self, 
			text = "The cost of deletion (cdel):"
			).grid(row = 3, column = 0, sticky = W)
		self.cdel = IntVar()
		self.scale_cdel = Scale(self, variable = self.cdel, orient = HORIZONTAL)
		self.scale_cdel.grid(row = 3, column = 1, sticky = W)

		# create a label and text entry for cins
		Label(self, 
			text = "The cost of insertion (cins):"
			).grid(row = 4, column = 0, sticky = W)
		self.cins = IntVar()
		self.scale_cins = Scale(self, variable = self.cins, orient = HORIZONTAL)
		self.scale_cins.grid(row = 4, column = 1, sticky = W)

		# create a label and text entry for csub
		Label(self, 
			text = "The cost of substitution (csub):"
			).grid(row = 5, column = 0, sticky = W)
		self.csub = IntVar()
		self.scale_csub = Scale(self, variable = self.csub, orient = HORIZONTAL)
		self.scale_csub.grid(row = 5, column = 1, sticky = W)

		# create a label and text entry for input string S
		Label(self, 
			text = "Input string S or a file name:"
			).grid(row = 6, column = 0, sticky = W)
		self.input_S = Entry(self)
		self.input_S.grid(row  = 6, column = 1, sticky = W)

		# create check button for file 
		self.check_fileS = BooleanVar()
		Checkbutton(self, text = "if S is a file, please check.", 
			variable = self.check_fileS
			).grid(row = 6, column = 2, sticky = W)

		# create a label and text entry for input string T
		Label(self, 
			text = "Input string T or a file name:"
			).grid(row = 7, column = 0, sticky = W)
		self.input_T = Entry(self)
		self.input_T.grid(row = 7, column = 1, sticky = W)

		#### Enhancement: to accept file names
		# create check button for file 
		self.check_fileT = BooleanVar()
		Checkbutton(self, text = "if T is a file, please check.", 
			variable = self.check_fileT
			).grid(row = 7, column = 2, sticky = W)

		# create a label for checkbox button
		Label(self, 
			text = "Output perferences:"
			).grid(row = 8, column = 0, sticky = W)

		# create full edit distance matrix check button
		self.check_fdist = BooleanVar()
		Checkbutton(self, text = "full edit distance matrix", 
			variable = self.check_fdist
			).grid(row = 8, column = 1, sticky = W)	

		# create backtrack matrix check button
		self.check_btrack = BooleanVar()
		Checkbutton(self, text = "backtrack matrix", 
			variable = self.check_btrack
			).grid(row = 9, column = 1, sticky = W)		
		
		# create alignment check button
		self.check_align = BooleanVar()
		Checkbutton(self, text = "alignment", 
			variable = self.check_align
			).grid(row = 10, column = 1, sticky = W)		
		
		# create a compare button
		Button(self, text = "Compare",
			command = self.computation
			).grid(row = 11, column = 0, sticky = W)

		#### Enhancement: for clear button
		# create a clear button
		Button(self, text = "Clear",
			command = self.clear_textbox
			).grid(row = 11, column = 2, sticky = W)

		# create a text box to display the results with x scrollbar and y scrollbar. Use a fixed width font.
		fixed_width_font = tkFont.nametofont("TkFixedFont")
		self.results = Text(self,  width = 115, height = 20, wrap = NONE, font = fixed_width_font)
		self.results.grid(row = 12, column = 0, columnspan = 4, sticky = W)
		scrollby = Scrollbar(self, command = self.results.yview)
		scrollby.grid(row = 12, column = 4, sticky = N + S + E + W)
		self.results['yscrollcommand'] = scrollby.set
		scrollbx = Scrollbar(self, orient = HORIZONTAL)
		scrollbx.grid(row = 13, column = 0, sticky = N + S + E + W)
		scrollbx.config(command = self.results.xview)
		self.results['xscrollcommand'] = scrollbx.set
	#### Enhancement: for clear button	
	def clear_textbox(self):
		self.results.delete("1.0", "end") 

	################################################################ computation part ########################
	def computation(self):

		# get values from the GUI
		cdel = self.cdel.get()
		cins = self.cins.get()
		csub = self.csub.get()
		S = self.input_S.get()
		T = self.input_T.get()

		# the input S, T are filenames; when the file can not open or it actually not file, it will show warning in the textbox
		if self.check_fileS.get():
			if os.path.isfile(S):
				f = open(S, 'r')
				S = ""
				for line in f:
					S = S + line
				f.close()

			#### Enhancement: to accept file names
			else:
				self.results.insert(END, 'Warning: File S can not open. File name is considered as a string to be computed.')
				self.results.insert(END, '\n')

		if self.check_fileT.get():
			if os.path.isfile(T):
				f = open(T, 'r')
				T = ""
				for line in f:
					T = T + line
				f.close()

			#### Enhancement: to accept file names
			else:
				self.results.insert(END, 'Warning: File T can not open. File name is considered as a string to be computed.')
				self.results.insert(END, '\n')

		lengthofS = len(S)
		lengthofT = len(T)
		
		# create matrics
		distmatrix = [[' ' for y in range(lengthofT + 2)] for x in range(lengthofS + 2)]
		backmatrix = [[' ' for y in range(lengthofT + 2)] for x in range(lengthofS + 2)]

		distmatrix[1][1] = 0
		backmatrix[1][1] = 0 
		
		for i in range(2, lengthofS + 2):
			distmatrix[i][0] = S[i - 2]
			backmatrix[i][0] = S[i - 2]
		for j in range(2, lengthofT + 2):
			distmatrix[0][j] = T[j - 2]
			backmatrix[0][j] = T[j - 2]

		# initial conditions: dist[i, 0] = dist[i-1] + cdel; dist[0, j] = dist[0, j-1] + cins
		for i in range(2, lengthofS + 2):
			distmatrix[i][1] = distmatrix[i - 1][1] + cdel
			backmatrix[i][1] = '|'
		
		for j in range(2, lengthofT + 2):
			distmatrix[1][j] = distmatrix[1][j - 1] + cins
			backmatrix[1][j] = '-'

		# compute the recurrence equations and get full distance matrix and backtrack matrix
		for i in range(2, lengthofS + 2):
			for j in range(2, lengthofT + 2):
				vertical = distmatrix[i - 1][j] + cdel
				horizontal = distmatrix[i][j - 1] + cins
				if S[i - 2] == T[j - 2]:
					diagonal = distmatrix[i - 1][j - 1]
				else:
					diagonal = distmatrix[i - 1][j - 1] + csub

				mindist = min(diagonal, vertical, horizontal)
				distmatrix[i][j] = mindist

				# get the backtrack matrix
				if mindist == diagonal:
					backmatrix[i][j] = '\\'
				elif mindist == vertical:
					backmatrix[i][j] = '|'
				else: 
					backmatrix[i][j] = '-'
		
		# create the alignment
		ss = ""
		tt = ""
		mark = ""

		i = lengthofS + 1
		j = lengthofT + 1
		while not(i == 1  and j == 1):
			c = backmatrix[i][j]
			if c == '|':
				ss += S[i - 2] + ' '
				tt += '-' + ' '
				mark += ' ' + ' '
				i = i - 1
			elif c == '\\':
				ss += S[i - 2] + ' '
				tt += T[j - 2] + ' '
				if S[i - 2] == T[j - 2]:
					mark += '|' + ' '
				else:
					mark += ' ' + ' '
				i = i - 1
				j = j - 1
			else:
				ss += '-' + ' '
				tt += T[j - 2] + ' '
				mark += ' ' + ' '
				j = j - 1

		editdist = distmatrix[lengthofS + 1][lengthofT + 1]	

#################################################################### display results ####################
		self.results.insert(END, 'Final edit distance value: ' + str(editdist))
		self.results.insert(END, '\n')

		# codes for show matrices properly using format()
		n = 0
		m = max(lengthofT, lengthofS)
		while(m != 0):
			m = m / 10
			n += 1

		# display Full edit distance matrix
		if self.check_fdist.get():
			self.results.insert(END, 'Full edit distance matrix: ' + '\n')
			a = '{0:<' + str(n + 2) + '}'
			for i in range(0, lengthofS + 2):
				for j in range(0, lengthofT + 2):
					self.results.insert(END, a.format(str(distmatrix[i][j])))
				self.results.insert(END, '\n')
		
		# display Backtrack matrix
		if self.check_btrack.get():
			self.results.insert(END, 'Backtrack matrix: ' + '\n')
			for i in range(0, lengthofS + 2):
				for j in range(0, lengthofT + 2):
					self.results.insert(END, '{0: <5}'.format(str(backmatrix[i][j])))
				self.results.insert(END, '\n')
		self.results.insert(END, '\n')

		# display alignment
		if self.check_align.get():
			self.results.insert(END, 'The alignment: ' + '\n')
			self.results.insert(END, ss[::-1] + '\n')
			self.results.insert(END, mark[::-1] + '\n')
			self.results.insert(END, tt[::-1])
		self.results.insert(END, '\n')
		self.results.insert(END, '\n')

#################################################################### main part #########################
root = Tk()
root.title("String edit distance")
app = Application(root)
root.mainloop()
