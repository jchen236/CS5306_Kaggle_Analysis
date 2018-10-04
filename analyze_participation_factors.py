import urllib.request, json
import matplotlib.pyplot as plt
from functools import reduce
import numpy as np
import time

# The goal of this file is to analyze metadata about a competition and see how that affects the number of teams
# that submit as well as the total number of submissions


# $reward vs # of teams
# $reward vs # of submissions
# awardsPoints vs # of teams
# awardsPoints vs # of submissions
# categories vs # of teams
# categories vs # of submissions

#### LOAD JSON ####
competition_data = []
leaderboard_data = []
kernel_data = []
with open('kaggle_competition_data.json') as competition_json_data:
    competition_data = json.load(competition_json_data)
with open('kaggle_competition_leaderboard_data.json') as leaderboard_json_data:
    leaderboard_data = json.load(leaderboard_json_data)
with open('kaggle_competition_kernel_data.json') as kernel_json_data:
    kernel_data = json.load(kernel_json_data)

## CALCULATE REWARD VS TEAMS/SUBMISSIONS AND REWARD TYPE VS TEAMS/SUBMISSIONS
reward_to_teams = []
reward_to_submissions = []
reward_type_to_teams = {}
reward_type_to_submissions = {}

kernel_count_to_teams = []
kernel_count_to_submissions = []
num_competitions = 0
for i in range(1, 16):
    competition_page = competition_data['{}'.format(i)]
    competitions = (competition_page['pagedCompetitionGroup']['competitions'])
    for competition in competitions:
        num_competitions+=1
        competition_id = competition['competitionId']
        print(competition_id)
        
        reward_type_name = competition['rewardTypeName']
        reward_quantity = competition['rewardQuantity']
        if reward_type_name == None:
            print("NO REWARD TYPE NAME  ")
            print(competition_id)
        total_teams = competition['totalTeams']
        leaderboard_submissions_for_competition = leaderboard_data[str(competition_id)]
        total_submissions = 0

        if leaderboard_submissions_for_competition == []:
            continue;
        for submission in leaderboard_submissions_for_competition['submissions']:
            total_submissions += int((submission['entries']))
       
        # Populate lists and dictionaries
        reward_to_teams.append( (reward_quantity if (reward_quantity != None) else 0, total_teams))
        reward_to_submissions.append( (reward_quantity if (reward_quantity != None) else 0, total_submissions))

        if reward_type_name in reward_type_to_teams:
            reward_type_to_teams[reward_type_name].append(total_teams)
        else:
            reward_type_to_teams[reward_type_name] = [total_teams]

        if reward_type_name in reward_type_to_submissions:
            reward_type_to_submissions[reward_type_name].append(total_submissions)
        else:
            reward_type_to_submissions[reward_type_name] = [total_submissions]
        
        try:
            kernel_count_for_competition = kernel_data[str(competition_id)]
            num_kernels = str(kernel_count_for_competition)
            kernel_count_to_teams.append((num_kernels, total_teams))
            kernel_count_to_submissions.append((num_kernels, total_submissions))
        except KeyError:
            print("key error when trying to access kernel")

# print(reward_to_teams)
# print("*"*80)
# print(reward_to_submissions)
# print("*"*80)
# print(reward_type_to_teams)
# print("*"*80)
# print(reward_type_to_submissions)


# show relationship between reward to number of teams
# x = []
# y = []
# for pair in reward_to_teams:
#     x.append(pair[0] / 1000.0)
#     y.append(pair[1])

# plt.scatter(x,y)
# plt.xlabel('Award amount in thousands of $')
# plt.ylabel('Number of Teams per Competition')
# plt.title("Effect of Award Amount on Number of Teams")
# plt.savefig("AwardVsTeamCount.png")
# plt.show()


# show relationship between reward to number of submissions
# x = []
# y = []
# for pair in reward_to_submissions:
#     x.append(pair[0] / 1000.0)
#     y.append(pair[1])

# plt.scatter(x,y)
# plt.xlabel('Award amount in thousands of $')
# plt.ylabel('Number of Submissions per Competition')
# plt.title("Effect of Award Amount on Number of Submissions")
# plt.savefig("AwardVsSubmission.png")
# plt.show()

#show relationship between reward type to number of teams
# keys = ['Knowledge', 'USD', 'Swag', 'Kudos', None,'Jobs']
# type_counts = []
# y_pos = np.arange(len(keys))
# for key in keys:
#     team_counts = reward_type_to_teams[key]
#     avg_count = reduce(lambda x, y: x + y, team_counts) / len(team_counts)
#     type_counts.append(avg_count)

# plt.bar(y_pos, type_counts, align='center', alpha=0.5)
# plt.xticks(y_pos, keys)
# plt.xlabel('Award Type')
# plt.ylabel('Average Number of Teams per Competition')
# plt.title("Effect of Award Type on Number of Teams")
# plt.savefig("AwardTypevsTeam.png")
# plt.show()



# show relationship between reward to number of submissions
# keys = ['Knowledge', 'USD', 'Swag', 'Kudos', None,'Jobs']
# type_counts = []
# y_pos = np.arange(len(keys))
# for key in keys:
#     submission_count = reward_type_to_submissions[key]
#     avg_count = reduce(lambda x, y: x + y, submission_count) / len(submission_count)
#     type_counts.append(avg_count)

# plt.bar(y_pos, type_counts, align='center', alpha=0.5)
# plt.xticks(y_pos, keys)
# plt.xlabel('Award Type')
# plt.ylabel('Average Number of Submissions per Competition')
# plt.title("Effect of Award Type on Number of Submissions")
# plt.savefig("AwardTypevsSubmissions.png")
# plt.show()

# show relationship between kernel_count to number of teams
# x = []
# y = []
# for pair in kernel_count_to_teams:
#     x.append(pair[0])
#     y.append(pair[1])

# plt.scatter(x,y)
# plt.xlabel('Number of Kernels')
# plt.ylabel('Number of Teams per Competition')
# plt.title("Effect of Kernel Count on Number of Teams")
# plt.savefig("KernelVsTeamCount.png")
# plt.show()

# show relationship between kernel_count to number of submissions
x = []
y = []
for pair in kernel_count_to_submissions:
    x.append(pair[0])
    y.append(pair[1])

plt.scatter(x,y)
plt.xlabel('Number of Kernels')
plt.ylabel('Number of Submissions per Competition')
plt.title("Effect of Kernel Count on Number of Submissions")
plt.savefig("KernelVsSubmissionCount.png")
plt.show()
        

