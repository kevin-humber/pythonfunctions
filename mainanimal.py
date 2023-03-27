import requests
import animalfunc

api_key = 'sC+rZaSDcGKobphXlZxeNg==k8NVPTOZa0iMTHqX'

names = ['seal', 'dog']

for name in names:
    url = f'https://api.api-ninjas.com/v1/animals?name={name}'

    response = requests.get(url, headers={'X-Api-Key': api_key})

    if response.status_code == requests.codes.ok:
        data = response.json()
		#pull animal data using our function from the functions file
        animal_data = animalfunc.pull_animal_data(data)
        animalfunc.write_file(name, animal_data)
    else:
        print("Error:", response.status_code, response.text)
    