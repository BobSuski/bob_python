import sys, pickle
sys.path.insert(0, '../../src')

from  properties import properties
from helper.connection_manager import ConnectionManager
from helper import commons
from dao.personDAO import PersonDAO
from entity.person import Person



with open("c:\\git_python\\bob_python\8\\CEPIK\src\\database\\person.dat","+rb") as file:
    d=pickle.load(file)
    #d=pickle.load(file)
    print(d.name)