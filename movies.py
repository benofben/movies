import sys
from rockset import Client, ParamDict
from tabulate import tabulate

def query(q):
    print('\n' + q['message'] + year + ' are...')
    qlambda = rs.QueryLambda.retrieve(q['query'],version=q['version'], workspace='commons')
    results = qlambda.execute(parameters=params)
    print(tabulate(results['results'], headers='keys'))

ROCKSET_API_KEY = 'mJr4cmYxvcS7VjF0EnP2h6RtUi8bVppzGWS7v85KF1cug6lqoinAU585aomkuoc6'

if len(sys.argv)==2:
    year=sys.argv[1]
    print('Querying Rockset for year ' + year + '...')
else:
    print('usage: python3 movies.py [year]')
    exit(1)

params = ParamDict()
params['year'] = year
rs = Client(api_key=ROCKSET_API_KEY, api_server='https://api.rs2.usw2.rockset.com')

queries=[
    {'message':'The top 10 most popular movies for ', 'query':'mostpopular', 'version':'4a9eeaec908830b0'},
    {'message':'The top 10 highest grossing movies for ', 'query':'highestgrossing', 'version':'9ed282f82b8d18c3'},
    {'message':'The top 10 genres for ', 'query':'topgenres', 'version':'ff13cce933698574'},
    {'message':'The top production companies for the most popular genre of ', 'query':'topproductioncompanies', 'version':'67a8f1531a780120'}]

for q in queries:
    query(q)
