import csv

#populate 2d array name/profit
with open('./budget_data.csv','r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	
	header = next(csvreader)
	
	bankList = []
	bankList = [row for row in csvreader]

#Measure length of array
Length = len(bankList)

#iterate through rows looking at profit (column 2),
Total = 0.00
totalChange = 0.00
maxChange = ["date",0.00]
minChange = ["date",0.00]

for row in range(Length):
	Profit = float(bankList[row][1])
	
	#previous profit variable with handeling for second row
	if row >0:
		prevProfit = float(bankList[row-1][1])
	else: prevProfit = 0
	
	#date value for results
	Date = bankList[row][0]
	
	#add to total each iteration
	Total += Profit
	
	#Change in profit as variable and collected into list for average
	if row >0 and row < Length:
		profitChange = Profit - prevProfit
	else: profitChange = 0
	
	#collect current date and profit change if find a larger value than what is stored
	if float(maxChange[1]) < profitChange:
		maxChange = [Date,profitChange]
	
	#same but for minimum
	if float(minChange[1]) > profitChange:
		minChange = [Date,profitChange]

#sum of profit change for average, exclude first value
	totalChange += profitChange
	
#average change exclude first month because it has no value
avgChange = round(totalChange / (Length-1),2)

#print results in terminal

print("Number of Months: "+str(Length))
print("Total Profit/Loss: $"+str(Total))
print("Average Change $"+str(avgChange))
print("Maximum Profit is: "+str(maxChange))
print("Maximum Loss is: "+str(minChange))

#write to csv
with open('./output.csv','w') as csvfile:
	csvwriter = csv.writer(csvfile, delimiter=",")
	csvwriter.writerow(["Number of Months"]+[Length])
	csvwriter.writerow(["Total Profit/Loss"]+[Total])
	csvwriter.writerow(["Average Change"]+[avgChange])
	csvwriter.writerow(["Maximum Profit"]+[maxChange[0]]+[maxChange[1]])
	csvwriter.writerow(["Minimum Profit"]+[minChange[0]]+[minChange[1]])
	

