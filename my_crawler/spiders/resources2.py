import pandas as pd
import re
from tqdm import tqdm
from ecommercetools import seo
import time

# query_list = ['denmark, inflation', 'denmark, immigration', 'denmark, global warming', 'toronto, inflation',
#               'toronto, immigration', 'toronto global warming', 'washington, inflation',
#               'washington, immigration', 'washington, global warming', 'madrid, inflation', 'madrid immigration',
#               'madrid, global warming', 'paris, inflation', 'paris, immigration', 'paris, global warming',
#               'sweden, inflation', 'sweden, immigration', 'sweden, global warming']

query_list = ['machine learning pdf', 'Distributed systems pdf', 'Computer Security pdf']
# query_list = ['artificial intelligence pdf']

targets = []
for query in tqdm(query_list):
    pages_num = 3
    # conditions = ['wikipedia', 'twitter', 'linkedin', 'Facebook', 'news']
    conditions = ['videos', 'pdf']
    # conditions = ['']
    #use [''] to get all google search results
    try:
        res = seo.get_serps(query, pages=pages_num)
    except:
        continue
    for c in conditions:
        temp1 = res[res['link'].str.contains(c, case=False)]['title'].to_list()
        temp2 = res[res['link'].str.contains(c, case=False)]['link'].to_list()
        if len(temp1) == 0:
            y = ''
        else:
            y = temp1[0]
        if len(temp2) == 0:
            z = ''
        else:
            z = temp2[0]
        targets.append([y, z, c, query])
        time.sleep(25)
    time.sleep(20)

targets = pd.DataFrame(targets, columns=['title', 'link', 'link category', 'query keyword used'])
print(targets)