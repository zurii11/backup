import json
from pprint import pprint
import subprocess
import time

with open('json/followers.json', 'r') as f:
    followers = json.load(f)

command = """curl 'https://www.instagram.com/{username}/?__a=1' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0' -H 'Accept: */*' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'X-IG-App-ID: 936619743392459' -H 'X-IG-WWW-Claim: hmac.AR1bjuYncQwxupCakXLcn3NYilq91gMJke_bvRQCAQdsRiCe' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' -H 'Referer: https://www.instagram.com/shako331/' -H 'Cookie: ig_did=306048DC-0BB2-4A91-883D-E9E86A858E33; rur=FTW; csrftoken=O73wbIYUWBq7CpFd35GPmHpCQriRubux; mid=XjVG6gAEAAFJx5XcsLxMFHhbDmdr; fbm_124024574287414=base_domain=.instagram.com; fbsr_124024574287414=V15kyXFflkuD9Xsn5QuGILcSUZJvST8ZLJ7mzkH34d4.eyJ1c2VyX2lkIjoiMTAwMDAyMzUyNjcyMjgxIiwiY29kZSI6IkFRQTBRUWRBR0puNS1JRHk1RXc0clR2YU9OaUFPc2ZHakEyUTdBRm1HZnlSa1BjZEVBaVFUWGhxbFNDZEtJSGxITWlhdmRoazZaeXpnZkRmMzZwYnpqUHhZakpyWFk3aEV6NHN4LXFnSWVSZU1uOVk4MjZVM0s2Y0M5c3JlTkROamlGNFFaWFZRNlI3QVlyWkJ1VW4wOUozak5wck1vRThGU3p3WjVyMjhjbzJaSHFvRmtDbmszRkFRYUtuU0piR2p6dTBQNzNDTTJTZmJfTGxZNnVfMUFYMHIzQlhlcU1FNHRXNVJOR1lmbXA2WFM2ZlZhaXhwb1NBMHlRbGhTb2FJbXlYNnRzb21wZ0hZQkF2OEd0clUtd19qTVZRSm0yeHFvcGE0clBEUHNXdUE2TlQtVXVQUzdwaTVPS1pyNUN3dTBzIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQU9DeDVkc3FYbTNMcUQ4bHdsbUExYmlXYmxDUlJaQlFtT0VCaUxjT2NiVlluMnVXS1pCV0E1ZDZxY1ZETENBU2V4WkI2aE1vVFdITnRmblZKcWxWU0ZhcVc2d2MzQk5kMlVaQzlaQzVFam5mTVFqN2NsRVpBWENaQW9EckF1Y3ZobTRZZzJ4bTNRRndkSXdoVUhvb1hTMVpBNHdaQjhyMVVPU0tITVhUc1Z5RGRYcFB6ZUlZb1VHWVpEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE1ODA1NDk5NDl9; urlgen="{{\"46.49.62.43\": 16010}}:1ixrBh:D_sa5PyfKUlWIdAvZa-ey1Ewv0Q"; shbid=10178; shbts=1580549950.6313763; ds_user_id=6703477615; sessionid=6703477615%3APJIRDv20jiKM9A%3A28' -H 'TE: Trailers' > json/temp.json"""

index = 0
followers_filled = []
for user in followers:
    subprocess.run(command.format(username=user['username']), shell=True, capture_output=True)
    with open('json/temp.json', 'r') as f:
        data = json.load(f)
    user['followed'] = data['graphql']['user']['edge_followed_by']['count']
    user['posts'] = data['graphql']['user']['edge_owner_to_timeline_media']['count']
    user['pic'] = data['graphql']['user']['profile_pic_url']
    user['follows'] = data['graphql']['user']['edge_follow']['count']
    # add profile pic for gui

    followers_filled.append(user)

    print(f'Iteration {index}/{len(followers)}')
    time.sleep(5 if index % 10 != 0 else 20)
    index += 1

with open('json/followers_filled.csv', 'w') as f:
    f.write(f"Full Name, Username, Follows, Followed By, Posts, Profile Picture\n")
    for user in followers_filled:
        f.write(f"{user['full_name']},{user['username']},{user['follows']},{user['followed']},{user['posts']},{user['pic']}\n")

