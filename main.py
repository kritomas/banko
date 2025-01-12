from src import dbsingleton, config, clientdao

dao = clientdao.ClientDAO(0, 1, "kritomas", "xd", "kritomas@mail.com", "123456789")

clientdao.ClientDAO.create(dao)