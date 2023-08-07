import requests

def get_response(town):
  payload = {'n':'','M':'','T':'','q':'', 'lang':'ru'}
  response = requests.get(f'https://wttr.in/{town}', params=payload)
  response.raise_for_status()
  print(response.text)

def main():
  cities = ['Шереметьево','Лондон','Череповец']
  for city in cities:
    get_response(city)
  
if __name__ == '__main__':
  main()
