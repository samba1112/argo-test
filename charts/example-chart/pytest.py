import yaml
stream =open('database.yml', 'r')
data =yaml.load(stream, Loader=yaml.FullLoader)
var = data.get('image').get('tag')
print(var)
