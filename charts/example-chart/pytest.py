import yaml
stream =open('values.yaml', 'r')
data =yaml.load(stream, Loader=yaml.FullLoader)
var = data.get('image').get('tag')
print(var)
