from random import randint

#not efficient obviously

#>help/utils methods

#input decimal char array tuples, lists, whatever, and then it joins in a big string(must contain decimal ascii items)
def genCharSet(sets):
  return ''.join([chr(d) for set in sets for d in set])

#convert base decimal to charset and positions
def based(index, length, charSet):
    base = len(charSet)
    digits = [0] * length
    pos = length - 1
    while pos >= 0:
        digits[pos] = index % base
        index = index // base
        pos -= 1
    word = [""] * length
    i = 0
    while i < length:
        word[i] = charSet[digits[i]]
        i += 1
    return "".join(word), digits

#>main methods

#random onion v3 address generator
#v3 specifications:
#56 chars length(last one reserved, always ends with "d")
#so 55 random chars length
#a-z and 2-7 (32 characters)
#lowercase only
#in ascii decimal, a-z(97, 122+1(for loop)), 2-7(50, 55+1)
def randv3onion(begin="http://", end=".onion", lastChar='d', charSet=genCharSet([range(97,122+1), range(50, 55+1)]), length=55):
  return begin+''.join([charSet[randint(0,len(charSet)-1)] for d in range(length)])+lastChar+end

#split "d.onion" then split "//" if it has any
#checks length
#checks valid chars
def isValidV3Address(address):
  s=address.split("d.onion")[0]
  if '//' in s:
    s=s.split('//')[1]
  if len(s)!=55:
    return False
  for c in s:
    d=ord(c)
    if (not (d>=97 and d<=122)) and (not (d>=50 and d<=55)):
      return False
  return True

#address list generator
#not all valid since the valid addresses have hashes and keys,
#but probably some addresses are valid, though it's practically impossible to find them this way.
#generates from a numeric representation, following the specific character set a-z/2-7
#32**55 = 32⁵⁵ = 60708402882054033466233184588234965832575213720379360039119137804340758912662765568
def generate(start=0, end=100, output=print, length=55, charSet=genCharSet([range(97,122+1), range(50, 55+1)])):
    #charset = "abcdefghijklmnopqrstuvwxyz234567"
    base = len(charSet)
    word, digits = based(start, length, charSet)
    index = start
    while index < end:
        output(word) #customize your output method(it's a stream, doesn't make sense to store and return a array)
        pos = length - 1
        while pos >= 0:
            digits[pos] += 1
            if digits[pos] < base:
                break
            digits[pos] = 0
            pos -= 1
        if pos < 0:
            return
        word = list(word)
        word[pos] = charSet[digits[pos]]
        i = pos + 1
        while i < length:
            word[i] = charSet[digits[i]]
            i += 1
        word = "".join(word)
        index += 1

#If you wish to store in an array:
# addresses=[]
# generate(0,10,addresses.append)


#>testing
print(genCharSet([range(97,123), range(50,56)]))
print(based(0,55,"abcdefghijklmnopqrstuvwxyz234567"))
print(randv3onion("https://"))
print(isValidV3Address(randv3onion()))
generate(0,3)

# fyi this ins't viable, these addresses are totally randomic, hardly you will find any useful
# even if you try to request brute-force it would take billions of years to finish all addresses
# if ya wanna know how they generate custom addresses search the term in TODO comment below
# TODO> add "vanity address generation method"