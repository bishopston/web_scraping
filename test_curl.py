import requests
import json

url = "https://www.worldcup2018.hockey/admin/api/v1/matches/get-match-statics-list"

payload = json.dumps({
  "perPage": "200",
  "page": 1,
  "competition_id": 1295,
  "team_id": [],
  "venus_id": []
})
headers = {
  'Connection': 'keep-alive',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
  'sec-ch-ua-mobile': '?0',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
  'sec-ch-ua-platform': '"Windows"',
  'Content-Type': 'application/json',
  'Accept': '*/*',
  'Origin': 'https://www.fihproleague.com',
  'Sec-Fetch-Site': 'cross-site',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Dest': 'empty',
  'Referer': 'https://www.fihproleague.com/',
  'Accept-Language': 'en-US,en;q=0.9,el;q=0.8',
  'Cookie': 'AWSELB=E7D97B4314FA26C81AC086FF58630988BE484265E525D60A9C696DAA05AE8FBBFB0049D54E2C518E4CC12A0412130845BF33CAA25C2A0DFE9096AE4916A965A12EF514FEBF; AWSELBCORS=E7D97B4314FA26C81AC086FF58630988BE484265E525D60A9C696DAA05AE8FBBFB0049D54E2C518E4CC12A0412130845BF33CAA25C2A0DFE9096AE4916A965A12EF514FEBF'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
