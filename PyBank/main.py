
from ast import Index
import os
import csv
budget_csv=os.path.join("./Resources/budget_data.csv")
with open(budget_csv) as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=",")
    csv_header= next(csv_file)
    Month=[]
    Total_Profit_Losses=[]
    Profit_Loss= []
    Month_counter=0
    Previous_Month=0
    
    
    for row in csv_reader:
        Month_counter +=1
        Current_Month=(int(row[1]))
        if Month_counter==1:
            Previous_Month=Current_Month
        else:    
            Profit_Losses= ((Current_Month)-(Previous_Month))
            Total_Profit_Losses.append(int(row[1]))
            Profit_Loss.append(Profit_Losses)
            Previous_Month=Current_Month
            Month.append(row[0])
            Highest_Profit=max(Profit_Loss)
            x=Profit_Loss.index(max(Profit_Loss))
            y=Profit_Loss.index(min(Profit_Loss))
            Month_Index=(Month[x])
            Month_Index2=(Month[y])
    print ("Financial Analysis")
    print ("-----------------------")
    print ("Total Months:",(Month_counter))
    print ("Total:$",sum(Total_Profit_Losses))
    print ("Average Changes:","$",round(sum((Profit_Loss))/((Month_counter)-1),2))
    print ("Greatest Increase in Profits:",(Month_Index),"($",max(Profit_Loss),")")
    print ("Greatest Decrease in Profits:",(Month_Index2),"($",min(Profit_Loss),")")
    
  ### Print to text file ##### 
text_file = os.path.join("./analysis/PyBank.txt") 
with open(text_file, "w") as f:
    print("Financial Analysis", file=f)
    print("-----------------------", file=f)
    print("Total Months:",(Month_counter), file=f)
    print("Total:$",sum(Total_Profit_Losses), file=f)
    print("Average Changes:","$",round(sum((Profit_Loss))/((Month_counter)-1),2), file=f)
    print("Greatest Increase in Profits:",(Month_Index),"($",max(Profit_Loss),")", file=f)
    print("Greatest Decrease in Profits:",(Month_Index2),"($",min(Profit_Loss),")", file=f) 