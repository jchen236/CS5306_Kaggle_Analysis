import urllib.request, json
import matplotlib.pyplot as plt
from functools import reduce
import numpy as np
import csv

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
competition_dict = {}
leaderboard_dict = {}
with open('kaggle_competition_data.json') as competition_json_data:
    competition_data = json.load(competition_json_data)
with open('kaggle_competition_leaderboard_data.json') as leaderboard_json_data:
    leaderboard_data = json.load(leaderboard_json_data)
with open('kaggle_competition_kernel_data.json') as kernel_json_data:
    kernel_data = json.load(kernel_json_data)

with open('competition2.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['competitionID', 'amount', 'teamNumber', 'submissionNumber', 'orgName', 'numKernels'])

for i in range(1, 16):
    competition_page = competition_data['{}'.format(i)]
    competitions = (competition_page['pagedCompetitionGroup']['competitions'])
    for competition in competitions:
        competition_id = competition['competitionId']
        reward_quantity = competition['rewardQuantity']
        num_kernels = 0
        try:
            num_kernels = int(kernel_data[str(competition_id)])
        except KeyError:
            pass
        if reward_quantity != None and reward_quantity > 0:
            competition_dict[competition_id] = competition
            leaderboard_dict[competition_id] = leaderboard_data[str(competition_id)]
            leaderboard_submissions_for_competition = leaderboard_data[str(competition_id)]
            total_submissions = 0
            if leaderboard_submissions_for_competition != []:
                for submission in leaderboard_submissions_for_competition['submissions']:
                    total_submissions += int((submission['entries']))
        
            with open('competition2.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([competition_id, reward_quantity, competition['totalTeams'], total_submissions, competition['organizationName'], num_kernels])

