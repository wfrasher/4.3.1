# put $1000 in bank and get 3% interest anually  

# use while loop to determine how long it will take for the account to have at least $1200



account = 0
year = 0
while account <= 1200:
    account = account + 1000 + (account * .03)
    year += 1

print("$" + str(account) + "   " + "Years: " + str(year)) 
