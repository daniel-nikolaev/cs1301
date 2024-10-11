flips = "HHTTHTHHTTHHTHTHTHHTTHH"

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#The string above gives the results of a series of coin flips,
#H for heads and T for tails.
#
#Count the number of heads and number of tails. Then, print
#a message like this one based on the results:
#
#13 heads, 10 tails. Heads wins.
#
#Replace 13 and 10 with the actual numbers of heads and tails.
#Replace 'Heads wins.' with 'Tails wins.' ift there are more
#tails, or with 'It's a tie.' if there are the same number of
#heads and tails.
#
#For example:
#
# "HHTTHH" -> 4 heads, 2 tails. Heads wins.
# "THTHTT" -> 2 heads, 4 tails. Tails wins.
# "TTHHHT" -> 3 heads, 3 tails. It's a tie.


#Add your code here!
heads = 0
tails = 0

for char in range(len(flips)):
    if flips[char] == "H":
        heads += 1
    else:
        tails += 1
if heads > tails:
    print(str(heads), "heads," , str(tails) , "tails. Heads wins.")
elif heads < tails:
    print(str(heads), "heads," , str(tails) , "tails. Tails wins.")
else:
    print(str(heads), "heads," , str(tails) , "tails. It's a tie.")