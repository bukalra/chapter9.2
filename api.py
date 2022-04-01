from operator import delitem
import requests
import csv

#func that pulls data from NBP api
def get_rates():
    r = requests.get('http://api.nbp.pl/api/exchangerates/tables/c?format=json')
    if r.status_code != 200:
        print('Something went wrong...')
        print(r.status_code)
    else:
        data = r.json()[0]['rates']
    return data


#func that exports currencies to the .csv file
def export_file_to_csv(data):
    with open('nbp_rates.csv', 'w', newline='') as csvfile:
        fieldnames = ['currency','code','ask','bid']
        writer = csv.DictWriter(csvfile,fieldnames=fieldnames, delimiter= ";")
        writer.writeheader()
        
        for item in data:
            writer.writerow({'currency':item['currency'],'code':item['code'],'ask':item['ask'],'bid':item['bid']})
        print('Successfully exported data to nbp_rates.csv')

if __name__=="__main__":
    data = get_rates()
    export_file_to_csv(data)