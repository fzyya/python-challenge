import pandas as pd

pybank = pd.read_csv(r'C:\Users\fawzi\Documents\GitHub\python-challenge\PyBank\Resources\budget_data.csv.')

# total number of months
total_months = len(pybank)

# net total amount of profit/losses
total = pybank["Profit/Losses"].sum()

# average change in profit/loss
pybank["Changes"] = pybank["Profit/Losses"].diff()
average_change = pybank["Changes"].mean()

# max profit/loss
max_pl = pybank["Changes"].max()
date_max_pl = pybank[pybank["Changes"]==max_pl]["Date"].values[0]

# min profit/loss
min_pl = pybank["Changes"].min()
date_min_pl = pybank[pybank["Changes"]==min_pl]["Date"].values[0]

# print results
results = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: {total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {date_max_pl} (${max_pl:.0f})\n"
    f"Greatest Decrease in Profits: {date_min_pl} (${min_pl:.0f})"
)

print(results)

# export at txt
path = r"C:\Users\fawzi\Documents\GitHub\python-challenge\PyBank\pybank_challenge_results.txt"
with open(path, "w") as f:
    f.write(results)
