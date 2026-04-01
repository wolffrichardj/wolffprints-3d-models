from googlesearch import search

query = 'site:makerworld.com/en/models "mini banana buddy"'
print("Testing google search:")
try:
    for j in search(query, num_results=2, advanced=True):
        print(j.url, j.description)
except Exception as e:
    print(e)
