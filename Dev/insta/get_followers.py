import subprocess
import time
import json
import urllib.parse


url_base = 'https://www.instagram.com/graphql/query/?'

command = """curl '{url}' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0' -H 'Accept: */*' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'X-CSRFToken: O73wbIYUWBq7CpFd35GPmHpCQriRubux' -H 'X-IG-App-ID: 936619743392459' -H 'X-IG-WWW-Claim: hmac.AR1bjuYncQwxupCakXLcn3NYilq91gMJke_bvRQCAQdsRtoV' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' -H 'Referer: https://www.instagram.com/kesane.b/followers/' -H 'Cookie: ig_did=306048DC-0BB2-4A91-883D-E9E86A858E33; csrftoken=O73wbIYUWBq7CpFd35GPmHpCQriRubux; mid=XjVG6gAEAAFJx5XcsLxMFHhbDmdr; fbm_124024574287414=base_domain=.instagram.com; shbid=10178; shbts=1581512653.37708; ds_user_id=6703477615; sessionid=6703477615%3APJIRDv20jiKM9A%3A28; fbsr_124024574287414=V15kyXFflkuD9Xsn5QuGILcSUZJvST8ZLJ7mzkH34d4.eyJ1c2VyX2lkIjoiMTAwMDAyMzUyNjcyMjgxIiwiY29kZSI6IkFRQTBRUWRBR0puNS1JRHk1RXc0clR2YU9OaUFPc2ZHakEyUTdBRm1HZnlSa1BjZEVBaVFUWGhxbFNDZEtJSGxITWlhdmRoazZaeXpnZkRmMzZwYnpqUHhZakpyWFk3aEV6NHN4LXFnSWVSZU1uOVk4MjZVM0s2Y0M5c3JlTkROamlGNFFaWFZRNlI3QVlyWkJ1VW4wOUozak5wck1vRThGU3p3WjVyMjhjbzJaSHFvRmtDbmszRkFRYUtuU0piR2p6dTBQNzNDTTJTZmJfTGxZNnVfMUFYMHIzQlhlcU1FNHRXNVJOR1lmbXA2WFM2ZlZhaXhwb1NBMHlRbGhTb2FJbXlYNnRzb21wZ0hZQkF2OEd0clUtd19qTVZRSm0yeHFvcGE0clBEUHNXdUE2TlQtVXVQUzdwaTVPS1pyNUN3dTBzIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQU9DeDVkc3FYbTNMcUQ4bHdsbUExYmlXYmxDUlJaQlFtT0VCaUxjT2NiVlluMnVXS1pCV0E1ZDZxY1ZETENBU2V4WkI2aE1vVFdITnRmblZKcWxWU0ZhcVc2d2MzQk5kMlVaQzlaQzVFam5mTVFqN2NsRVpBWENaQW9EckF1Y3ZobTRZZzJ4bTNRRndkSXdoVUhvb1hTMVpBNHdaQjhyMVVPU0tITVhUc1Z5RGRYcFB6ZUlZb1VHWVpEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE1ODA1NDk5NDl9; rur=FTW; urlgen="{{\"46.49.62.43\": 16010\054 \"46.49.115.56\": 16010\054 \"94.43.141.80\": 35805\054 \"94.43.156.106\": 35805}}:1j2t9z:0Hyzg-494-2-9NP1wz-QLuDhSKQ"' -H 'TE: Trailers' > json/followers_{index}.json"""

index = 1
after = None
followers_sum = 0
while True:
    after_value = f',"after":"{after}"' if after else ''
    variables = f'{{"id":"1638200246","include_reel":true,"fetch_mutual":true,"first":50{after_value}}}'
    get_parameters = {
        'query_hash': 'c76146de99bb02f6415203be841dd25a',
        'variables': variables
    }
    ws_url = url_base + urllib.parse.urlencode(get_parameters)

    result = subprocess.run(command.format(url=ws_url, index=index), shell=True, capture_output=True)
    if result.returncode != 0:
        exit('Suicide')

    with open(f'json/followers_{index}.json', 'r') as f:
        data = json.load(f)

    if not data['data']['user']['edge_followed_by']['page_info']['has_next_page']:
        break

    after = data['data']['user']['edge_followed_by']['page_info']['end_cursor']
    all_followers = data['data']['user']['edge_followed_by']['count']
    current = len(data['data']['user']['edge_followed_by']['edges'])
    followers_sum += current
    print(f'{followers_sum}' + '/' + f'{all_followers}')

    time.sleep(5 if index % 10 != 0 else 20)
    index += 1

print('Done')