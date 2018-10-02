import urllib.request, json 
import time

competitions = []
# for each competition, we want to store [competitionID, competitionName,
#  competitionTitle, competitionURL, totalTeams, rewardQuantity, rewardTypeName, enabledDate,
#  maxDailySubmissions, evaluationMetric, awardsPoints, ]

#### CODE THAT CREATES JSON FILE OF COMPETITIONS. ONLY RUN ONCE ####
# dict = {}

# for i in range(1, 16):
#     with urllib.request.urlopen("https://www.kaggle.com/competitions.json?page={}".format(i)) as url:
#         data = json.loads(url.read().decode())
#         dict[i] = data

# with open('kaggle_competition_data.json', 'w') as fp:
#     json.dump(dict, fp)

#### CODE THAT CREATS JSON FILE OF COMPETITION ID -> COMPETITION LEADERBOARD DATA
leaderboard_dict = {}
with open('kaggle_competition_data.json') as json_data:
    competition_data = json.load(json_data)

    for i in range(1, 16):
        competition_page = competition_data['{}'.format(i)]
        competitions = (competition_page['pagedCompetitionGroup']['competitions'])
        for competition in competitions:
            print("Processing competition {}".format(competition))
            time.sleep(10)
            competition_id = competition['competitionId']
            with urllib.request.urlopen("https://www.kaggle.com/c/{}/leaderboard.json?includeBeforeUser=true&includeAfterUser=false".format(competition_id)) as url:
                data = json.loads(url.read().decode())
                print(data)
                print("*"*80)
                leaderboard_dict[competition_id] = data

with open('kaggle_competition_leaderboard_data.json', 'w') as fp:
     json.dump(leaderboard_dict, fp)

#with urllib.request.urlopen("https://www.kaggle.com/c/2667/leaderboard.json?includeBeforeUser=true&includeAfterUser=false")