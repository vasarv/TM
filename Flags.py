class Flags:
    def __init__(self):
        self.add_rec = False
        self.del_rec = False
        self.edit_rec = False

    def change_flags(self, flag):
        if flag =='add':
            self.add_rec = True if not self.add_rec else False
        
        if flag == 'del':
            self.del_rec = True if not self.del_rec else False
        
        if flag == 'edit':
            self.edit_rec = True if not self.edit_rec else False