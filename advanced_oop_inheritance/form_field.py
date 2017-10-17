class FormField(object):
    def __init__(self, title, help_text=None):
        self.title = title
        self.help_text = help_text
        self.answer = None

    def submit_answer(self, answer):
        self.answer = answer

    def get_answer(self):
        return self.answer

    def is_valid(self):
        print(self.answer)
        if self.answer:
            return True
        else:
            raise ValueError()


class TextField(FormField):
    pass


class EmailField(FormField):
    def __init__(self, help_text, title=None):
            FormField.__init__(self,title,help_text)

    def submit_answer(self,answer):
        if '@' in answer:
            FormField.submit_answer(self,answer)
        else:
            FormField.is_valid(self)


class URLField(FormField):
    def __init__(self, help_text, title=None):
        FormField.__init__(self,title,help_text)


class MultipleChoiceField(FormField):
    def __init__(self, title, options, help_text=None):
        FormField.__init__(self,title,help_text)
        self.options = options

email_field = EmailField("What's your email?")
email_field.submit_answer('INVALID EMAIL')
assert not email_field.is_valid()
