import digdag

class MyWorkflow(object):
    def my_task(self, arg: str, nested: str):
        print('Running my_task')
        print(arg)
        print("nested: "+nested)
        digdag.env.store({'my_task': arg})
        digdag.env.store({'arg': arg})

    def my_second_task(self, my_task, arg, arg2):
        print('Running my_second_task')
        print(my_task)
        print(arg)
        print(arg2)
        print(digdag.env.params['my_task'])
