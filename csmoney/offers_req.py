import requests

cookies = {
    "_gcl_au": "1.1.1364228153.1675618691",
    "utm_source": "google",
    "utm_medium": "cpc",
    "utm_campaign": "Search_Brand_UA_Desktop_Act",
    "utm_term": "cs%20money",
    "utm_content": "ads_adaptive",
    "sc": "D1059B1C-E62B-7BD7-2A02-C8F2870F2593",
    "_gid": "GA1.2.1700211239.1675618692",
    "_fbp": "fb.1.1675618691606.1141373986",
    "_scid": "00177fb3-9654-44fc-a638-4e28c846b5e6",
    "new_language": "ru",
    "_hjSessionUser_2848248": "eyJpZCI6IjU0MWI5MDQ0LTJhODUtNWE3OS1iZTZhLTUyODc3YmU3Y2RhOCIsImNyZWF0ZWQiOjE2NzU2MTg2OTE1ODQsImV4aXN0aW5nIjp0cnVlfQ==",
    "page_before_registration": "/ru/",
    "csgo_ses": "f2bb698d13e658d5ff860bfabf1190f9798899a8ff05d6548b15249b5bc69569",
    "steamid": "76561199042153366",
    "avatar": "https://avatars.akamai.steamstatic.com/f4e7432889c3773c1f585f0f5ccf488fec760a5b_medium.jpg",
    "username": "%E5%85%AB%E6%80%80%E5%85%AB%E6%9C%88%E5%88%9D%E5%85%AB",
    "support_token": "5ed32378b0e7fb4fea5db31d23b240025ff3968ce5e0c8ea9412733010c04bca",
    "registered_user": "true",
    "AB_TEST_CONCRETE_SKIN_1_ITERATION": "a",
    "_gcl_aw": "GCL.1675618707.EAIaIQobChMIzbHEhfb-_AIVrkaRBR1WWguZEAAYASAAEgL18PD_BwE",
    "GleamId": "nKZepxjJBgFaO9fwm",
    "GleamA": "%7B%22nKZep%22%3A%22login%22%7D",
    "onboarding__skin_quick_view": "false",
    "_gac_UA-77178353-1": "1.1675618796.EAIaIQobChMIzbHEhfb-_AIVrkaRBR1WWguZEAAYASAAEgL18PD_BwE",
    "_tt_enable_cookie": "1",
    "_ttp": "EzrC2l3Sw0rFbZdxaQCCdHT4svx",
    "_sctr": "1|1676152800000",
    "_hjHasCachedUserAttributes": "true",
    "isAnalyticEventsLimit": "true",
    "_dc_gtm_UA-77178353-1": "1",
    "_ga_HY7CCPCD7H": "GS1.1.1676329696.43.0.1676329696.60.0.0",
    "_ga": "GA1.1.485440045.1675618692",
    "_hjIncludedInSessionSample_2848248": "1",
    "_hjSession_2848248": "eyJpZCI6ImQ2YmIxNGE0LTM3MTktNDBjMi05N2FjLTBlMjFiYmM5MjY2OCIsImNyZWF0ZWQiOjE2NzYzMjk2OTYzMTksImluU2FtcGxlIjp0cnVlfQ==",
    "_hjIncludedInPageviewSample": "1",
    "_hjAbsoluteSessionInProgress": "0",
    "_hjUserAttributesHash": "b0cab6883fdd7eb32048d4d25bd33701",
    "_uetsid": "dc6bad90a57b11edaf50e5dbc6330abb",
    "_uetvid": "dc6bd140a57b11ed8d730dab9587bafa",
    "amplitude_id_c14fa5162b6e034d1c3b12854f3a26f5cs.money": "eyJkZXZpY2VJZCI6Ijg4NzdkODJmLTg4ZGYtNDhkZC1iMGRjLThmOTRmZmY1MzFjOFIiLCJ1c2VySWQiOiI3NjU2MTE5OTA0MjE1MzM2NiIsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTY3NjMyOTY5NjA3NCwibGFzdEV2ZW50VGltZSI6MTY3NjMyOTcwNTAxNSwiZXZlbnRJZCI6MjAzLCJpZGVudGlmeUlkIjozMjYsInNlcXVlbmNlTnVtYmVyIjo1Mjl9",
}

