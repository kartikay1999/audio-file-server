## audio-file-server

## CREATE
ROUTE:/create METHODS:'POST'  INPUT_TYPE: JSON

DATA_INPUT_FORMATS:
1.) {"audioFileType":"song",
        "audioFileMetadata":{
            "Name of the song" : (mandatory, string, cannot be larger than 100 characters)
            "Duration in number of seconds" – (mandatory, integer, positive)
              }
 }
 
 2.) {"audioFileType":"podcast",
        "audioFileMetadata":{
         "Name of the podcast":"test song",
        "Duration in number of seconds" – (mandatory, integer, positive)
        "Host" – (mandatory, string, cannot be larger than 100 characters)
        "Participants" – (optional, list of strings)
          }
  }
    
3.) {"audioFileType":"audiobook",
        "audioFileMetadata":{
            "Title of the audiobook" :(mandatory, string, cannot be larger than 100 characters),
            "Author of the title": (mandatory, string, cannot be larger than 100 characters),
            "Narrator" : (mandatory, string, cannot be larger than 100 characters),
            "Author of the title": (mandatory, string, cannot be larger than 100 characters),
            "Duration in number of seconds":(mandatory, integer, positive)
        }
}
 
 
## UPDATE
ROUTE:/update/<songfiletype>/<id> METHODS='POST' INPUT_TYPE:JSON


ACTION: UPDATES INFORMATION ABOUT THE FILE STORED AT ID=<id>
        
DATA_INPUT_FORMATS:
1.){
            "Name of the song" : (mandatory, string, cannot be larger than 100 characters)
            "Duration in number of seconds" – (mandatory, integer, positive)
              }
              
2.){
         "Name of the podcast":"test song",
        "Duration in number of seconds" – (mandatory, integer, positive)
        "Host" – (mandatory, string, cannot be larger than 100 characters)
        "Participants" – (optional, list of strings)
          }
          
3.){
            "Title of the audiobook" :(mandatory, string, cannot be larger than 100 characters),
            "Author of the title": (mandatory, string, cannot be larger than 100 characters),
            "Narrator" : (mandatory, string, cannot be larger than 100 characters),
            "Author of the title": (mandatory, string, cannot be larger than 100 characters),
            "Duration in number of seconds":(mandatory, integer, positive)
        }


## DELETE
ROUTE:/delete/<songfiletype>/<id> METHODS='GET'

ACTION: DELETES THE FILE STORED WITH THE ID=<id>
 
## GET

ROUTE 1:/get/<songfiletype>/<id> METHODS='GET'

ACTION: (RETURNS DATA ABOUT MUSIC FILE WITH ID=<id>)

ROUTE 2:/get/<songfiletype> METHODS='GET'
        
RETURNS: (RETURNS ALL THE FILES OF THAT SONG FILE TYPE)
