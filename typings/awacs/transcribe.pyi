"""
This type stub file was generated by pyright.
"""

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Amazon Transcribe"
prefix = "transcribe"

class Action(BaseAction):
    def __init__(self, action=...) -> None: ...

class ARN(BaseARN):
    def __init__(self, resource=..., region=..., account=...) -> None: ...

CreateLanguageModel = Action("CreateLanguageModel")
CreateMedicalVocabulary = Action("CreateMedicalVocabulary")
CreateVocabulary = Action("CreateVocabulary")
CreateVocabularyFilter = Action("CreateVocabularyFilter")
DeleteLanguageModel = Action("DeleteLanguageModel")
DeleteMedicalTranscriptionJob = Action("DeleteMedicalTranscriptionJob")
DeleteMedicalVocabulary = Action("DeleteMedicalVocabulary")
DeleteTranscriptionJob = Action("DeleteTranscriptionJob")
DeleteVocabulary = Action("DeleteVocabulary")
DeleteVocabularyFilter = Action("DeleteVocabularyFilter")
DescribeLanguageModel = Action("DescribeLanguageModel")
GetMedicalTranscriptionJob = Action("GetMedicalTranscriptionJob")
GetMedicalVocabulary = Action("GetMedicalVocabulary")
GetTranscriptionJob = Action("GetTranscriptionJob")
GetVocabulary = Action("GetVocabulary")
GetVocabularyFilter = Action("GetVocabularyFilter")
ListLanguageModels = Action("ListLanguageModels")
ListMedicalTranscriptionJobs = Action("ListMedicalTranscriptionJobs")
ListMedicalVocabularies = Action("ListMedicalVocabularies")
ListTranscriptionJobs = Action("ListTranscriptionJobs")
ListVocabularies = Action("ListVocabularies")
ListVocabularyFilters = Action("ListVocabularyFilters")
StartMedicalStreamTranscription = Action("StartMedicalStreamTranscription")
StartMedicalStreamTranscriptionWebSocket = Action(
    "StartMedicalStreamTranscriptionWebSocket"
)
StartMedicalTranscriptionJob = Action("StartMedicalTranscriptionJob")
StartStreamTranscription = Action("StartStreamTranscription")
StartStreamTranscriptionWebSocket = Action("StartStreamTranscriptionWebSocket")
StartTranscriptionJob = Action("StartTranscriptionJob")
UpdateMedicalVocabulary = Action("UpdateMedicalVocabulary")
UpdateVocabulary = Action("UpdateVocabulary")
UpdateVocabularyFilter = Action("UpdateVocabularyFilter")