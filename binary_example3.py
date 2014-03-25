letter_a = "A"
letters = []

print "uppercase:"
for i in range(26):
  idx = ord(letter_a)
  new_letter = chr(idx + i)
  letters.append(new_letter)
  print new_letter

print "\nlowercase:"
for letter in letters:
  idx = ord(letter)
  shifted = idx + 32
  new_letter = chr(shifted)
  print new_letter
