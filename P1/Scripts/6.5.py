text = 'X-DSPAM-Confidence:    0.8475'
pos1 = text.find('    ')
pos2 = text.find('5', pos1)
num = text[pos1+1 : pos2+1]
print('the answer is:',num)
