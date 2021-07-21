import sys
from rockset import Client, ParamDict
from tabulate import tabulate

if len(sys.argv) == 2:
    year = sys.argv[1]
    print('Querying Rockset for year ' + year + '...\n')
else:
    print('usage: python3 movies.py [year]')
    exit(1)

params = ParamDict()
params['year'] = year
rs = Client()

queries = [
    {'message': 'The top 10 most popular movies for ', 'query': 'mostpopular', 'version': '4a9eeaec908830b0'},
    {'message': 'The top 10 highest grossing movies for ', 'query': 'highestgrossing', 'version': '9ed282f82b8d18c3'},
    {'message': 'The top 10 genres for ', 'query': 'topgenres', 'version': 'ff13cce933698574'},
    {'message': 'The top production companies for the most popular genre of ', 'query': 'topproductioncompanies', 'version': '67a8f1531a780120'}]


def query(q):
    print(q['message'] + year + ' are...')
    qlambda = rs.QueryLambda.retrieve(q['query'], version=q['version'], workspace='commons')
    results = qlambda.execute(parameters=params)
    print(tabulate(results['results'], headers='keys') + '\n')


for q in queries:
    query(q)
