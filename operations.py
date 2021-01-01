import main as crd 
crd.create("pawan",28)
crd.create("pp",70,3600) 
crd.read("pawan")
crd.read("pp")
crd.create("pawan",50) #it throws an ERROR since the key already exists in the db
crd.modify("pawan",55)
crd.delete("pawan")
# it can be access through thread
thrd1=Thread(target=(create or read or delete),args=(key,value,t_out))
thrd1.start()
thrd1.sleep()
thrd2=Thread(target=(create or read or delete),args=(key,value,t_out))
thrd2.start()
thrd2.sleep()
thrd3=Thread(target=(create or read or delete),args=(key,value,t_out))
thrd3.start()
thrd3.sleep()
