class ButtonCommands():
        def add_new_task(self, taskbox, entry):
                if entry.get() != '':
                        taskbox.insert(0, entry.get())
                        entry.delete(0, 'end')
                else:
                        pass
        
        def delete_task(self,taskbox):
                taskbox.delete(taskbox.index('anchor'))

        def complete_task(self, ct_taskbox, td_taskbox):
                if td_taskbox.get(0,'end'):
                        ct_taskbox.insert(0, td_taskbox.get(td_taskbox.index('anchor')))
                        td_taskbox.delete(td_taskbox.index('anchor'))
                        ct_taskbox.selection_clear(0,'end')