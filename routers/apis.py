from fastapi import APIRouter, Depends

from crud.crud_pdauser import pdaUser
from deps import deps
from deps.deps import get_session
from schemas import pdauser
from schemas.pdauser import PdaUserSelectSchema, PdaUserSchema

router = APIRouter()


@router.get("/api/{id}", response_model=pdauser.PdaUserSelectSchema)
def getPdaUserById(id: int, session=Depends(deps.get_session)):
    data = pdaUser.getById(id=id, db=session)
    if data != None:
        return data
    else:
        return '没有获取数据'

@router.post("/api/save", response_model=PdaUserSelectSchema)
def savePdaUser(pdaUserSchema : PdaUserSchema, session=Depends(deps.get_session)):
    data = pdaUser.save(db=session, obj_in=pdaUserSchema)
    if data != None:
        return data
    else:
        return '保存失败了'