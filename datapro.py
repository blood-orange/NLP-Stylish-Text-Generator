



def data_pro(lines,minlen,ngram,chardic):
	dataX = []
	dataY = []
	for line in lines:
		if len(line)<minlen:
			continue;
		else:
			for i in range(0,len(line)-ngram,1):
				numline =[]
				for char in line[i:i+ngram]:
					numline.append(chardic[char][0])
				next_char = line[i+ngram]
				dataX.append(numline)
				dataY.append(chardic[next_char][0])
	return {'dataX':dataX,'dataY':dataY,''}



charset = {"我":[1,4],"要":[2,5], "吃":[3,6], "饭":[4,4]}
testlines = ["我要吃饭","吃我饭要"]
print(data_pro(testlines,1,3,charset))

