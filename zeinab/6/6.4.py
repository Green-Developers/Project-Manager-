class UndoRedo:
    def __init__(self):
        self.main_stack = []
        self.redo_stack = []


    #کاراکتر ورودی را به انتهای پشته اضافه میکند
    def type(self, char):
        self.main_stack.append(char)
        self.redo_stack.clear()  # پاک کردن redo پس از هر تغییر جدید


    #اگر پشته اصلی خالی نباشد اخرین عنصر را از پشته اصلی برداشتهو  به redoمنتقل میکنه
    def undo(self):
        if self.main_stack:
            self.redo_stack.append(self.main_stack.pop())


    #اگر پشته redoخالی نباشد اخرین عنصر را از پشته اصلی برداشتهو  به پشته اصلی منتقل میکنه
    def redo(self):
        if self.redo_stack:
            self.main_stack.append(self.redo_stack.pop())

    def get_text(self):
        return ''.join(self.main_stack)


# مثال
editor = UndoRedo()
editor.type('a')
editor.type('b')
print(editor.get_text())  # خروجی: 'ab'
editor.undo()
print(editor.get_text())  # خروجی: 'a'
editor.redo()
print(editor.get_text())  # خروجی: 'ab'