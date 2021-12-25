import yaml
stream =open('database.yml', 'r')
data =yaml.load(stream, Loader=yaml.FullLoader)
var = data.get('database').get('test')
print(var)
