# Use Cases
I have three working uses cases with plans to add more to support verb parsing and conjugating
### 1. User enters a russian noun in Cyrillic or Latin characters as input and the app returns parse information (person, number, gender, case, declension) and translation. 
Input: "работу" or "rabotu" 

Output: 'работу: worker/laborer, accusative, feminine, singular, first'

### 2. The app returns the Cyrillic text from Latin transliteration input from the following key:

a: а
b: б
v: в
g: г
d: д
ye: е
yo: ё
zh: ж
z: з
i: и
yi: й
k: к
l: л
m: м
n: н
o: о
p: п
r: р
s: с
t: т
u: у
f: ф
x: х
ts: ц
ch: ч
sh: ш
shh: щ
jj: ы
e: э
yu: ю
ya: я
j: ь

Input: "privyet rabotnik"
Output: "привет работник"

### 3. Takes user russian noun input and returns all forms for that noun