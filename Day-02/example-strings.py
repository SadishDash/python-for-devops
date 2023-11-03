first_name = 'Sadish And'
last_name = 'Dash'

def full_name(first, last):
    fullName = first + " " + last
    return fullName

print(full_name(first_name,last_name).replace('Dash','Richa').split('And')[1].strip())
print(full_name(first_name,last_name).replace('Dash','Richa').strip('S'))


#Replace -> Replaces A string with a different string // str.replace ('a','b')
#split -> Splits the string based on the spliting condition // str.split('And')
#strip -> Removes the character/string from the start and end of a string based on the parameter //  str.strip()