from operator import delitem
import requests
import csv
r = requests.get('http://api.nbp.pl/api/exchangerates/tables/c?format=json')
if r.status_code != 200:
    print('Something went wrong...')
    print(r.status_code)
else:
    data = r.json()[0]['rates']

def forwarder():
    return data



#func that exports currencies to the .csv file
def export_file_to_csv():
    with open('nbp_rates.csv', 'w', newline='') as csvfile:
        fieldnames = ['currency','code','ask','bid']
        writer = csv.DictWriter(csvfile,fieldnames=fieldnames, delimiter= ";")
        writer.writeheader()
        
        for item in data:
            writer.writerow({'currency':item['currency'],'code':item['code'],'ask':item['ask'],'bid':item['bid']})
        print('Successfully exported data to nbp_rates.csv')

if __name__=="__main__":
    export_file_to_csv()