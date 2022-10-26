import pandas

# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

data = pandas.read_csv('nato_phonetic_alphabet.csv')

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

asking = True

while asking:

    user_input = input('Please enter word:\n')
    user_input = user_input.upper()

    try:
        output_list = [phonetic_dict[letter] for letter in user_input]
        print(output_list)
        asking = False
    except KeyError:
        print('Just letters in the alphabet please!')
