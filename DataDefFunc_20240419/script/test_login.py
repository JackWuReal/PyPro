import sys
sys.path.append("..")

syspath=sys.path
print(syspath)

from DataDefFunc_20240419.service.login_service import login

login('username','123','bbbb')
login('admin','123456','888')
login('99','1456','bbbb')




