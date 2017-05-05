from setting import params
from core import execute


url = params['url']
tag = params['tag']

dataframe = execute(url, tag)
dataframe.to_csv('output.txt', sep='\t', header=False)


