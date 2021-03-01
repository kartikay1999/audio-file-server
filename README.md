## audio-file-server

## CREATE
ROUTE 1:/create methods:'POST'  INPUT_TYPE: JSON

DATA_INPUT_FORMATS:
{"audioFileType":"song",
        "audioFileMetadata":{
            "Name of the song" : (mandatory, string, cannot be larger than 100 characters)
            "Duration in number of seconds" – (mandatory, integer, positive)
              }
 }
 
 {"audioFileType":"podcast",
        "audioFileMetadata":{
         "Name of the podcast":"test song",
        "Duration in number of seconds" – (mandatory, integer, positive)
        "Host" – (mandatory, string, cannot be larger than 100 characters)
        "Participants" – (optional, list of strings)
          }
  }
    
{"audioFileType":"audiobook",
        "audioFileMetadata":{
            "Title of the audiobook" :(mandatory, string, cannot be larger than 100 characters),
            "Author of the title": (mandatory, string, cannot be larger than 100 characters),
            "Narrator" : (mandatory, string, cannot be larger than 100 characters),
            "Author of the title": (mandatory, string, cannot be larger than 100 characters),
            "Duration in number of seconds":(mandatory, integer, positive)
        }
}
 
 
