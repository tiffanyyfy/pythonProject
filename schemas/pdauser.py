from pydantic import BaseModel, Field


class PdaUserSchema(BaseModel):
    id : int
    gsid : int
    glybh : None | str = 'code-001'
    zsmc : None | str = ''
    dlmc : None | str = ''
    dlmm : None | str = ''
    mmyz : None | str = ''
    yhlx : int

    class Config:
        from_attributes = True
class PdaUserUpdateSchema(PdaUserSchema):
    '''
    用于更新
    '''
    pass


class PdaUserSelectSchema(PdaUserSchema):
    pass