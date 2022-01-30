import csv
import json

with open("../data/neos.csv", encoding='utf-8') as f:
    reader = csv.DictReader(f)
    has_name_count = 0
    for line in reader:
        name = line.get("diameter", "").strip()
        if name:
            has_name_count+= 1
            
    print(has_name_count)




with open("../data/cad.json", encoding='utf-8') as f:
  data = json.load(f)
  for entry in data["data"]:
    date = entry[3]
    if date.startswith("2000-Jan-01"):
        print(entry)
        
        #['2015 CL', '7', '2451544.575085225', '2000-Jan-01 01:48', '0.144929602021186', '0.144894711605919', '0.144964493657327', '12.0338907050642', '12.0323628689746', '00:19', '25.3']