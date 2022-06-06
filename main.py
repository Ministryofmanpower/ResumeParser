from flask import Flask,render_template,request
from func import fin

import os


app=Flask(__name__,static_folder="history")
APP_ROOT=os.path.dirname(os.path.abspath(__file__))


@app.route('/',methods=['GET'])
def homepage():
    return render_template('upload.html')

@app.route('/complete',methods=['POST'])
def upload():
    if request.method == 'POST':
        tar=os.path.join(APP_ROOT,'history/')
        print(tar)
        if not os.path.isdir(tar):
            os.mkdir(tar)
        for file in request.files.getlist('file'):
            filename=file.filename
            destination="/".join([tar,filename])
            print(destination,"my destination")
            file.save(destination)
            data = fin(destination)
            print("the data type is here")
            print(type(data))
            values = []
            keyss = []
            for i in data.items():
                keyss.append(i[0])
                values.append(i[1])
            final_value = (tuple(values))
            final_keyss = tuple(keyss)
            print(final_keyss,"here are the keys")
            print(final_value,"here are the values")

        return render_template("form.html",final_keyss = final_keyss,final_value = final_value)
    else: 
        return "Something Went Wrong"



if __name__=='__main__':
    app.run(debug=True)