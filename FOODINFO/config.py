

db = {
    'user': 'mgrsdp',
    'password': 'ajrrjfl!',
    'host': 'mgrsdp.c8ybdvubh7vg.ap-northeast-2.rds.amazonaws.com',
    'port': 3306,
    'database': 'mgrsdp'
}


db_url = f"mysql+mysqlconnector://{db['user']}:{db['password']}""@" \
         f"{db['host']}:{db['port']}/{db['database']}"