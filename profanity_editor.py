import urllib

def read_text():
    #Give the absolute path of the file you want to check for profanity as input for open
    input_file = open("C:\Users\Avani\Desktop\Python udacity\Input_for_profanity_editor.txt")
    input_text = input_file.read()
    #print(input_text)
    input_file.close()
    profanity_check(input_text)

def profanity_check(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
    output = connection.read()
    connection.close()

    if "true" in output :
        print("Profanity Alert")
    elif "false" in output :
        print("Good to go")
    else :
        print("Error in reading the file")



read_text()
