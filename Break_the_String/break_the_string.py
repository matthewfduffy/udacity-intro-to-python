"""
    Write a loop with a break statement to create a string, *news_ticker*, that is exactly 140 characters long. You should create the news ticker by adding headlines from the *headlines* list, inserting a space in between each headline. If necessary, truncate the last headline in the middle so that news_ticker is exactly 140 characters long.
"""
# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
# write your loop here
news_ticker_length = 0
for headline in headlines:
    if len(headline) + news_ticker_length >= 140:
        cutoff_char_count = news_ticker_length - len(headline)
        short_headline = headline[0:cutoff_char_count]
        news_ticker = news_ticker + " " + short_headline
        break
    else:



print(news_ticker)