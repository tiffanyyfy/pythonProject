'''
导入文件
'''
from typing import Dict

import yaml
from pydantic import BaseModel


class YmlLoder(BaseModel):

    def lode_yml_file(self, file) -> Dict:
        with(open(file, mode='rb')) as ymlFile:
            ymlObj = yaml.load(ymlFile, Loader=yaml.FullLoader)

            print("ymlObj:{}".format(ymlObj))
            return ymlObj


ymlLoader = YmlLoder()

# print(id(1))
# print(id(8))