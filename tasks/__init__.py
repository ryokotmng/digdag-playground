import digdag

class MyWorkflow(object):
    def my_task(self, arg, nested, who):
        print('Running my_task')
        print(arg)
        print("nested: "+nested)
        digdag.env.store({'my_task': arg})
        digdag.env.store({'who': who})
        digdag.env.store({'arg': arg})

    def my_second_task(self, my_task, arg, who):
        print('Running my_second_task')
        print(my_task)
        print(arg)
        print(who)
        print(digdag.env.params['my_task'])
