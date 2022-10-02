import urllib.request, json, re


def is_letter(char):
    return ("A" <= char <= "Z") or ("a" <= char <= "z")

def extract_words(sentence):
    word = ""
    words_list = []
    for ch in sentence:
        if is_letter(ch):
            word += ch
        else:
            if word:
                words_list.append(word)
                word = ""
    if word:
        words_list.append(word)
    return words_list

def exercise_2():

    # Get data : 
    url =  "https://bafybeidqw6oyclcnmqjbj2472vzofyhafdtot5woenazsgpmm3b6irnaoi.ipfs.w3s.link/"
    reponse = urllib.request.urlopen(url)
    data = json.load(reponse)

    contents = []
    links = []
    total_items = 0
    words = set() # using set to not add duplicate and getting a lot of data that we don't need

    # Check if there is key "Content" + if is list + if there is items
    if ("Content" in data and isinstance(data['Content'], list) and len(data['Content'])):

        total_items = len(data['Content'])

        for i, item in enumerate(data['Content']):

            print('{} item /{}'.format(i, total_items))

            if (item["Content"] != "None") : 
                contents.append(item["Content"])
                links += re.findall(r'https?://[^\s<>")()]+|www\.[^\s<>"]+', str(item["Content"]))

                # print(item["Content"])

                content_splitted = extract_words(item["Content"])
                # content_splitted = item["Content"].split()
                for word in content_splitted :
                    if len(word) >= 8 and len(word) <= 20:
                        words.add(word)



        # Number items
        print('There is {} items'.format(total_items))

        # Links http and https
        print('There is {} links and {} unique links'.format(len(links), len(set(links))))


        # Top 5 of words between 8 and 20
        words_sorted = sorted(list(words), key=len, reverse=True)
        top_5 = words_sorted[:5]
        print('Top 5 words between 8 and 20:', top_5)

    else : print('There is no item in the JSON')


if __name__ == "__main__":
    exercise_2()
