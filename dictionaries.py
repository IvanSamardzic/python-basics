Jan -> January
Mar -> March

#give the name to dictionary
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July";
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"Novermber",
    "Dec":"December",
}

#give the 3char month name as a paramter and get the full month name
print(monthConversions["Nov"])
print(monthConversions["Mar"])
print(monthConversions.get("Sep"))

#pass the default value
print(monthConversions.get("Sep", "Invalid key"))

