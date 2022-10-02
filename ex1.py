import urllib.request

def remove_delimiters(s):
    delimiters = [",", ".", "!", "?", "/", "&", "-", ":", ";", "@", "'", "..."]

    for d in delimiters:
        ind = s.find(d)
        while ind != -1:
            s = s[:ind] + s[ind+1:]
            ind = s.find(d)

    return ' '.join(s.split())

def get_symbol(element):
    return element.split()[0]

def exercise_1():

    # Get data : 
    url =  "https://raw.githubusercontent.com/exorde-labs/TestnetProtocol/main/targets/keywords.txt"
    file = urllib.request.urlopen(url)

    # Iterate and clean data : 
    text = []
    for line in file:
        element = line.decode('utf-8').strip()
        element_cleaned = get_symbol(remove_delimiters(element))
        text.append(element_cleaned)

    # Checking if is not null :
    if (len(text)) :
        text_unduplicated = set(text) # To remove duplicate, no need to convert back to list if we need just iterate because set is iterable
    
        #Sorted :
        text_sorted = sorted(text_unduplicated)
        print('Element Sorted are :', text_sorted)

        #Smaller or equal than 4 characters :
        smallers = list(set(filter(lambda x:len(x)<=4, text_sorted)))
        print("Number of elements smaller or equal than 4 characters are :", len(smallers))

    else :
        print("Unique Element is Null")

if __name__ == "__main__":
    exercise_1()