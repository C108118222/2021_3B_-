import pymssql
# 連接SQL
def connectMsSQL():
    db_settings = {
        "server": "Your Server Name",
        "user": "Your account",
        "password": "Your password",
        "database": "Your Database",
        'charset': "utf8",
        'autocommit': True
    }
    try:
        # 建立Connection物件
        conn = pymssql.connect(**db_settings)
        cursor = conn.cursor()
        return cursor
    except Exception as ex:
        print(ex)
