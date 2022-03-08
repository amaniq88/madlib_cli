import re
def read_template(path):
    '''
    read function used to read the data from file , rais error incase the file not found error
    input : path of the file 
    output : string that contain data in the file 
    '''
    try:
        f = open(path)
    except FileNotFoundError:
        content = "Error: Sorry the file does not exist!"
        raise FileNotFoundError
    else:
        content = f.read()
        f.close()
        return content

def test_push():
    pass

def test_push_new():
    pass

def parse_template(content):
    '''
    parse function used to divide the string into dtripped and parts 
    input : string 
    output : stripped and parts 
    '''
    parts = re.findall('{(.+?)}',content)
    stripped = re.sub('{(.+?)}', '{}', content)
    return stripped , tuple(parts)  


def merge(stripped, userInput):
    '''
    merge the user answers with the stripped part 
    input : the stripped part and user input 
    output : string contain the story 
    '''
    gameResuilt = stripped.format(*userInput)
    return gameResuilt

if __name__ == "__main__":
    print('''
**************************************
**    Welcome to the Midlib!   **
**       Instructions          ** 
In this python game user has to enter 
substitutes for blanks in the story 
without knowing the story.
        *************
 It will be fun to read aloud the stories 
  after filling the blanks.
**************************************
    ''')
    stripped_data , parts_data = parse_template(read_template("madlib_cli/data.txt")) 
    user_input = []
    for i in parts_data:
        user_input.append(input(i+" : "))
    game = merge(stripped_data, tuple(user_input))

    print ('''Finaly Got your story ...
            ****************************
            ****************************

    ''')
    
    print(game)
    with open("./madlib_cli/game.txt", "w") as f:
            f.write(game)
