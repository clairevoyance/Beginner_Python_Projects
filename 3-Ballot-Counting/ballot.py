polls = []

# As the name suggests, this program counts the votes and displays the name of the winner

number = int(input('Enter the number of polls taken : '))
print('Please enter the polls under : ')
for i in range(number):
    temp = input('Vote given to : ')
    polls.append(temp)
votes = []
candidates = []
max_candidates = []
for candidate in polls:
    if candidate not in candidates:
        candidates.append(candidate)
        votes.append(1)
    else:
        index = candidates.index(candidate)
        votes[index] += 1
max_votes = 0
for i in range(len(votes)):
    if votes[i] > max_votes:
        max_candidates = []
        max_votes = votes[i]
        max_candidates.append(candidates[i])
    elif votes[i] == max_votes:
        max_candidates.append(candidates[i])
print(*votes, sep=' ')
print('The maximum votes are obtained by the following : ')
print(*max_candidates, sep='\n')
print('The votes obtained by each of them is :', max_votes)
