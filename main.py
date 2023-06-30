# Dapatkan html dengan python

import requests as re

response = re.get ('https://elforest.se/news.php?lang=en&id=1607088350')
html = response.text

print(html) 