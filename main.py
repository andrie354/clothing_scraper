import requests
import pandas as pd
import time

url = "https://sea.newchic.com/api/collection/ajax_ranklist"

res = []

for x in range(1,2):
    querystring = {"filter_value":"","pagesize":"100","page":f"{x}","default_rule_country_cdn":"100","currency_cdn":"IDR","cdn_lang":"en","conversionType":"ASIA","color_id":"","size":"","brand_id":"","sort":"","ship":"","act":"","position_id":"","newarrivals":"","favorite":"","is_logo":"","id":"3372"}

    headers = {
        "cookie": "newchic_SID=776a519eeef133640703cdcf47db951f; _bgLang=en-GB; currency=IDR; default_rule_country=100; default_rule_warehouse=100%257CCZ%257CCN; system_microtime=1636255969997; generalAbTest=37; _abtest=1; nc-country-code=ID",
        "authority": "sea.newchic.com",
        "pragma": "no-cache",
        "cache-control": "no-cache",
        "sec-ch-ua": "^\^Google"
    }

    r = requests.request("GET", url, headers=headers, params=querystring)

    data = r.json()
    for product in data['result']['list']:
        res.append(product)
        print('results found : ', len(res))
        time.sleep(3)


df = pd.json_normalize(res)
df.to_csv('results.csv')

