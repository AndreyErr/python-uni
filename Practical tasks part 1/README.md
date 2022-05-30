# Practikal tasks part 1
---
All sorts of tasks from the university are collected here
---
__Description:__

- [File: Math1](#math1)

- [File: Math2](#math2)

- [File: Math3](#math3)

- [File: Math4](#math4)

- [File: Math5](#math5)

- [File: Math6](#math6)

- [File: Math7](#math7)

- [File: Math8](#math8)

- [Folder: Data_parsing](#Data_parsing)

- [Folder: Error_Handling](#Error_Handling)

- [Folder: To_base](#To_base)

---
### <a name="math1">File: Math1</a>
__Task:__

Solve this example:

![example](https://github.com/AndreyErr/python-uni/blob/main/Practical%20tasks%20part%201/img/t1.png)

Examples of calculation results:  
main(-0.45) = 8.38e+01  
main(0.79) = -1.35e+02  
main(-0.4) = 1.95e+02  
main(0.09) = -7.17e+06  
main(0.13) = -5.44e+05  

---
### <a name="math2">File: Math2</a>
__Task:__

Solve this example:

![example](https://github.com/AndreyErr/python-uni/blob/main/Practical%20tasks%20part%201/img/t2.png)

Examples of calculation results:  
f([-0.07, -0.93]) = 1.53e+00  
f([-0.13, 0.61]) = 5.18e-01  
f([0.46, -0.87]) = 3.80e+01  
f([-0.0, 0.96]) = 3.28e+00  
f([0.87, 0.45]) = 1.62e+02  

---
### <a name="math3">File: Math3</a>
__Task:__

Implement a function to compute a decision tree:  

![example](https://github.com/AndreyErr/python-uni/blob/main/Practical%20tasks%20part%201/img/t3.png)

Examples of calculation results:  
main(['NESC', 1982, 1961, 'LEAN', 2006]) = 12  
main(['NESC', 1981, 1961, 'LEAN', 1989]) = 5  
main(['ALLOY', 2000, 1961, 'HLSL', 2006]) = 11  
main(['ALLOY', 1981, 1962, 'MUF', 1989]) = 9  
main(['ALLOY', 1981, 1993, 'HLSL', 1989]) = 6  

---
### <a name="math4">File: Math4</a>
__Task:__

Implement a function for converting bit fields.  
The solution must use bitwise operations.  
Input format:  

![example](https://github.com/AndreyErr/python-uni/blob/main/Practical%20tasks%20part%201/img/t4_1.png)

Output format:  

![example](https://github.com/AndreyErr/python-uni/blob/main/Practical%20tasks%20part%201/img/t4_2.png)

Examples of calculation results:  
f(0x44e12479) = 0xf3c12508  
f(0xd507771b) = 0x360f6d6e  

---
### <a name="math5">File: Math5</a>
__Task:__

Implement a function to parse a string containing data in text format. Explore the details of the format using the examples below. Return the result as a dictionary.  
  
Example  
Input string:  
<sect> <% store 'usried_920'is list( q(dimaza_172) q(maanen_298))  
%>;<% store 'ladies' is list( q(edis) q(erorer_471) q(inma_662)  
q(edatar_811)) %>; </sect>  
  
Disassembled result:  
{'usried_920': ['dimaza_172', 'maanen_298'],  
 'ladies': ['edis', 'erorer_471', 'inma_662', 'edatar_811']}  

---
### <a name="math6">File: Math6</a>
__Task:__

Implement a Mile finite automaton as a class. The initial state of the automaton is A. Methods return numeric values. If the called method is not implemented for some state, a KeyError exception must be thrown.  

![example](https://github.com/AndreyErr/python-uni/blob/main/Practical%20tasks%20part%201/img/t6.png)

In the examples below, the main function returns an object of the created class. Then the methods of the received object are called sequentially.  
  
Example 1  
o = main()  
o.crawl() # 1  
o.close() # 0  
o.exit() # 4  
o.exit() # 6  
o.close() # 7  
o.close() # 8  
  
Example 2  
o = main()  
o.crawl() # 1  
o.crawl() # 1  
o.close() # 0  
o.crawl() # KeyError  
o.exit() # 4  
o.exit() # 6  
o.crawl() # KeyError  
o.close() # 7  
o.exit() # KeyError  
o.close() # 8  

---
### <a name="math7">File: Math7</a>
__Task:__

Implement the tabular data conversion function. The input and output tables are set in line-by-line form, using lists. The filled cells have a string data type. Empty cells have the value None.  
When converting numbers, the round() function is first used to round to the desired number of decimal places.  
Perform a number of transformations on the input table:  
- Remove duplicates among columns, leaving only the first driving of the duplicate column into the table.  
- Delete duplicates among rows, leaving only the first driving of the duplicate row to the table.  
- Delete empty lines.  
- Split one of the columns by the separator “;”.  
- Convert the contents of cells by examples.  
Examples of tabular transformations:  
Source table:  

![example](https://github.com/AndreyErr/python-uni/blob/main/Practical%20tasks%20part%201/img/t7_1.png)

Conversion result:  

![example](https://github.com/AndreyErr/python-uni/blob/main/Practical%20tasks%20part%201/img/t7_2.png)

---
### <a name="math8">File: Math8</a>
__Task:__

Implement binary data format parsing. The data starts with the signature 0xcf 0x46 0x52 0x42 0x4b, followed by the structure A. Byte order: from lowest to highest. Addresses are indicated as offsets from the beginning of the data. The solution suggests using the struct module.

Structure A:

![example](https://github.com/AndreyErr/python-uni/blob/main/Practical%20tasks%20part%201/img/t8_1.png)

Structure B:

![example](https://github.com/AndreyErr/python-uni/blob/main/Practical%20tasks%20part%201/img/t8_2.png)

Structure C:

![example](https://github.com/AndreyErr/python-uni/blob/main/Practical%20tasks%20part%201/img/t8_3.png)

Structure D:

![example](https://github.com/AndreyErr/python-uni/blob/main/Practical%20tasks%20part%201/img/t8_4.png)
  
Example  
Binary data:  
(b'\xcfFRBKkvhqrrgY\x00\x00\x00x\x00\x00\x000COi\xe7#\xcb?!\x9d\x14\x1a3P\x05N'  
 b'\x92\xfa\xe5\\U\xb6H\xd3V<\xda\\(\x82\x8b\xd5\xc0\x7fS\xd3?\xa0\x88\xef'  
 b'\xde)2\xd9\xe1\x0e\x0e\x02\x00\x1d\x00\x00\x001\x12\x03\x00%\x00\x00'  
 b'\x00`\xdd\x04\x001\x00\x00\x00\x87\xe4\x03\x00\x00\x00A\x00Y\x00\x04'  
 b'\x7f\xc8o\xab\xf2\xaf\x99(gS\xac\xa5y:\xed}z\x08K\xee\x82\xdbH\xfc\xd4\xcddc'  
 b'\xef`\xe4\xbf')  
  
 The result of the analysis:  
 {'A1': 'kvhqrrg',  
 'A2': {'B1': -7033,  
        'B2': [{'C1': 3598, 'C2': [857347229, -1840380592]},  
               {'C1': 4657, 'C2': [1432151546, 1456687286, 677173820]},  
               {'C1': -8864,  
                'C2': [-1059746942, 1070814079, -554727264, -505859543]}],  
        'B3': 17486192885111193689,  
        'B4': [175, 153],  
        'B5': 26408,  
        'B6': [83, -84, -91],  
        'B7': 17170827326471879289},  
 'A3': {'D1': -62334078, 'D2': -0.6368328992161261},  
 'A4': 0.21203320161887396,  
 'A5': 33}  
  
---
### <a name="Data_parsing">Folder: Data_parsing</a>

__Task:__
Analyze the database of old computer games.  
Use graphs to answer the following questions:  
What were the most popular years in terms of the release of games?  
What genres were popular in different periods of time?  

__Final output graphs:__

[years](https://github.com/AndreyErr/python-uni/blob/1e4b6fcbfe6d7029a7a9d2e6c73b3b421dbbb72a/Practical%20tasks%20part%201/Data_parsing/years.png)

[distribution_of_genres_by_year](https://github.com/AndreyErr/python-uni/blob/1e4b6fcbfe6d7029a7a9d2e6c73b3b421dbbb72a/Practical%20tasks%20part%201/Data_parsing/distribution_of_genres_by_year.png)


---
### <a name="Error_Handling">Folder: Error_Handling</a>

__Task:__
Write a function that adds information about the exception that has occurred (class, message, trace) to the log file. The function should not handle exceptions. The input of the function that needs to be developed receives a link to the user function being performed:

`def run_with_log(func):`

__Final output log:__

[log file](https://github.com/AndreyErr/python-uni/blob/main/Practical%20tasks%20part%201/Error_Handling/log.log)

---
### <a name="To_base">Folder: To_base</a>

__Task:__
Using the doctest module

- Add the documentation to the program as a docstring string.
- Specify examples in doctest format. Examples should cover boundary cases.
- Test the program by calling the doctest module.
- Transfer the examples to a separate file and test the program again.