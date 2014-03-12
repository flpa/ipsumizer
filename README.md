# Lorem Ipsumizer
_Turns your essay into placeholder text in the blink of an eye._

## Description ##

Lorem Ipsumizer 'obfuscates' alpha-characters in input text read from stdin by iterating through the alpha characters in a Lorem Ipsum sample text, while preserving tha case.

## Example ##

**Input (sample.txt)**
    
    Your tasks:
	- Analysis of secret projects
	- Writing documents about secret projects

	Required knowledge:
	• Basic algorithms 
	• Advanced level jQuery, JavaScript (ExtJS), AJAX, HTML, XML
	• Vim and Emacs
	• English

**Invocation**

	$ cat sample.txt | ./lorem-ipsumizer.py 

**Output**

	Lore mipsu:
	- Mdolorsi ta metcon sectetur
	- Adipisi cingelits eddoe iusmod temporin

	Cididunt utlaboree:
    • Tdolo remagnaali 
	• Quauteni madmi nImven, IamqUisnos (TruDE), XERC, ITAT, ION
	• Ull amc Olabo
	• Risnisi
