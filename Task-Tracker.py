# CLI structure to handle user inputs.

import argparse
from TasktrackerHood import Task,update_task_description,delete_task,Update_status,list_done,list_in_progress,list_not_started,list_all

def _task(args):
    Object = Task(task_placeholder=args.task_description)
    Object.Add_task()

def _update(args):
    update_task_description(task_id=args._id_update,updated_description=args.updated_description)
    
def _delete(args):
    delete_task(args._id_delete)
    
def _inprogress(args):
    Update_status('in-progress',args.id_mark)

def _done(args):
    Update_status('done',args.id_done)

def _listall(args):
    list_all()

def _listinprogress(args):
    list_in_progress()

def _listnotstarted(args):
    list_not_started()

def _listdone(args):
    list_done()

# Parser    
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

#Sub_parser Delete Command
delete_praser = sub_parser.add_parser("delete",help="Deletes Task Description to Task tracker memory")
delete_praser.add_argument('_id_delete',type=str,help="provide the task_id to delete task")
# The default function to call
delete_praser.set_defaults(func=_delete)

# Sub_parser mark-in-progress Command
markinprogress_praser = sub_parser.add_parser("mark-in-progress",help="change status of Task to in progress in the Task tracker memory")
markinprogress_praser.add_argument('id_mark',type=str,help="provide task id to update status of the task")
# The default function to call
markinprogress_praser.set_defaults(func=_inprogress)

# Sub_parser mark-done Command
markdone_praser = sub_parser.add_parser("mark-done",help="change status of Task to done in the Task tracker memory")
markdone_praser.add_argument('id_done',type=str,help="provide task id to update status of the task")
# The default function to call
markdone_praser.set_defaults(func=_done)

# Sub_parser list Command
listall_praser = sub_parser.add_parser("list",help="change status of Task to in progress in the Task tracker memory")
# The default function to call
listall_praser.set_defaults(func=_listall)

# Sub_parser list not-started Command
listnotstarted_praser = sub_parser.add_parser("list not-started",help="List all tasks whose status is in-progress in the Task tracker memory")
# The default function to call
listnotstarted_praser.set_defaults(func=_listnotstarted)

# Sub_parser list in-progress Command
listinprogress_praser = sub_parser.add_parser("list in-progress",help="change status of Task to in progress in the Task tracker memory")
# The default function to call
listinprogress_praser.set_defaults(func=_listinprogress)

# Sub_parser list done Command
listdone_praser = sub_parser.add_parser("list done",help="change status of Task to in progress in the Task tracker memory")
# The default function to call
listdone_praser.set_defaults(func=_listdone)

# Parse the arguments 
args = parser.parse_args()
args.func(args)

