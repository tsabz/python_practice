# key value pairs. in relation to dictionary is 
# a key is the word and the pair is the defition of the word


monthConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}


print(monthConversion["Dec"])
print(monthConversion.get("Dec"))
print(monthConversion.get("De", "Not a valid key")) #not a valid key