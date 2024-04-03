import requests
import functools

@functools.lru_cache(maxsize=None)  # Memoização com cache ilimitado
def get_country_details(country_code):
    try:
        endpoint = f"https://restcountries.com/v3.1/alpha/{country_code}"
        response = requests.get(endpoint)
        
        if response.status_code == 200:
            country_data = response.json()
            return country_data
        else:
            print(f"Erro ao obter os detalhes do país {country_code}: {response.status_code}")
            return None
    except Exception as e:
        print(f"Ocorreu um erro ao obter os detalhes do país {country_code}: {e}")
        return None

@functools.lru_cache(maxsize=None)  # Memoização com cache ilimitado
def get_all_countries():
    try:
        endpoint = "https://restcountries.com/v3.1/all"
        
        response = requests.get(endpoint)
        
        if response.status_code == 200:
            countries_data = response.json()
            return countries_data
        else:
            print(f"Erro ao obter a lista de países: {response.status_code}")
            return None
    except Exception as e:
        print(f"Ocorreu um erro ao obter a lista de países: {e}")
        return None

print(get_country_details("USA"))  
print(get_country_details("GBR"))  
print(get_country_details("USA"))  
print(get_all_countries())
