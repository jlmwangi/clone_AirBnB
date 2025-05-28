from fabric import task

@task
def hello(c):
    print("Hello from Fabric!")
