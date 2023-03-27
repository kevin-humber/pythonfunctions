import json
import requests

def pull_animal_data(animal_input):
    animal_response={}
    animal_response['animal name']=animal_input[0]['name']
    animal_response['kingdom']=animal_input[0]['taxonomy']['kingdom']
    animal_response['location']=animal_input[0]['locations']
    animal_response['top speed']=animal_input[0]['characteristics']['top_speed']
    return animal_response

def write_file(animalName, content):
    pretty_response = json.dumps(content, indent=4)
    filename =f'{animalName}_pulleddata.txt'
    with open (filename, 'w') as file:
        #write the data into the file
        file.write(pretty_response)
        print('saved to file')
        file.close()
    return filename
'''
In Python, the if __name__ == "__main__" statement is used to check whether the current script 
is being run as the main program or being imported as a module in another script. If the script 
is being run as the main program, the code block inside the if statement will execute. If it is being 
imported as a module in another script, the code block will not execute.

The __name__ variable is a special built-in variable in Python that holds the name of the current module. 
When a script is being run as the main program, the value of __name__ is set to "__main__".
'''

if __name__ == "__main__":
    api_key = 'sC+rZaSDcGKobphXlZxeNg==k8NVPTOZa0iMTHqX'
    animal = 'lion'
    url = f'https://api.api-ninjas.com/v1/animals?name={animal}'
    response = requests.get(url, headers={'X-Api-Key': api_key})

    if response.status_code == requests.codes.ok:
        data = response.json()
		#pull animal data using our function from the functions file
        animal_data = pull_animal_data(data)
        write_file(animal, animal_data)
    else:
        print("Error:", response.status_code, response.text)
