import pandas as pd

pypoll = pd.read_csv(r"C:\Users\fawzi\Documents\GitHub\python-challenge\PyPoll\Resources\election_data.csv.")

# total number votes casts
total_votes = len(pypoll)

# list of candidates
candidates = pypoll["Candidate"].value_counts()

# percetage of votes
percentage = (candidates/total_votes) * 100

# popular vote winner
max_votes = candidates.idxmax()

# print results
results = f"Election Results\n----------------------------\nTotal Votes: {total_votes}\n----------------------------\n"

for candidate in candidates.index:
    results += f"{candidate}: {percentage[candidate]:.3f}% ({candidates[candidate]})\n"

results += f"-------------------------\nWinner: {max_votes}\n-------------------------"    

print(results)

# export as txt
path = r"C:\Users\fawzi\Documents\GitHub\python-challenge\PyPoll\pypoll_challenge_results.txt"
with open(path, "w") as f:
    f.write(results)