headers = {
    "authority": "cs.money",
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8,ru;q=0.7",
    # 'cookie': '_gcl_au=1.1.1364228153.1675618691; utm_source=google; utm_medium=cpc; utm_campaign=Search_Brand_UA_Desktop_Act; utm_term=cs%20money; utm_content=ads_adaptive; sc=D1059B1C-E62B-7BD7-2A02-C8F2870F2593; _gid=GA1.2.1700211239.1675618692; _fbp=fb.1.1675618691606.1141373986; _scid=00177fb3-9654-44fc-a638-4e28c846b5e6; new_language=ru; _hjSessionUser_2848248=eyJpZCI6IjU0MWI5MDQ0LTJhODUtNWE3OS1iZTZhLTUyODc3YmU3Y2RhOCIsImNyZWF0ZWQiOjE2NzU2MTg2OTE1ODQsImV4aXN0aW5nIjp0cnVlfQ==; page_before_registration=/ru/; csgo_ses=f2bb698d13e658d5ff860bfabf1190f9798899a8ff05d6548b15249b5bc69569; steamid=76561199042153366; avatar=https://avatars.akamai.steamstatic.com/f4e7432889c3773c1f585f0f5ccf488fec760a5b_medium.jpg; username=%E5%85%AB%E6%80%80%E5%85%AB%E6%9C%88%E5%88%9D%E5%85%AB; support_token=5ed32378b0e7fb4fea5db31d23b240025ff3968ce5e0c8ea9412733010c04bca; registered_user=true; AB_TEST_CONCRETE_SKIN_1_ITERATION=a; _gcl_aw=GCL.1675618707.EAIaIQobChMIzbHEhfb-_AIVrkaRBR1WWguZEAAYASAAEgL18PD_BwE; GleamId=nKZepxjJBgFaO9fwm; GleamA=%7B%22nKZep%22%3A%22login%22%7D; onboarding__skin_quick_view=false; _gac_UA-77178353-1=1.1675618796.EAIaIQobChMIzbHEhfb-_AIVrkaRBR1WWguZEAAYASAAEgL18PD_BwE; _tt_enable_cookie=1; _ttp=EzrC2l3Sw0rFbZdxaQCCdHT4svx; _sctr=1|1676152800000; _hjHasCachedUserAttributes=true; isAnalyticEventsLimit=true; _dc_gtm_UA-77178353-1=1; _ga_HY7CCPCD7H=GS1.1.1676329696.43.0.1676329696.60.0.0; _ga=GA1.1.485440045.1675618692; _hjIncludedInSessionSample_2848248=1; _hjSession_2848248=eyJpZCI6ImQ2YmIxNGE0LTM3MTktNDBjMi05N2FjLTBlMjFiYmM5MjY2OCIsImNyZWF0ZWQiOjE2NzYzMjk2OTYzMTksImluU2FtcGxlIjp0cnVlfQ==; _hjIncludedInPageviewSample=1; _hjAbsoluteSessionInProgress=0; _hjUserAttributesHash=b0cab6883fdd7eb32048d4d25bd33701; _uetsid=dc6bad90a57b11edaf50e5dbc6330abb; _uetvid=dc6bd140a57b11ed8d730dab9587bafa; amplitude_id_c14fa5162b6e034d1c3b12854f3a26f5cs.money=eyJkZXZpY2VJZCI6Ijg4NzdkODJmLTg4ZGYtNDhkZC1iMGRjLThmOTRmZmY1MzFjOFIiLCJ1c2VySWQiOiI3NjU2MTE5OTA0MjE1MzM2NiIsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTY3NjMyOTY5NjA3NCwibGFzdEV2ZW50VGltZSI6MTY3NjMyOTcwNTAxNSwiZXZlbnRJZCI6MjAzLCJpZGVudGlmeUlkIjozMjYsInNlcXVlbmNlTnVtYmVyIjo1Mjl9',
    "if-none-match": 'W/"b32-yMgPc9tVIUrCXTPm8vQ9Iuxx/8E"',
    "referer": "https://cs.money/ru/market/sell/",
    "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "traceparent": "00-9668fcc1c15bcbecab62d8ad7072811c-ca48d4e956eb298a-01",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "x-client-app": "web",
}

response = requests.get(
    "https://cs.money/1.0/market/active-offers", cookies=cookies, headers=headers
)
