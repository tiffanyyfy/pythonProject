from typing import Type, Any

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from db.models import PdaUser
from schemas.pdauser import PdaUserUpdateSchema


class CrudPdaUser:
    def __init__(self, model: Type[PdaUser]):
        self.model = model

    def getById(self, id: Any, db: Session):
        return db.query(self.model).filter(self.model.id == id).first()

    def save(self, db: Session, *, obj_in: PdaUserUpdateSchema) -> PdaUser:
        obj_in_data = jsonable_encoder(obj_in)  #转换成字典
        pda_user_obj = self.model(**obj_in_data)  # 解包字典操作，生成对象
        db.add(pda_user_obj)
        db.commit()
        db.refresh(pda_user_obj)
        return pda_user_obj

    def updateById(self,db: Session, *, id: int, obj_update: PdaUserUpdateSchema) -> PdaUser:
        pdaUser = db.query(self.model).filter(self.model.id == id).first()
        if (pdaUser is None or pdaUser.id == 0):
            print("更新失败，根据id未查到需要更新的对象")
            return None
        pda_user_dict = jsonable_encoder(pdaUser)
        if(isinstance(obj_update, dict)):
            update_obj = obj_update
        else:
            update_obj = obj_update.model_dump(exclude_unset=True)
        for field in pda_user_dict:
            if field in update_obj:
                setattr(pdaUser, field, update_obj[field])
        db.add(pdaUser)
        db.commit()
        db.refresh(pdaUser)
        return pdaUser

pdaUser = CrudPdaUser(PdaUser)
