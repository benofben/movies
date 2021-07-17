import sys
from rockset import Client, ParamDict

ROCKSET_API_KEY = 'mJr4cmYxvcS7VjF0EnP2h6RtUi8bVppzGWS7v85KF1cug6lqoinAU585aomkuoc6'

if len(sys.argv)==2:
    year=sys.argv[1]
    print('Querying Rockset for year ' + year + '...')
else:
    print('usage: python3 movies.py [year]')
    exit(1)

params = ParamDict()
params['year'] = year

print('\nLet\'s get the top rated movies...')
rs = Client(api_key=ROCKSET_API_KEY, api_server='https://api.rs2.usw2.rockset.com')
qlambda = rs.QueryLambda.retrieve('mostpopular',version='744188d437a6ac0d',workspace='commons')
results = qlambda.execute(parameters=params)
print('\nThe top 10 most popular movies for ' + year + ' are...')
for i in range(0,10):
    print(str(i) + ' ' + results['results'][i]['title'] + ' ' + str(results['results'][i]['popularity']))

print('\nLet\'s get the top grossing movies...')
qlambda = rs.QueryLambda.retrieve('highestgrossing', version='b1c9036b3a6ae864', workspace='commons')
results = qlambda.execute(parameters=params)
print('\nThe top 10 highest grossing movies for ' + year + ' are...')
for i in range(0,10):
    print(str(i) + ' ' + results['results'][i]['title'] + ' ' + str(results['results'][i]['revenue']) + ' ' + str(results['results'][i]['r']))

print('\nLet\'s get the top genres...')
qlambda = rs.QueryLambda.retrieve('topgenres', version='fc8349e40153ebf1', workspace='commons')
results = qlambda.execute(parameters=params)
print('\nThe top 10 genres for ' + year + ' are...')
for i in range(0,10):
    print(str(i) + ' ' + results['results'][i]['name'] + ' ' + str(results['results'][i]['?count']))
