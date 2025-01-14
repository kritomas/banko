#from src import dbsingleton, config, addressdao, clientdao
#dao = addressdao.AddressDAO(0, "Ankh-Morkpork", "Palacum", "1", None)
#clientdao.ClientDAO.readByClientNumber("123456")

from src import interface
i = interface.Interface()
i.start()

# mysql-connector-python