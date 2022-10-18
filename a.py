import requests

headers = {
    'authority': 'www.gittigidiyor.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'apollographql-client-name': 'app-search',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'content-type': 'application/json',
    'accept': '*/*',
    'apollographql-client-version': '0.1.481',
    'sec-ch-ua-platform': '"Windows"',
    'origin': 'https://www.gittigidiyor.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.gittigidiyor.com/cep-telefonu-aksesuar/bluetooth-aksesuar/bluetooth-kulaklik?cmpg=4582&sf=2',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': '_sgf_user_id=5352966454066536449; TrackingId=d13c2d24e702f080915d44c5c0999fdef13b41ae; wis_unreg=1; __gads=ID=c7585ad7a46c4e21:T=1617215930:S=ALNI_MbdFT9lPuxnGMb96AFBGUcX2prdkQ; PSESSID=5ed58b05c08f89eabb547552793fc523; _sgf_session_id=5353141982354399232; _gcl_au=1.1.1457426270.1638642720; _gid=GA1.2.526747913.1638642721; _fbp=fb.1.1638642721647.2040317816; wis_u=b0883992-5c6a-17fc-b6e1-f2eb055af053|1617215927013|3|||68; wis_s_homecounter=1; wis_i_58310=140894; wis_i_24400=44671; lastViewed=589907330; TS20b97530027=08987aa469ab20002201894352be436255aee0ecd17b148c0d0868b698d3800c27a011d84f7aced908a1c5b430113000d0eb68bb1fba7bc19be6e81e86ecec81d64a899b489aade6c17da93e5e02a4899f11b6af204cc1a9e848fae4080038fb; _ga=GA1.2.66835683.1617215927; wis_v=1638642721713|8|Home Page|1; wis_s_srpcounter=7; wis_i_58311=140892; _dc_gtm_UA-313101-1=1; _ga_S8YE7ZZF2L=GS1.1.1638642720.4.1.1638643685.33',
}

data = {"operationName":"GetProducts","variables":{"slug":"cep-telefonu-aksesuar/bluetooth-aksesuar/bluetooth-kulaklik","url":"https://www.gittigidiyor.com/cep-telefonu-aksesuar/bluetooth-aksesuar/bluetooth-kulaklik?cmpg': '4582','sf': '2","store":"","platform":"DESKTOP","rows":32,"page":2},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"fc897513f81a740000ee9ed78f20e63979020689487f7653844f2df94ee44682"}}}


response = requests.post('https://www.gittigidiyor.com/nucleus-gateway', headers=headers , data=data)

print(response.content)
