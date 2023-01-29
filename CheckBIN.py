import json
import argparse
import requests

banner = """____ _  _ ____ ____ _  _ ___  _ _  _ 
|    |__| |___ |    |_/  |__] | |\ | 
|___ |  | |___ |___ | \_ |__] | | \|
"""

print(banner)
parser = argparse.ArgumentParser(description='CheckBIN - BIN Checker tool')
parser.add_argument("--bin", "-b", required=True, help="Enter the bin number to check")
args = parser.parse_args()

if not args.bin:
    parser.print_help()
    exit()

url = f"https://bank-card-bin-num-check.p.rapidapi.com/api/v1/bins/b/{args.bin}"

headers = {
"X-RapidAPI-Key": "3398693b48msh311dd6a4dbdd27bp19903ajsn7fcf6c888dda",
"X-RapidAPI-Host": "bank-card-bin-num-check.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)
data = json.loads(response.text)

print(f"BIN:     {data['bin_number']}")
print(f"Bank:    {data['bank']}")
print(f"Scheme:  {data['scheme']}")
print(f"Type:    {data['type']}")
print(f"Country: {data['country']}\n")
