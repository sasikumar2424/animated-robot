#!/usr/bin/env python
# coding: utf-8

# In[6]:


from tkinter import*


# In[7]:


root = Tk()
root.geometry('500x500')
root.title("Registration Form")


# In[8]:


label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)
label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
label_1.place(x=80,y=130)
entry_1 = Entry(root)
entry_1.place(x=240,y=130)
label_2 = Label(root, text="Email",width=20,font=("bold", 10))
label_2.place(x=68,y=180)
entry_2 = Entry(root)
entry_2.place(x=240,y=180)
label_3 = Label(root, text="Phone",width=20,font=("bold", 10))
label_3.place(x=70,y=230)
entry_3 = Entry(root)
entry_3.place(x=240,y=230)
label_4 = Label(root, text="Description",width=20,font=("bold", 10))
label_4.place(x=70,y=280)
entry_4 = Entry(root)
entry_4.place(x=240,y=280)


# In[9]:


Button(root, text='Submit',width=20,bg='brown',fg='white').place(x=180,y=380)
root.mainloop()


# In[ ]:




