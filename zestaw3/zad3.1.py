x = 2 ; y = 3 ;
if (x > y):
    result = x;
else:
    result = y;

#poprawny

for i in "qwerty": if ord(i) < 100: print i

#jesli rozbijemy kod na linie bedzie dzialac. w tej formie jest niepoprawny

for i in "qwerty":
   if ord(i) < 100:
      print (i)

for i in "axby": print ord(i) if ord(i) < 100 else i

#niepoprawny. brak znakow konca linii i dwukropkow