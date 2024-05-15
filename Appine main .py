print('                         AppyPine App')
print('                 Welcome to The Best Android App')
print( "Python Programming Tutorials..  let's  start with  Variables ")
print('name')
name = 35.5
print(name)
print(' a = 2309 b = 708')
a = 2309
b = 708
print(a+b)
print(a-b)

print ( 'N1 = Appine N_2 = CodeJury') 
N1 = 'Appine'
N_2 = 'CodeJury '
print(N1)
print(N1 + N_2)
print('')

print('    Boolean (true/false)')
print ('My_name = True ')
My_name = True
print(My_name)
print('')

print('Receive input')
name = input('What is your name? ')
print('Hello  ' + name) 
print('')

print('Welcome to  Lifesavers Health Care and  Hospital #by GSI TECH ')
print('')
print('    Healthcare | Checkup   | Scan |  Surgery & operations   | Childcare  |  Emergency services   | See a Doctor /Nurse')
print('   Quarantine   | Complaints  | Insurance  | Drugs & Medications ')
print('')
a = input(' Choose  Any option  above and press enter   ')
print('Loading ' + a + '   Page')
print('')
print('               HOSPITAL BIODATA FORM')
b = input('Please Input your names     First Name: ')
b1 = input('Middle name: ')
b2 = input('Last Name:  ')
Name1 = b + b1 + b2

s = input('Country/Nationality: ') 
s2 = input ('State: ') 
s3 = input('Local Government/County: ') 

adr1 = input('Address: ') 
adr2 = input('Street Number/Address: ')

dob1 = input('Date of birth:  ' )
dob2 = input('Month of Birth: ')
dob3 = input('Year of Birth: ')
print('')
cy = input('Current Year:  ')
int(dob1)
age = int(cy) - int(dob3)

if age <= 17:
	print(' Hello ')
	print( ' You are underage. please move to the Teens and Kids form page')
	
	print(' Welcome sir / ma')
	print(' You are an adult. Please proceed to the next Lab')

print('')
print('    Blood  Group:  ( A	B	AB	O 	(A+   B+  AB+  O+ )')
Bldg = input("What's  Your  Blood Group ")


print('')
print('    Genotype:  AA AS SS SA (unknown) ')
Gen1 = input(' Genotype :')

print('')
print('    Relationship Status ( Single  |	Married	|	Divorced |	Widow	|	Widower ')
R1 = input('Relationship status: ')


print('')
k1 = input(' Do you have Kids / A child / Adopted / Relative')
k2 = input('How Many Children  do you have?  ')
int(k2)

print('')
print(' Current Working Status:  ( Employed  |  Self Employed   |  Part Time  |  Studying / Schooling  |  Businessman /Woman  |  CEO |  Government Worker  |  Military / Paramilitary  Personel |  Not Working  | ')
wks = input('Work Status: ')


print('')
print(Name1 + ' Biodata ')
print(Name1)
print(s)
print(s2)
print(s3)
print('your address is: ' + adr1)
print(adr2)
print(dob1)
print(dob2)
print(dob3)
print('You are ' + str(age))
print(Bldg + ' is your  blood group. ')
print(Gen1 + ' Is your  Genotype. ')
print(Name1 + ' is ' + R1)
print('Work Status: ' + wks)
print('')
print('            Lifesavers Healthcare Center')
print('                   GSI TECHNOLOGIES  ')