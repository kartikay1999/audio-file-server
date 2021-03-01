from flask import Flask,request,jsonify,abort
from flask_sqlalchemy import SQLAlchemy
import json
import os
from datetime import datetime

local_server=True

app=Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Songs.sqlite3"
db=SQLAlchemy(app)

#database models
class SONGFILE(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    duration=db.Column(db.Integer,nullable=False)
    upload_time=db.Column(db.DateTime,nullable=False)

    def __init__(self,name,duration,upload_time):
        self.name=name
        self.duration=duration
        self.upload_time=upload_time

class PodcastFile(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    duration=db.Column(db.Integer,nullable=False)
    upload_time=db.Column(db.DateTime,nullable=False)
    host=db.Column(db.String(100),nullable=False)
    participants=db.Column(db.String,nullable=True)
    
    def __init__(self,name,duration,upload_time,host, **kwargs):
        self.name=name
        self.duration=duration
        self.upload_time=upload_time
        self.host=host
        self.participants=kwargs['Participants']



class AudioBook(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    author=db.Column(db.Integer,nullable=False)
    narrator=db.Column(db.Integer,nullable=False)
    host=db.Column(db.String(100),nullable=False)
    duration=db.Column(db.Integer,nullable=False)
    upload_time=db.Column(db.DateTime,nullable=False)
    
    def __init__(self,title,author,narrator,host,duration,upload_time):
        self.title=title
        self.author=author
        self.narrator=narrator
        self.host=host
        self.duration=duration
        self.upload_time=upload_time


#CREATE
@app.route('/create',methods=['POST'])
def create():
    if request.content_type=='application/json':
        file_data=request.get_json()
        if file_data['audioFileType'].lower()=='song':
            print(file_data)
            name=file_data['audioFileMetadata']['Name of the song']
            if file_data['audioFileMetadata']['Duration in number of seconds']<0:
               abort(400)
            else:
                duration=file_data['audioFileMetadata']['Duration in number of seconds']            
            upload_time=datetime.now() 
            query=SONGFILE(name,duration,upload_time)
            db.session.add(query)
            
            
        if file_data['audioFileType'].lower()=='podcast':
            name=file_data['audioFileMetadata']['Name of the song']
            if file_data['audioFileMetadata']['Duration in number of seconds']<0:
               abort(400)
            else:
                duration=file_data['audioFileMetadata']['Duration in number of seconds']        
            upload_time=datetime.now()
            host=file_data['audioFileMetadata']['Host']
            print(file_data)
            if 'Participants' in file_data['audioFileMetadata']:
                participants=','.join(file_data['audioFileMetadata']['Participants'])
                query=PodcastFile(name,duration,upload_time,host,Participants=participants)
            else:
                query=PodcastFile(name,duration,upload_time,host)
            db.session.add(query)

        if file_data['audioFileType'].lower()=='audiobook':
            title=file_data['audioFileMetadata']['Title of the audiobook']
            author=file_data['audioFileMetadata']['Author of the title']
            narrator=file_data['audioFileMetadata']['Narrator']
            host=file_data['audioFileMetadata']['Host']
            if file_data['audioFileMetadata']['Duration in number of seconds']<0:
               abort(400)
            else:
                duration=file_data['audioFileMetadata']['Duration in number of seconds']        
            upload_time=datetime.now()
            query=AudioBook(title,author,narrator,host,duration,upload_time)
            db.session.add(query)
        db.session.commit()
        return "- Action is successful: 200 OK"


#DELETE 
@app.route('/delete/<string:audiofiletype>/<int:sid>',methods=['GET'])
def delete(audiofiletype,sid):
    aft=audiofiletype
    print(aft,sid)

    if aft=="song":
        if SONGFILE.query.filter_by(id=int(sid)).first()==None:
            abort(400)
        else:  
            SONGFILE.query.filter_by(id=int(sid)).delete()
    elif aft=='podcast':
        if PodcastFile.query.filter_by(id=int(sid)).first()==None:
            abort(400)
        PodcastFile.query.filter_by(id=(int(sid))).delete()
    elif aft=='audiobook':
        if AudioBook.query.filter_by(id=int(sid)).first()==None:
            abort(400)
        AudioBook.query.filter_by(id=(int(sid))).delete()
    
    db.session.commit()
    return "Action is successful: 200 OK"

#UPDATE
@app.route('/update/<string:audiofiletype>/<sid>',methods=['POST'])
def update(audiofiletype,sid):
    if request.content_type=='application/json':
        file_data=request.get_json()
        if audiofiletype=='song':
            data=SONGFILE.query.filter_by(id=int(sid)).first()
            if data==None:
                abort(400)
            data.name=file_data['Name of the song']
            if file_data['Duration in number of seconds']<0:
               abort(400)
            else:
                data.duration=file_data['Duration in number of seconds']

            data.upload_time=datetime.now()
            
        if audiofiletype=='podcast':
            data=PodcastFile.query.filter_by(id=int(sid)).first()
            if data==None:
                abort(400)
            data.name=file_data['Name of the song']
            if file_data['Duration in number of seconds']<0:
               abort(400)
            else:
                data.duration=file_data['Duration in number of seconds']
            data.upload_time=str(datetime.now())
            data.host=file_data['Host']
            if 'Participants' in file_data:
                data.participants=file_data['Participants']

            
        if audiofiletype=='audiobook':

            data=AudioBook.query.filter_by(id=int(sid)).first()
            if data==None:
                abort(400)
            data.title=file_data['Title of the audiobook']
            data.author=file_data['Author of the title']
            data.narrator=file_data['Narrator']
            data.host=file_data['Host']
            if file_data['Duration in number of seconds']<0:
               abort(400)
            else:
                data.duration=file_data['Duration in number of seconds']
            data.upload_time=str(datetime.now())
        db.session.commit()
        return "Action is successful: 200 OK"

#GET
@app.route('/get/<audioFileType>/<audioFileID>')
def get(audioFileType,audioFileID):
    if audioFileType=='song':
        song=SONGFILE.query.filter_by(id=int(audioFileID)).first()
        data={"Name of the song":str(song.name),
        "Duration in number of seconds":str(song.duration),
        "Uploaded time":str(song.upload_time)
        }
        return jsonify(data)
    elif audioFileType=='podcast':
        pod=PodcastFile.query.filter_by(id=int(audioFileID)).first()
        data={"Name of the song":str(pod.name),
        "Duration in number of seconds":str(pod.duration),
        "Uploaded time":str(pod.upload_time),
        "Host":str(pod.host),
        "participants":pod.participants
        }
        return jsonify(data)
    elif audioFileType=='audiobook':
        book=AudioBook.query.filter_by(id=int(audioFileID)).first()
        data={"Title of the audiobook":str(book.title),
        "Author of the title":book.title,
        "Narrator":book.narrator,
        "Duration in number of seconds":str(book.duration),
        "Uploaded time":str(book.upload_time),
        }
        return jsonify(data)


@app.route('/get/<audioFileType>')
def getall(audioFileType):
    data=[]
    if audioFileType=='song':
        songs=SONGFILE.query.all()
        for song in songs:
            data.append({"Name of the song":str(song.name),
        "Duration in number of seconds":str(song.duration),
        "Uploaded time":str(song.upload_time)
        })
        return jsonify(data)
    elif audioFileType=='podcast':
        pods=PodcastFile.query.all()
        for pod in pods:
            data.append({"Name of the song":str(pod.name),
        "Duration in number of seconds":str(pod.duration),
        "Uploaded time":str(pod.upload_time),
        "Host":str(pod.host),
        "participants":pod.participants
        })
        return jsonify(data)
    elif audioFileType=='audiobook':
        books=AudioBook.query.all()
        for book in books:
            data.append({"Title of the audiobook":str(book.title),
        "Author of the title":book.title,
        "Narrator":book.narrator,
        "Duration in number of seconds":str(book.duration),
        "Uploaded time":str(book.upload_time)
        })

        return jsonify(data)




if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
