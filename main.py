import pandas
""""
student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass


student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

"""
user_input = str(input("Enter the word to convert to NATO alphabet:"))

nato_dic = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dic.columns = ["word", "value"]
# for w in user_input:
#     row = nato_dic.loc[nato_dic["word"] == w.upper()]
#     ans.append(row["value"].item())
ans = [nato_dic.loc[nato_dic["word"] == w.upper()]["value"].item() for w in user_input]
print(ans)

