# Python-GUI-Sample
Python GUI Programming: STRING EDIT DISTANCE   Qi Chen   10/16/2014
———————————————————————————————————————————————
Zip file information
----------
After extracting the zip file, you file get 4 files in the main file. - GUI.py: this is the source file for the implementation of the program.
- README.pdf: this is read me file which shows you more information about the program.
- Snapshots of test.pdf: it shows some snapshots of my program in action with some comments. The output format might be a little different from the ones in this file because I changed the format a little bit.
- testfile: this file includes two text files, each of them contains a string. They are used to test whether the program goes well.

Execute the program
----------
I executed my program in the terminal in the OS X, so after changing the directory to where the program is, then type in “python GUI.py” to run the program. A window will show up on the screen. You can just try any strings, cost values, check which output you want, then click “Compare”. And you can use "Clear" button to clear the result window.

Notes: 1.for text files, please make sure that there is ONLY one string for each file. Otherwise, the program will read ‘\n’ for new lines and shows results weird and incorrect. If you want to make your test files to test the program in the sunlab, please be careful that the text file you create. I tried and found that although the results are right, it still shows something weird and improperly. Or you can just change the contents in my test files to test. 2.The sliders for costs sometimes are not easy to control, then you can click on the grey spot in the slider to change numbers slightly.

Take the example from the assignment, S = compare, T = computer, cdel = 1, cins = 1, csub = 2. The results you will get is
Final edit distance value: 5
Full edit distance matrix: 
      c  o  m  p  u  t  e  r  
   0  1  2  3  4  5  6  7  8  
c  1  0  1  2  3  4  5  6  7  
o  2  1  0  1  2  3  4  5  6  
m  3  2  1  0  1  2  3  4  5  
p  4  3  2  1  0  1  2  3  4  
a  5  4  3  2  1  2  3  4  5  
r  6  5  4  3  2  3  4  5  4  
e  7  6  5  4  3  4  5  4  5  
Backtrack matrix: 
          c    o    m    p    u    t    e    r    
     0    -    -    -    -    -    -    -    -    
c    |    \    -    -    -    -    -    -    -    
o    |    |    \    -    -    -    -    -    -    
m    |    |    |    \    -    -    -    -    -    
p    |    |    |    |    \    -    -    -    -    
a    |    |    |    |    |    \    \    \    \    
r    |    |    |    |    |    \    \    \    \    
e    |    |    |    |    |    \    \    \    |    

The alignment: 
 c o m p - - a r e
 | | | |       |  
 c o m p u t e r -

Explanation for the program 
----------
The program is divided in three main parts.

The first part is to create widgets part after creating the GUI application. In this part, it creates fancy user interface using
widgets. One thing needs to mention is that for the text box, I create a x- and y-scrollbar.The x-scrollbar is used to make the output matrices look nice. When you have a T string with long width, you can just scroll the x-scrollbar at the bottom of the text bow to right hand side to see the whole results. Here, I add a clear button for users to clear the results window.

The next part is computation part which is used to compute edit distance. The results always include the final distance value as
assigned. By checking whether the checkbooks are checked, the output will show what you want to see. Using the algorithm learned from https://web.stanford.edu/class/cs124/ lec/med.pdf, the distance computation part is straightforward and gets final distance. While distance computation, the program creates backtrack matrices at the same time. Then according to the backtrack
matrices, we get the alignments.

I add one enhancement to let the string inputs accept file names. To make this enhancement, this part program should check whether the input string is string or a file name. If it is a file name, you need to check the checkbox to make the system know. Then program will try to open the file. If the file can open, then the program will get the string and compute it. If the file cannot be open or actually it is not a file, the program will take whatever you type as strings and you will see warnings from the text box and the results of what you type. When you type in a real file name, but you forget to check the check box, it will take them as normal strings instead of file names. In the each text file, there should be only one string. 

The last main part is to display results. To print the full edit distance matrices properly, I try to get the length of strings to make the print width well. Others are obvious.
