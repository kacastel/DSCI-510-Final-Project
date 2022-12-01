hpi_data = requests.get('https://api.healthyplacesindex.org/api/hpi?geography=tracts&year=2020&indicator=voting&format=json&key=f07f86d6-58b5-40e3-a17f-333b92ccc57d').json()
vaccine_data = requests.get('https://data.sandiegocounty.gov/resource/nrkb-eanb.json').json()

hpi_data
vaccine_data