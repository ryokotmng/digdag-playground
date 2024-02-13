class MyWorkflow(object):
    def my_task(self, arg: str) -> str:
        print('Running my_task')
        print(arg)
        # digdag.env.store({'my_task': arg})