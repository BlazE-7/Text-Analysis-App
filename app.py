from tkinter import *
from my_database import Database
from tkinter import messagebox
from my_api import sentiment, emotion, ner


class NLPApp:

    def __init__(self):

        self.sentiment_input = None
        self.sentiment_output = None

        self.ner_input = None
        self.ner_output = None

        self.emotion_input = None
        self.emotion_output = None

        self.payload = None

        self.dbo = Database()

        self.email_input = None
        self.name_input = None
        self.password_input = None

        self.root = Tk()
        self.root.title('Text Analysis App')
        self.root.geometry('1000x750')
        self.root.iconbitmap('Resources/favicon.ico')
        self.root.configure(bg='#000000')
        self.login_gui()

        self.root.mainloop()

    # login GUI
    def login_gui(self):

        self.clear()

        # heading
        heading = Label(self.root, text='Text Analysis App', bg='#000000', fg='white')
        heading.pack(pady=(50, 70))
        heading.configure(font=('verdana', 50, 'bold'))

        # email label
        label1 = Label(self.root, text='Enter Email:', bg='#000000', fg='white')
        label1.pack(pady=(20, 3))
        label1.configure(font=('Helvetica', 15, 'bold'))

        # email input box
        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5, 10), ipady=3)

        # password label
        label2 = Label(self.root, text='Enter Password:', bg='#000000', fg='white')
        label2.pack(pady=(20, 3))
        label2.configure(font=('Helvetica', 15, 'bold'))

        # password input
        self.password_input = Entry(self.root, width=50, show='*')
        self.password_input.pack(pady=(5, 20), ipady=3)

        # login button
        login_btn = Button(self.root, text='Login', width=10, height=2, command=self.perform_login)
        login_btn.configure(font=('Helvetica', 10, 'bold'))
        login_btn.pack(pady=(20, 10))

        # asking member or not
        label3 = Label(self.root, text='Not a member?', bg='#000000', fg='white')
        label3.pack(pady=(50, 3))
        label3.configure(font=('Helvetica', 10, 'bold'))

        # registration button
        register_btn = Button(self.root, text='Register Now', width=13, height=2, command=self.register_gui)
        register_btn.configure(font=('Helvetica', 8, 'bold'))
        register_btn.pack(pady=(3, 10))

    # clear GUI
    def clear(self):
        for i in self.root.pack_slaves():
            print(i.destroy())

    # registration GUI
    def register_gui(self):

        self.clear()

        # heading
        heading = Label(self.root, text='Text Analysis App', bg='#000000', fg='white')
        heading.pack(pady=(50, 70))
        heading.configure(font=('verdana', 50, 'bold'))

        # name label
        label1 = Label(self.root, text='Enter Name:', bg='#000000', fg='white')
        label1.pack(pady=(20, 3))
        label1.configure(font=('Helvetica', 15, 'bold'))

        # name input box
        self.name_input = Entry(self.root, width=50)
        self.name_input.pack(pady=(5, 10), ipady=3)

        # # email label
        label2 = Label(self.root, text='Enter Email:', bg='#000000', fg='white')
        label2.pack(pady=(20, 3))
        label2.configure(font=('Helvetica', 15, 'bold'))

        # email input box
        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5, 10), ipady=3)

        # password label
        label3 = Label(self.root, text='Enter Password:', bg='#000000', fg='white')
        label3.pack(pady=(20, 3))
        label3.configure(font=('Helvetica', 15, 'bold'))

        # password input
        self.password_input = Entry(self.root, width=50, show='*')
        self.password_input.pack(pady=(5, 20), ipady=3)

        # registration button
        registration_btn = Button(self.root, text='Register', width=10, height=2, command=self.perform_registration)
        registration_btn.configure(font=('Helvetica', 10, 'bold'))
        registration_btn.pack(pady=(20, 10))

        # asking already a member?
        label4 = Label(self.root, text='Already a member?', bg='#000000', fg='white')
        label4.pack(pady=(50, 3))
        label4.configure(font=('Helvetica', 10, 'bold'))

        # login button
        redirect_btn = Button(self.root, text='Login Now', width=13, height=2, command=self.login_gui)
        redirect_btn.configure(font=('Helvetica', 8, 'bold'))
        redirect_btn.pack(pady=(3, 10))

    # registration process
    def perform_registration(self):

        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.add_data(name, email, password)

        if response:
            messagebox.showinfo('Success', 'Registration Successful!!!  You can Login now')
        else:
            messagebox.showerror('Error', 'Email already exists')

    # login button process
    def perform_login(self):

        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.search(email, password)

        if response:
            messagebox.showinfo('Success', 'Login Successful!!!')
            self.home_gui()
        else:
            messagebox.showerror('Error', 'Incorrect email or password')

    # home page GUI
    def home_gui(self):

        self.clear()

        # heading
        heading = Label(self.root, text='Text Analysis App', bg='#000000', fg='white')
        heading.pack(pady=(50, 70))
        heading.configure(font=('verdana', 50, 'bold'))

        # sentiment analysis button
        sentiment_btn = Button(self.root, text='Sentiment Analysis', width=30, height=4, command=self.sentiment_gui)
        sentiment_btn.configure(font=('Helvetica', 12, 'bold'))
        sentiment_btn.pack(pady=(20, 20))

        # ner analysis button
        ner_btn = Button(self.root, text='Named Entity Recognition (NER)', width=30, height=4, command=self.ner_gui)
        ner_btn.configure(font=('Helvetica', 12, 'bold'))
        ner_btn.pack(pady=(20, 20))

        # emotion analysis button
        emotion_btn = Button(self.root, text='Emotion Prediction', width=30, height=4, command=self.emotion_gui)
        emotion_btn.configure(font=('Helvetica', 12, 'bold'))
        emotion_btn.pack(pady=(20, 20))

        # logout button
        logout_btn = Button(self.root, text='Logout', width=13, height=2, command=self.login_gui)
        logout_btn.configure(font=('Helvetica', 10, 'bold'))
        logout_btn.pack(pady=(40, 10))

    # sentiment analysis GUI
    def sentiment_gui(self):

        self.clear()

        # heading
        heading = Label(self.root, text='Text Analysis App', bg='#000000', fg='white')
        heading.pack(pady=(50, 70))
        heading.configure(font=('verdana', 50, 'bold'))

        # sentiment heading
        heading = Label(self.root, text='Sentiment Analysis', bg='#000000', fg='white')
        heading.pack(pady=(10, 10))
        heading.configure(font=('verdana', 40))

        # enter text label
        label1 = Label(self.root, text='Enter The Text:', bg='#000000', fg='white')
        label1.pack(pady=(40, 3))
        label1.configure(font=('Helvetica', 15, 'bold'))

        # enter input text
        self.sentiment_input = Entry(self.root, width=80)
        self.sentiment_input.pack(pady=(5, 20), ipady=3)

        # analysis button
        sentiment_analyse_btn = Button(self.root, text='Analyse', width=20, height=2,
                                       command=self.do_sentiment_analysis)
        sentiment_analyse_btn.configure(font=('Helvetica', 12, 'bold'))
        sentiment_analyse_btn.pack(pady=(20, 20))

        # output label
        label2 = Label(self.root, text='Output:', bg='#000000', fg='white')
        label2.pack(pady=(20, 20))
        label2.configure(font=('Helvetica', 15, 'bold'))

        # sentiment analysis output
        self.sentiment_output = Label(self.root, text='', bg='#000000', fg='white')
        self.sentiment_output.pack(pady=(10, 10))
        self.sentiment_output.configure(font=('Helvetica', 15))

        # go back button
        back_btn = Button(self.root, text='Go Back', width=20, height=2, command=self.home_gui)
        back_btn.configure(font=('Helvetica', 12, 'bold'))
        back_btn.pack(pady=(10, 10))

    # fetching input data
    def do_sentiment_analysis(self):
        text = self.sentiment_input.get()
        result = sentiment(text)
        self.sentiment_output['text'] = result

    # ner analysis GUI
    def ner_gui(self):

        self.clear()

        # heading
        heading = Label(self.root, text='Text Analysis App', bg='#000000', fg='white')
        heading.pack(pady=(50, 70))
        heading.configure(font=('verdana', 50, 'bold'))

        # sentiment heading
        heading = Label(self.root, text='NER Analysis', bg='#000000', fg='white')
        heading.pack(pady=(10, 10))
        heading.configure(font=('verdana', 40))

        # enter text label
        label1 = Label(self.root, text='Enter The Text:', bg='#000000', fg='white')
        label1.pack(pady=(40, 3))
        label1.configure(font=('Helvetica', 15, 'bold'))

        # enter input text
        self.ner_input = Entry(self.root, width=80)
        self.ner_input.pack(pady=(5, 20), ipady=3)

        # analysis button
        ner_analyse_btn = Button(self.root, text='Analyse', width=20, height=2, command=self.do_ner_analysis)
        ner_analyse_btn.configure(font=('Helvetica', 12, 'bold'))
        ner_analyse_btn.pack(pady=(20, 20))

        # output label
        label2 = Label(self.root, text='Output:', bg='#000000', fg='white')
        label2.pack(pady=(20, 20))
        label2.configure(font=('Helvetica', 15, 'bold'))

        # sentiment analysis output
        self.ner_output = Label(self.root, text='', bg='#000000', fg='white')
        self.ner_output.pack(pady=(20, 20))
        self.ner_output.configure(font=('Helvetica', 15))

        # go back button
        back_btn = Button(self.root, text='Go Back', width=20, height=2, command=self.home_gui)
        back_btn.configure(font=('Helvetica', 12, 'bold'))
        back_btn.pack(pady=(20, 20))

    # fetching input data
    def do_ner_analysis(self):
        text = self.ner_input.get()
        ner(text)

    # emotion analysis GUI
    def emotion_gui(self):

        self.clear()

        # heading
        heading = Label(self.root, text='Text Analysis App', bg='#000000', fg='white')
        heading.pack(pady=(50, 70))
        heading.configure(font=('verdana', 50, 'bold'))

        # emotion heading
        heading = Label(self.root, text='Emotion Prediction', bg='#000000', fg='white')
        heading.pack(pady=(10, 10))
        heading.configure(font=('verdana', 40))

        # enter text label
        label1 = Label(self.root, text='Enter The Text:', bg='#000000', fg='white')
        label1.pack(pady=(50, 3))
        label1.configure(font=('Helvetica', 15, 'bold'))

        # enter input text
        self.emotion_input = Entry(self.root, width=80)
        self.emotion_input.pack(pady=(5, 20), ipady=3)

        # analysis button
        emotion_analyse_btn = Button(self.root, text='Analyse', width=20, height=2,
                                     command=self.do_emotion_analysis)
        emotion_analyse_btn.configure(font=('Helvetica', 12, 'bold'))
        emotion_analyse_btn.pack(pady=(20, 20))

        # output label
        label2 = Label(self.root, text='Output:', bg='#000000', fg='white')
        label2.pack(pady=(20, 20))
        label2.configure(font=('Helvetica', 15, 'bold'))

        # emotion analysis output
        self.emotion_output = Label(self.root, text='', bg='#000000', fg='white')
        self.emotion_output.pack(pady=(20, 20))
        self.emotion_output.configure(font=('Helvetica', 15))

        # go back button
        back_btn = Button(self.root, text='Go Back', width=20, height=2, command=self.home_gui)
        back_btn.configure(font=('Helvetica', 12, 'bold'))
        back_btn.pack(pady=(20, 20))

    # fetching input data
    def do_emotion_analysis(self):
        text = self.emotion_input.get()
        emotion(text)


if __name__ == "__main__":
    nlp = NLPApp()
    nlp.do_sentiment_analysis()
    nlp.do_ner_analysis()
    nlp.do_emotion_analysis()

# if __name__ == "__main__":
#     nlp = NLPApp()
#
#
# if __name__ == "__main__":
#     nlp = NLPApp()


nlp = NLPApp()
