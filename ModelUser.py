from entities.User import User
class ModelUser():

    @classmethod
    def login(self,db,user):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT ID_USUARIO,CORREO_SOLVO,CONTRASENA,ID_SOLVO,NOMBRES,APELLIDOS,ESTADO,PERFIL,ID_SUPERVISOR,ID_COMPANIA,ID_CIUDAD FROM usuario 
                    WHERE CORREO_SOLVO = '{}'""".format(user.correo_solvo)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                compania=ModelUser.get_by_id_compania(db,row[9])
                ciudad=ModelUser.get_by_id_ciudad(db,row[10])
                user = User(row[0], row[1],compania,ciudad, User.check_password(row[2], user.contrasena), row[3],row[4],row[5],row[6],row[7],row[8])
                return user
            else:
                return None
        except Exception as ex: 
            raise Exception(ex)
        
    @classmethod
    def ExistsUser(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT CORREO_SOLVO FROM usuario 
                    WHERE CORREO_SOLVO = '{}'""".format(user.correo_solvo)        
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                user = User(0,row[0],None,None)
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)



        
    @classmethod
    def get_by_id_compania(self,db,idCC):
        try:
            compania={}
            cursor = db.connection.cursor()
            sql = """select * from compania where id_compania={}""".format(idCC)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                compania={'id':row[0],'nombre':row[1]}
                return compania
            else:
                return compania
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def get_by_id_ciudad(self,db,idCC):
        try:
            ciudad={}
            cursor = db.connection.cursor()
            sql = """select * from ciudad where id_ciudad={}""".format(idCC)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                ciudad={'id':row[0],'nombre':row[1]}
                return ciudad
            else:
                return ciudad
        except Exception as ex:
            raise Exception(ex)
        

