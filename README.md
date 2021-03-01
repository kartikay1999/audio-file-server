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
ROUTE:/update/<songfiletype> METHODS='POST' INPUT_TYPE:JSON

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

 
