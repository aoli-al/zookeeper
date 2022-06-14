from kazoo.client import KazooClient

zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()


transaction = zk.transaction()
transaction.commit()

zk.stop()