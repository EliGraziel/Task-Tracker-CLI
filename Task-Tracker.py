import argparse
from TasktrackerHood import Task,update_task_description

def _task(args):
    Object = Task(task_placeholder=args.task_description)
    Object.Add_task()

def _update(args):
    update_task_description(task_id=args._id_update,updated_description=args.updated_description)
    
'''def _delete(args):
    task_object.delete_task(task_num=args._id_delete)'''

# Parse     
parser = argparse.ArgumentParser(prog='Task-Tracker-CLI',
description="A simple command line interface (CLI) to track what you need to do, what you have done, and what you are currently working on")
sub_parser = parser.add_subparsers(dest='command', required=True)

# Sub_parser Add Command
add_praser = sub_parser.add_parser("add",help="Adds Task Description to Task tracker memory")
add_praser.add_argument('task_description',type=str,help="Add a short task description to track")
# The default function to call
add_praser.set_defaults(func=_task)

# Sub_parser Update Command
update_praser = sub_parser.add_parser("update",help="Updates Task Description to Task tracker memory")
update_praser.add_argument('updated_description',type=str,help="Provide task_id & the task description update")
update_praser.add_argument('_id_update', type= str,help="Provide task_id & the task description update")
# The default function to call
update_praser.set_defaults(func=_update)

''''# Sub_parser Delete Command
delete_praser = sub_parser.add_parser("delete",help="Deletes Task Description to Task tracker memory")
delete_praser.add_argument('_id_delete',type=str,help="provide the task_id to delete task")
# The default functiob to call
delete_praser.set_defaults(func=_delete)'''

# Parse the arguments 
args = parser.parse_args()
args.func(args)

