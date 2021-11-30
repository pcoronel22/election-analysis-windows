#Add our dependencies
import csv
import os

#Add a variable to load a file from a path
file_to_load = os.path.join("Ressources", "election_results.csv")
#print (file_to_load)
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# intialize a total vote counter
total_votes = 0

#Candidate options and candidate votes
candidate_options=[]
candidate_votes = {}

#Challenge county option county votes
county_names = []
county_votes = {}

#track the winning candidate vote count and percentage
winning_candidate = ""
winning_count = 0 
winning_percentage = 0

#challenge: track the largest county vote turnout and its percentage
largest_county_turnout = ""
largest_county_vote = 0

with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    print(reader)

    #Read header
    header = next(reader)
    
    #loop each row in the csv file
    for row in reader:
        #add to the total vote count
        total_votes = total_votes+1
        #Get the candidate name from each row
        candidate_name = row[2]
        #Get the county name from each row
        county_name = row [1]
        #if the candidate does not match any existing candidate
        #add it to the list
        if candidate_name not in candidate_options:
            #Add the candidate name to candidate list
            candidate_options.append(candidate_name)
            #and beign tracking that candidate voter count
            candidate_votes [candidate_name] = 0
    #add vot to that candidate count
    candidate_votes[candidate_name] += 1
 
    #challenge
    if county_name not in county_names:
        #add it to the list of county
        county_names.append(county_names)
        #begin tracking the county votes
        county_votes[county_name] = 0

    county_votes[county_name]+= 1

print(candidate_votes)
print (county_votes)

#save the results to out text file
with open (file_to_save, "w") as text_file:
    #print the final count to terminal
    election_results = (
        f"\nElection Results\n"
        f"------------------\n"
        F"Total Votes {total_votes:,}\n"
        f"County Votes:\n"   
    )
    print(election_results, end= "")
    text_file.write(election_results)

    #Challenge Save final county vote to text file
    for county in county_votes:
        #retrieve vote count and percewntage
        county_vote = county_votes [county]
        county_percent=int(county_vote)/int(total_votes)*100

        county_results = (
            f"{county}: {county_percent:1f}% ({county_votes:,})\n"
        )
        print (county_results, end="")
        text_file.write(county_results)

        #Determine winning vote count

        if (county_vote > largest_county_vote):
            largest_county_vote = county_vote
            largest_county_turnout = county

        #print the county w the largest turnout
        largest_county_turnout = (
            f"\n--------------------\n"
            f"Largest County Turnout {largest_county_turnout}\n"
            f"\n--------------------\n"
        )
print(largest_county_turnout)
text_file.write(largest_county_turnout)

#save the final candidate vote count to the text file
for candidate in candidate_votes:
    #retrieve vote  count and percentage
    votes = candidate_votes[candidate]
    vote_percentage = int(votes)/int(total_votes) + 100
    candidate_results = (
        f"{candidate}:{vote_percentage:.1f}% ({votes:,}\n"
    )

    #print each candidate voter count and percentage to the terminal
    print(candidate_results)
    text_file.write(candidate_results)

    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_candidate = candidate
        winning_percentage = vote_percentage

    winning_candidate_summary = (
        f" --------------------------\n"
        f"winner: {winning_candidate}\n"
        f"winning vote count: {winning_count:,}\n"

    )
    print (winning_candidate_summary)
#save the winning candidate name totext file
txt_file.write(winning_candidate_summary)

