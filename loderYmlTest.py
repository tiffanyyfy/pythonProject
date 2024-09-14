
from common.loder import ymlLoader as YL

ymlFile = r'test_yml.yml'
yml = YL.lode_yml_file(ymlFile)

print("loder yml file ,result:{}".format(yml))

print("application-name:{}".format(yml.get('server').get('port')))