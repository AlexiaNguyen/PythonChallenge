import os
import csv
pypoll = os.path.join("election_data.csv")

total_vote = 0
khan_vote = 0
correy_vote = 0
li_vote = 0
otooley_vote = 0
khan_percent = 0
correy_percent = 0
li_percent = 0
otooley_percent = 0
candidate = {}

with open(pypoll, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)
    for row in csv_reader:
        total_vote = total_vote +1
        
        if row[2] in candidate.keys():
            candidate[row[2]] = candidate[row[2]] + 1
        else:
            candidate[row[2]] = 1

    khan_percent = (candidate.get('Khan'))/sum(candidate.values()) * 100
    correy_percent = (candidate.get('Correy'))/sum(candidate.values()) * 100
    li_percent = (candidate.get('Li'))/sum(candidate.values()) * 100
    otooley_percent = (candidate.get("O'Tooley"))/sum(candidate.values()) * 100

    winner = max(candidate, key=candidate.get)

print("Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_vote}")
print(f"----------------------------")
print(f"Khan: {khan_percent:.2f}% ({candidate.get('Khan')})")
print(f"Correy: {correy_percent:.2f}% ({candidate.get('Correy')})")
print(f"Li: {li_percent:.2f}% ({candidate.get('Li')})")
print(f"""O'Tooley: {otooley_percent:.2f}% ({candidate.get("O'Tooley")})""")
print(f"----------------------------")
print(f"Winner: {winner}")


output_file = os.path.join("Election_Results_Summary.txt")

with open(output_file,"w") as f:

    f.write("Election Results")
    f.write("\n")
    f.write(f"----------------------------")
    f.write("\n")
    f.write(f"Total Votes: {total_vote}")
    f.write("\n")
    f.write(f"----------------------------")
    f.write("\n")
    f.write(f"Khan: {khan_percent:.2f}% ({khan_vote})")
    f.write("\n")
    f.write(f"Correy: {correy_percent:.2f}% ({correy_vote})")
    f.write("\n")
    f.write(f"Li: {li_percent:.2f}% ({li_vote})")
    f.write("\n")
    f.write(f"O'Tooley: {otooley_percent:.2f}% ({otooley_vote})")
    f.write("\n")
    f.write(f"----------------------------")
    f.write("\n")
    f.write(f"Winner: {winner}")
    f.write("\n")