chai_desc = "Aromatic and Bold"
print(f"first word : {chai_desc[0:8]}")
print(f"first word : {chai_desc[:8]}")
print(f"second word : {chai_desc[0:8:1]}") # in [0:8:1] -> 1 means each character
print(f"Third word : {chai_desc[0:8:2]}") # in [0:8:2] -> 2 means skip odd index character
print(f"Fourth word : {chai_desc[9:-1]}") # in [9:-1] -> -1 means till last character(does not include last character)
print(f"Fifth word : {chai_desc[9:]}") # in [9:] -> empty number means till last character(includes last character)
# Reverse String
print(f"Reversed word : {chai_desc[::-1]}") # in [::-1] -> -1 means reverse the string 

# Encoding a String with foriegn language
label_text = "Chai Spècial"
encode_lable = label_text.encode('utf-8')
print(f"Non Encoded Lable : {label_text}")
print(f"Encoded Lable : {encode_lable}")

decode_label = encode_lable.decode("utf-8")
print(f"Decoded Lable : {decode_label}")



