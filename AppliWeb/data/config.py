def chemin():
    return "/IENAC/template_final"

def configBD():
    config = {
        'user': 'ienac',
        'password': 'ienac',
        'host': 'localhost',
        'port':'80',
        'database': 'bd_test',
        'raise_on_warnings': True
    }
    return config