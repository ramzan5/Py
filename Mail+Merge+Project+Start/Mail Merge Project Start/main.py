#TODO: Create a letter using starting_letter.txt 
placeholder = '[name]'

with open('../Mail Merge Project Start/Input/Names/invited_names.txt') as names:
    content1 = names.readlines()
    # print(len(content1))
with open('../Mail Merge Project Start/Input/Letters/starting_letter.txt') as invitation_letter:
    content = invitation_letter.read()
    for name in content1:
        striped_name = name.strip()
        new_letter = content.replace(placeholder, striped_name)

        with open(f'../Mail Merge Project Start/Output/ReadyToSend/{name}.txt','w') as f3:
            f3.write(new_letter)







