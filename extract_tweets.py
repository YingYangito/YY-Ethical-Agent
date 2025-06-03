import json

# Change to your own path if needed
tweets_file = 'tweets.js'
output_file = 'my_tweets.txt'

with open(tweets_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Remove the JS variable assignment (usually the first line)
json_str = ''.join(lines)
json_str = json_str[json_str.index('['):]  # Find the first '['

# Parse as JSON
tweets_data = json.loads(json_str)

# Extract tweets
all_tweets = []
for entry in tweets_data:
    tweet = entry.get('tweet', {})
    text = tweet.get('full_text') or tweet.get('text')  # Some have 'text', some 'full_text'
    if text:
        all_tweets.append(text.replace('\n', ' '))  # Remove newlines in tweets

# Write to plain text file, one tweet per line
with open(output_file, 'w', encoding='utf-8') as out:
    for tweet in all_tweets:
        out.write(tweet + '\n')

print(f'Extracted {len(all_tweets)} tweets to {output_file}')
