#!/usr/bin/env python
# coding: utf-8

# In[29]:


from flask import Flask,request,render_template
import joblib


# In[30]:


app=Flask(__name__)


# In[31]:


@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="POST":
        rates=float(request.form.get("rates"))
        print(rates)
        model=joblib.load("regression")
        r1=model.predict([[rates]])
        model2=joblib.load("tree")
        r2=model2.predict([[rates]])
        return(render_template("index.html",result1=r1,result2=r2))
    else:
        return(render_template("index.html",result1="waiting",result2="waiting"))


# In[32]:


if __name__=="__main__":
    app.run()

