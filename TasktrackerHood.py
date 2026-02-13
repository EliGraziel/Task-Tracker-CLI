from datetime import datetime
import json
import shelve
import os

# Global variables
time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Assign of task_ids to each task, never repeat an id. 
def assign_id():
    with shelve.open('_id_') as db:
        _id = db.get('_id_',-1)
        _id += 1
        db['_id_'] = _id
        return _id 

    """ To restart the memory, just delete the file
    what happpens:
        starts from -1: Hence the generated id starts from 0.
    """

# Read the json file, Load Data to Variable to contain the list of tasks (in form of dictionaries). 
def read_json():
    with open(file='task.json', mode='r', encoding='utf-8') as L:
        read_jsonData = json.load(L)
        return read_jsonData
        
# Add new task to the latest version of the list of tasks (in form of dictionaries).
def Add_to_list(new_task):
    nes = read_json()
    nes.extend(new_task)
    return nes

# Write the latest version of the list of tasks (in form of dictionaries) to a json file.
def write_json(latest_list):
    with open(file="task.json", mode='w', encoding= 'utf-8') as t:
        json.dump(latest_list,t,indent=4)

# Provide the index of the task dictionary required for other functions.
def return_index(id_provided):
    collect = []
    for index, task_dict in enumerate(read_json()):
        id_found = next(iter(task_dict))
        if id_found == id_provided:
            collect.append(id_found)
            return index
    if id_provided not in collect:
        return 'Bro, the ID you provided was not found! :('

# Provide the indices of the task dictionaries required for other functions.
def return_indices(status_queried):
    list_indices = []
    for index, tas_dic in enumerate(read_json()):
        key = next(iter(tas_dic))
        nested_dic = tas_dic.get(key)
        if nested_dic['status'] ==  status_queried:
            list_indices.append(index)
    return list_indices
            
# Object for Task 
class Task:
    def __init__(self,task_placeholder, _id_=assign_id(),status = 'not-started',time_of_creation = time_now,time_of_update = None ):
        self.task_id = _id_
        self.task_description = task_placeholder
        self.status = status
        self.createdAt = time_of_creation
        self.updatedAt = time_of_update
        
# Methods
    #Converts the object's attributes to a list.
    def construct_task(self):
        return [
            {
                self.task_id:{
                    "task description":self.task_description,
                    "status":self.status,
                    "create time": self.createdAt,
                    "update time": self.updatedAt
                }
            }
        ]
        
    # Add a task to the list of task dictionaries.
    def Add_task(self):     
        if not os.path.exists('task.json'):
            write_json(self.construct_task())
        else:
            write_json(Add_to_list(self.construct_task()))
        #print(self.construct_task())
        print(f"TASK SUCCESSFULLY SAVED AS ID:{self.task_id}")
                
# Update task description of specific task in the list of task dictionaries.
def update_task_description(task_id,updated_description):
    if isinstance(return_index(task_id),int):
        _ID_= next(iter(read_json()[return_index(task_id)]))
        nested_dictionary = read_json()[return_index(task_id)].get(_ID_)
        _taskObject = Task(_id_=_ID_,
                            task_placeholder=updated_description,
                            status=nested_dictionary['status'],
                            time_of_creation=nested_dictionary['create time'],
                            time_of_update= time_now)
        updated_task = _taskObject.construct_task()
        task_history = read_json()
        task_history[return_index(task_id)] = updated_task[0]
        write_json(task_history)
        #print(updated_task[0])
        print(f'Task:{nested_dictionary['task description']} updated to --> {updated_description}')
        
    elif isinstance(return_index(task_id),str):
        print(f'id provided: {task_id}|data type: {type(task_id)}')
        print(return_index(task_id))
        
    else: 
        print(f"Oops what went wrong!:\nDetails\nargument datatype :{type(task_id)}\nindex datatype: {type(return_index(task_id))}\nindex: {return_index(task_id)}")
    
# Delete a task from list of the tasks, provide the task_id.
def delete_task(task_id):
    if isinstance(return_index(task_id),int):
        _idtask= next(iter(read_json()[return_index(task_id)]))
        nested_dictionary = read_json()[return_index(task_id)].get(_idtask)
        tasks_json = read_json()
        del tasks_json[return_index(task_id)]
        write_json(tasks_json)
        print(f"The task:{nested_dictionary['task description']} has been successfully deleted!")
    elif isinstance(return_index(task_id),str):
        print(f'id provided: {task_id}|data type: {type(task_id)}')
        print(return_index(task_id))
        
    else:
        print("Oops what went wrong!")

# Update the task status in list of the tasks, provide the task_id.        
def Update_status(task_status,task_id):
    if isinstance(return_index(task_id),int):
        _idt= next(iter(read_json()[return_index(task_id)]))
        nested_ = read_json()[return_index(task_id)].get(_idt)
        _taskOb = Task(_id_=_idt,
                            task_placeholder=nested_['task description'],
                            status=task_status,
                            time_of_creation=nested_['create time'],
                            time_of_update= nested_['update time'])
        changedstatus = _taskOb.construct_task()
        task_hist = read_json()
        task_hist[return_index(task_id)] = changedstatus[0]
        write_json(task_hist)
        print(f'Task:{nested_['task description']} status updated to : {task_status} ')
        #print(changedstatus[0])

    elif isinstance(return_index(task_id),str):
        print(f'id provided: {task_id}|data type: {type(task_id)}')
        print(return_index(task_id))
        
    else:
        print("Oops what went wrong!")

# list all tasks, whose status is done! 
def list_done():
    indices_done = return_indices('done')
    for index in indices_done:
        taskidentity = next(iter(read_json()[index]))
        nested_details = read_json()[index].get(taskidentity)
        taskdescription = nested_details['task description']
        print(f'ID:{taskidentity}      |     Task:{taskdescription}')
    
# list all tasks, whose status is in progress! 
def list_in_progress():
    indices_in_progress = return_indices('in-progress')
    for index in indices_in_progress:
        taskidentity = next(iter(read_json()[index]))
        nested_details = read_json()[index].get(taskidentity)
        taskdescription = nested_details['task description']
        print(f'ID:{taskidentity}    |      Task:{taskdescription}')
    
# list all tasks, whose status is in progress! 
def list_not_started():
    indices_not_started = return_indices('not-started')
    for index in indices_not_started:
        taskidentity = next(iter(read_json()[index]))
        nested_details = read_json()[index].get(taskidentity)
        taskdescription = nested_details['task description']
        print(f'ID:{taskidentity}     |     Task:{taskdescription}')

# list all tasks    
def list_all():
    nev = read_json()
    for tas_dic in nev:
        taskidentity = next(iter(tas_dic))
        nested_details = tas_dic.get(taskidentity)
        taskdescription = nested_details['task description']
        print(f'ID:{taskidentity}      |          Task:{taskdescription}')



# ================================================================================= THE END ===================================================================================
# CREDITS:  Eli_Graziel 
# This was not vibe coded, all code here was written from scratch !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



