from src import dbsingleton, config, addressdao, clientdao

dao = addressdao.AddressDAO(0, "Ankh-Morkpork", "Palacum", "1", None)

addressdao.AddressDAO.create(dao)