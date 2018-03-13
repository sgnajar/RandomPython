#   Author: Sasan Najar
#   Email: sasangnajar@gmail.com

#   This code is written to:
#       STEP #1 create the news ticker by adding headlines from the headlines list ### This news ticker designed to have exactly 80 characters long.
#       STEP #2 Insert a space in between each headline.

headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

newsTicker = ""
# newsTicker set to a string that contains no more than 80 characters long.
for headline in headlines:
    newsTicker += headline + " "
    if len(newsTicker) >= 80:
        newsTicker = newsTicker[:80]
        break