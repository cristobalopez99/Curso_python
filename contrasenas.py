import random 

def generar_new_pwrd():
    capital = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    mins = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    symbols = ['!', '#', '%', '&', '*', '/', '(', ')']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    characters = capital + mins + symbols + numbers
    
    password = []

    for i in range(10):
        random_character = random.choice(characters)
        password.append(random_character)

    password = "".join(password)
    return password 




        
    

def run():
    password = generar_new_pwrd()
    print('Your new password is: ' + password)

    



if __name__ == '__main__':
    run()