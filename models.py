
#User class that sets username and resets password
class User:

    def __init__(self, user_name, password, user_id):
        self.user_name = user_name
        self.password = password
        self.user_id = user_id
        self.users = {}

    def get_username(self, user_id):
        print(user_id)

    def set_username(self, user_id):
        print(user_id)

    def reset_password(self, user_id):
        print(user_id)


class Question:
    """This class defines methods that post, get and delete questions. Note that they just print out
    the question id"""
    def __init__(self, quiz_id, description, date_created, date_modified, user_id):
        self.quiz_id = quiz_id
        self.description = description
        self.date_created = date_created
        self.date_modified = date_modified
        self.user_id = user_id

    def post_question(self, quiz_id):
        print(quiz_id)

    def get_question(self, quiz_id):
        print(quiz_id)

    def get_all_questions(self, quiz_id):
        print(quiz_id)


class Answer:
    """This class defines methods that get, post, delete and accept answers. All the methods defined here are dummies
    functionality will be added fully later"""
    def __init__(self, answ_id, quiz_id, title, description, date_created, date_modified):
        self.ans_id = answ_id
        self.quiz_id = quiz_id
        self.title = title
        self.description = description
        self.date_created = date_created
        self.date_modified = date_modified

    def get_answers(self, quiz_id):
        return quiz_id

    def post_answers(self, quiz_id):
        return quiz_id

    def accept_answers(self, quiz_id, answ_id):
        return quiz_id

    def delete_answers(self,quiz_id, answ_id):
        return answ_id

#admin inherits User class and also has method create_account
class Admin(User):

    def __init__(self, username, password):
        super(Admin, self).__init__(username, password)

    def create_account(self, username, password):
        return username


if __name__ == "main":
    user = User("Joan ", "Ngugi", "1")
    admin = Admin("JNgugi", "@254Kenya")

    admin.reset_password("1")
    user.post_answers(1)
    user.get_answers()
    admin.get_all_questions()



