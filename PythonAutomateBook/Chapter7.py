#111-111-1111

# def isPhoneNumber(number):
#     if len(number) != 12:
#         print('is not number')
#         return False
#     list = str(number).split('-')
#     if not list[0].isdecimal() or not list[1].isdecimal() or not list[2].isdecimal():
#         print('is not number')
#         return False
    

#     if len(list[0])==3 and len(list[1])==3  and len(list[2]) ==4:
#         print('is number')
#         return True
#     print('is not number')
#     return False    
        
# number = input()
# isPhoneNumber(number)

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('my num is 122-122-2222')
print(mo.group())

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

mo.group(1)
#122
mo.group(2)
#122-2222
mo.group(0)
#122-122-2222
mo.group()
#122-122-2222

mo.groups()
#('122', '122-2222')

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')

mo.group(1)
#(122)

mo.group(2)
#122-2222


heroRegex = re.compile(r'shuten | douji')
mo1 = heroRegex.search('shuten and douji')
mo1.group()
#shuten

mo2 = heroRegex.search('douji and shuten')
mo2.group()
#douji

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
mo.group()
#Batmobile

mo.group(1)
#mobile

batRegex = re.compile(r'Bat(wom)?man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()
# 'Batman'

mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()
# 'Batwoman'

batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()
# 'Batman'

mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()
# 'Batwoman'

mo3 = batRegex.search('The Adventures of Batwowowowoman')
mo3.group()
# 'Batwowowowoman'

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
mo1.group()
# 'Batwoman'

mo2 = batRegex.search('The Adventures of Batwowowowoman')
mo2.group()
# 'Batwowowowoman'

mo3 = batRegex.search('The Adventures of Batman')
mo3 == None
# True

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
mo1.group()
# 'HaHaHa'

mo2 = haRegex.search('Ha')
mo2 == None
# True

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
mo1.group()
# 'HaHaHaHaHa'

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
mo2.group()
# 'HaHaHa'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
mo.group()
'415-555-9999'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
['415-555-9999', '212-555-0000']

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
[('415', '555', '9999'), ('212', '555', '0000')]

# \d Any numeric digit from 0 to 9.

# \D Any character that is not a numeric digit from 0 to 9.

# \w Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)

# \W Any character that is not a letter, numeric digit, or the underscore character.

# \s Any space, tab, or newline character. (Think of this as matching “space” characters.)

# \S Any character that is not a space, tab, or newline.

xmasRegex = re.compile(r'\d+\s\w+')
xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']

#matching every character that is a vowel
vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']

#matching every character that is not a vowel
consonantRegex = re.compile(r'[^aeiouAEIOU]')
consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
['R', 'b', 'C', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', '', 'B', 'B', 'Y', ' ', 'F', 'D', '.']

beginsWithHello = re.compile(r'^Hello')
beginsWithHello.search('Hello, world!')
# <re.Match object; span=(0, 5), match='Hello'>
beginsWithHello.search('He said hello.') == None
# True

endsWithNumber = re.compile(r'\d$')
endsWithNumber.search('Your number is 42')
# <re.Match object; span=(16, 17), match='2'>
endsWithNumber.search('Your number is forty two.') == None
True

wholeStringIsNum = re.compile(r'^\d+$')
wholeStringIsNum.search('1234567890')
#<re.Match object; span=(0, 10), match='1234567890'>
wholeStringIsNum.search('12345xyz67890') == None
True
wholeStringIsNum.search('12  34567890') == None
True

atRegex = re.compile(r'.at')
atRegex.findall('The cat in the hat sat on the flat mat.')
['cat', 'hat', 'sat', 'lat', 'mat']

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
mo.group(1)
'Al'
mo.group(2)
'Sweigart'

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
mo.group()
'<To serve man>'

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
mo.group()
'<To serve man> for dinner.>'

noNewlineRegex = re.compile('.*')
noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
'Serve the public trust.'


newlineRegex = re.compile('.*', re.DOTALL)
newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
'Serve the public trust.\nProtect the innocent.\nUphold the law.'

#ignore case sensitive
robocop = re.compile(r'robocop', re.I)
robocop.search('RoboCop is part man, part machine, all cop.').group()
'RoboCop'

robocop.search('ROBOCOP protects the innocent.').group()
'ROBOCOP'

robocop.search('Al, why does your programming book talk about robocop so much?').group()
'robocop'

namesRegex = re.compile(r'Agent \w+')
namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
'CENSORED gave the secret documents to CENSORED.'

agentNamesRegex = re.compile(r'Agent (\w)\w*')
agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that AgentEve knew Agent Bob was a double agent.')
# A**** told C**** that E**** knew B**** was a double agent.'

phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)

# using ignorecase, re.dotall, and re.verbose
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
