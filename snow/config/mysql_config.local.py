db_config = {
    'local': {
        'host': "127.0.0.1", 'port': 3306,
        'user': "root", 'passwd': "111111",
        'db': "snow", 'charset': "utf8",
        'pool': {
            # use = 0 no pool else use pool
            "use":0,
            # size is >=0,  0 is dynamic pool
            "size":10,
            # pool name
            "name":"local",
        }
    }
  
}
