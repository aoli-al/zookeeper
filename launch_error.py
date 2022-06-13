import subprocess
import os
import shutil
import time

SRC_DIR = os.path.dirname(os.path.realpath(__file__))


def prepare(idx):
    base = f"/tmp/zk{idx}"
    shutil.rmtree(base, True)
    os.mkdir(base)
    with open(os.path.join(base, "myid"), "w") as f:
        f.write(str(idx))
    shutil.copytree(os.path.join(SRC_DIR, "conf"), os.path.join(base, "conf"))
    with open(os.path.join(base, "conf", "zoo.cfg"), "a+") as f:
        f.write(f"dataDir={base}\n")
        f.write(f"clientPort=218{idx}\n")

    with open(os.path.join(base, "conf", "log4j.properties"), "a+") as f:
        f.write(f"zookeeper.log.dir={base}\n")

    command = ["bash", "./bin/zkServer.sh", "--config", os.path.join(base, "conf"), "start"]
    subprocess.call(command, env={
        "ZOO_LOG4J_PROP": os.path.join(base, "conf", "log4j.properties"),
        "ZOO_LOG_DIR": base
    })


def start():
    for i in range(1, 4):
        prepare(i)

    time.sleep(5)


if __name__ == "__main__":
    start()
