# Use Cases

### 1. User enters a russian noun in Cyrillic or Latin characters as input and the app generates database entries for each morphological form. 
Input: "работа" or "rabota" 

Output: 

'робота successfully entered into the database.'

| worker       | Nominative | Accusative | Genitive | Prepositional | Dative | Instrumental |
|--------------|------------|------------|----------|---------------|--------|--------------|
| **Singular** | работа     | работу     | роботы   | роботе        | роботе | роботами     |
| **Plural**   | роботы     | роботах    | роботе   | роботам       | роботами| роботах      |


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

### 3. Users can use flashcards randomly generated from database contents

Input: 

| use flashcards |
|----------------|

Output: *example using робота*

#### Flashcard for робота

| reveal |
|--------| 

*clicking the reveal button shows:* роботам

Case: Dative

Number: Plural

### 4. Users can refresh the database to delete all contents. 

This gives the users control over what nouns they wish to study with the flashcard function.