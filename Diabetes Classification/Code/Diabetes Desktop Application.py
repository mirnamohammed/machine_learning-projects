from tkinter import *
import joblib
models = joblib.load(r"E:\machine_projects\Diabetes Classification\Code\diabetes3.joblib")
p=[]
result= None
def pred():
    global p
    global result
    p = []
    p = [txt2.get(), txt3.get(), txt4.get(), txt5.get(), txt6.get(),txt7.get()]
    #l2 = txt2.get()
    #l3 = txt3.get()
    #l4 = txt4.get()
    #l5 = txt5.get()
    #l6 = txt6.get()
    #l7 = txt7.get()
    #p=[l2,l3,l4,l5,l6,l7]
    prediction = models.predict([p])
    result = prediction
  
    if (result==1):
        txt8.config(text="Diabees True",font=("arial",15))

    else:
        txt8.config(text="Diabetes False",font=("arial",15))

window=Tk()
# window.geometry("1000X1000")
#window.resizable(False,False)
window.config(background="#7697A0")
window.title("Diabetes Detection")
labll=Label(window,text="Welcome to Diabetes Detection")
labll.config(foreground="#94B0B7",font=("arial",20))
labl2=Label(window,text="1)Enter your Insulin")
labl2.config(background="#94B0B7",foreground="black",font=("arial",15))
txt2=Entry(window,font=("arial",15))
labl3=Label(window,text="2)Enter your Pregnancies")
txt3=Entry(window,font=("arial",15))
labl3.config(background="#94B0B7",foreground="black",font=("bold",15))
labl4=Label(window,text="3)Enter your Glucose",background="#94B0B7",foreground="black",font=("arial",15))
txt4=Entry(window,font=("arial",15))
labl5=Label(window,text="4)Enter your BMI",background="#94B0B7",foreground="black",font=("arial",15))
txt5=Entry(window,font=("arial",15))
labl6=Label(window,text="5)Enter your DPF",background="#94B0B7",foreground="black",font=("arial",15))
txt6=Entry(window,font=("arial",15))
label7=Label(window,text="6)enter your age",background="#94B0B7",foreground="black",font=("arial",15))
txt7=Entry(window,font=("arial",15))
label8=Label(window,text="The test result is:",font=("arial",15),background="#94B0B7")
txt8=Label(window,font=("arial",15))
label9=Label(window,text="Developed by Mirna Mohamed......",font=("arial",18),fg="black",background="#7697A0")
labll.place(x=10,y=5)
labl2.place(x=300,y=200)
txt2.place(x=500,y=200)
labl3.place(x=800,y=200)
txt3.place(x=1000,y=200)
labl4.place(x=300,y=300)
txt4.place(x=500,y=300)
labl5.place(x=800,y=300)
txt5.place(x=1000,y=300)
labl6.place(x=300,y=400)
txt6.place(x=500,y=400)
label7.place(x=800,y=400)
txt7.place(x=1000,y=400)

label8.place(x=500,y=550)
txt8.place(x=700,y=550)
label9.place(x=500,y=650)

# txt8.delete(0,"end")
# txt8.insert(END, str(result))
txt8.config(text=result,background="#7697A0")
b =Button(text="click to check diabetes",relief=RIDGE,fg="black",cursor="hand2",activebackground="black",activeforeground="#94B0B7",command=pred)
b.configure(font=("arial",15))
b.place(x=600,y=500)
window.mainloop()    
