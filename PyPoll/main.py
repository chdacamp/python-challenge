import csv

with open('./election_data.csv','r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	Header = next(csvreader)
	
	voteList = [row for row in csvreader]
	

#set comprehension for set of unique candidates, then converted to list
Candidates = {}
Candidates = {row[2] for row in voteList if row[2] not in Candidates}
#convert Candidates to list
listCan = list(Candidates)
#convert to keys in dict and add 0
dictCan = dict.fromkeys(Candidates,0)
dictCanPerc = dict.fromkeys(Candidates,0)

#If key found in row add to value in dictionary
for row in voteList:
	for can in range(0,len(listCan)):
		if row[2] == listCan[can]:
			dictCan[listCan[can]] = dictCan[listCan[can]] + 1

#Number of Votes
Length = len(voteList)

#loop for new dictionary to create a percent from value
for can in range(0,len(listCan)):
	dictCanPerc[listCan[can]] = dictCan[listCan[can]]/Length


#Collect max winnng value into winner variable	
Winning = 0

for can in range(0,len(listCan)):
	if dictCanPerc[listCan[can]] > Winning:
		Winning = dictCanPerc[listCan[can]]
		Winner = listCan[can]
		

#printing results

print("Election Results")
print("--------------------")
print("Total Votes: "+str(Length))
print("--------------------")

#loop pulling results out of dictionary for each candidate
for can in range(0,len(listCan)):
	print (listCan[can] + " | Votes: " + str(dictCan[listCan[can]])+" | Percent: "+str("{:.2%}".format(dictCanPerc[listCan[can]])))
print("--------------------")
print("Winner is... " + str(Winner))

#write to csv
with open('./output.csv','w') as csvfile:
	csvwriter = csv.writer(csvfile, delimiter=",")
	csvwriter.writerow(["Election Results"])
	csvwriter.writerow(["Total Votes: "]+[str(Length)])
	for can in range(0,len(listCan)):
		csvwriter.writerow([listCan[can]] + ["Votes:"] + [str(dictCan[listCan[can]])]+["Percent:"]+[str("{:.2%}".format(dictCanPerc[listCan[can]]))])
	csvwriter.writerow(["Winner:"]+[Winner])


