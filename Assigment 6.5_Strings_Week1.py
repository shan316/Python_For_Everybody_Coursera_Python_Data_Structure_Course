text = "X-DSPAM-Confidence:    0.8475"
Start_POS = text.find("0")
End_POS = text.find("5")
Data = text[23:End_POS + 1]
Data = float(Data)
print(Data)