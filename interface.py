import tkinter as tk
from button_commands import ButtonCommands

class Interface(tk.Frame):
        
    def createLabels(self):
        self.newTaskLabel = tk.Label(self, text = "Add new task here!")
        self.newTaskLabel.grid(column = 0, row = 0)
        self.TitleToDoTaskLabel = tk.Label(self, text = "To-Do:")
        self.TitleToDoTaskLabel.grid(row = 0, column = 3)
        self.TitleCompletedTaskLabel = tk.Label(self, text = "Completed:")
        self.TitleCompletedTaskLabel.grid(row = 0, column = 4)

    def createEntries(self):
        self.writeEntry = tk.Entry(self)
        self.writeEntry.grid(row = 0, column = 1, columnspan = 2)

    def createButtons(self):
        self.AddingButton = tk.Button(self, text = "Add new task", command = \
            lambda:[ButtonCommands.add_new_task(self,taskbox = self.ToDoTaskBox, entry = self.writeEntry)])
        self.AddingButton.grid(row = 1, column = 1)
        self.DeletingTaskButton = tk.Button(self, text = "Delete this task", command = \
            lambda:[ButtonCommands.delete_task(self, taskbox = self.ToDoTaskBox)])
        self.DeletingTaskButton.grid(row = 1, column = 2)
        self.MarkingCompleteTaskButton = tk.Button(self, text = "Complete task", command = \
            lambda:[ButtonCommands.complete_task(self, ct_taskbox = self.CompletedTaskBox, td_taskbox = self.ToDoTaskBox)])
        self.MarkingCompleteTaskButton.grid(row = 2, column = 3)

    def createListboxes(self):
        self.ToDoTaskBox = tk.Listbox(self)
        self.ToDoTaskBox.grid(row = 1, column = 3)
        self.CompletedTaskBox = tk.Listbox(self)
        self.CompletedTaskBox.grid(row = 1, column = 4)

    def createWidgets(self):
        self.createLabels()
        self.createEntries()
        self.createButtons()
        self.createListboxes()

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
