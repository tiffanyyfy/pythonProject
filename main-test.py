from fastapi import FastAPI

from schemas.pdauser import PdaUserSchema

app = FastAPI()

data = {
    "pdaUsers" : []
}

@app.get('/api/getPdaUser/{id}')
def getPdaInfo(id : int):
    list = data.get("pdaUsers")
    for item in list:
        if item.get('id') == id:
            return item
    return None

@app.get('/api/getAll')
def getAllPda():
    list = data.get("pdaUsers")
    return list

@app.post('/api/save')
def savePdaUser(pdaUser : PdaUserSchema ):
    list = data.get("pdaUsers")
    list.append(pdaUser)
    return pdaUser

@app.post('/api/update/{id}')
def update(*, id : int, name : str, pdaUser : PdaUserSchema ):
    print("update params ,id:{},name:{},pdaUser:{}".format(id, name, pdaUser.json()))
    list = data.get("pdaUsers")
    for item in list:
        # pu = PdaUser.dict(item)
        #  print("pu={}".format(pu))
        if(id == item.id and name == item.name):
            item.id = pdaUser.id
            item.name = pdaUser.name

    return data


@app.post('/api/delete/{id}')
def delete(id : int):
    res = None
    list = data.get("pdaUsers")
    for item in list:
        if(id == item.get('id')):
            res = list.delete(item)
    return res

