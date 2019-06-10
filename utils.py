from pymongo import MongoClient
client = MongoClient("mongodb+srv://test:test@cluster0-9nmh4.mongodb.net/test?retryWrites=true&w=majority")
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "client-secret.json"


import wikipedia



from PyDictionary import PyDictionary
dictionanry=PyDictionary()


db =client.get_database('bot_db')
records = db.bot_records


import dialogflow_v2 as dialogflow
dialogflow_session_client = dialogflow.SessionsClient()
PROJECT_ID = "db-bot-qaenmw"

def get_meaning(parameters):
    print(parameters)
    word = parameters.get('dict_word')
    return word
def get_translates(parameters):
    words = parameters.get('dict_translate')
    return words
def get_translate(parameters):
    words = parameters.get('dict_image')
    return words
    
def detect_intent_from_text(text, session_id, language_code='en'):
    session = dialogflow_session_client.session_path(PROJECT_ID, session_id)
    text_input = dialogflow.types.TextInput(text=text,language_code=language_code)
    query_input= dialogflow.types.QueryInput(text=text_input)
    response = dialogflow_session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result


def fetch_reply(msg, session_id):
    response = detect_intent_from_text(msg, session_id)
    if response.intent.display_name == 'dict_word':
        mean = get_meaning(dict(response.parameters))
        actualmean = dictionanry.meaning(mean)
        res_str="meaning of word is {}".format(actualmean['Noun'])
        dictdb={
            'word':mean,
            'meaning':res_str
        }
        records.insert_one(dictdb)
        return res_str
    if response.intent.display_name == 'dict_translate':
        mean = str(get_meaning(dict(response.parameters)))
        means = str(get_translates(dict(response.parameters)))
        actualmean = str(dictionanry.translate("rain","hi"))
        res_str="word translation is {}".format(actualmean)
        dictdb={
            'word':mean,
            'word translate':res_str
        }
        records.insert_one(dictdb)
        return res_str
    if response.intent.display_name == 'dict_image':
        mean = get_meaning(dict(response.parameters))
        ny = wikipedia.page(mean)
        myList = ny.images
        res_str="link of image is {}".format(myList[0])
        dictdb={
            'word':mean,
            'image link':res_str
        }
        records.insert_one(dictdb)
        return res_str

    else:
        return response.fulfillment_text
from pymongo import MongoClient
client = MongoClient("mongodb+srv://test:test@cluster0-9nmh4.mongodb.net/test?retryWrites=true&w=majority")
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "client-secret.json"


import wikipedia



from PyDictionary import PyDictionary
dictionanry=PyDictionary()


db =client.get_database('bot_db')
records = db.bot_records


import dialogflow_v2 as dialogflow
dialogflow_session_client = dialogflow.SessionsClient()
PROJECT_ID = "db-bot-qaenmw"

def get_meaning(parameters):
    print(parameters)
    word = parameters.get('dict_word')
    return word
def get_translates(parameters):
    words = parameters.get('dict_translate')
    return words
def get_translate(parameters):
    words = parameters.get('dict_image')
    return words
    
def detect_intent_from_text(text, session_id, language_code='en'):
    session = dialogflow_session_client.session_path(PROJECT_ID, session_id)
    text_input = dialogflow.types.TextInput(text=text,language_code=language_code)
    query_input= dialogflow.types.QueryInput(text=text_input)
    response = dialogflow_session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result


def fetch_reply(msg, session_id):
    response = detect_intent_from_text(msg, session_id)
    if response.intent.display_name == 'dict_word':
        mean = get_meaning(dict(response.parameters))
        actualmean = dictionanry.meaning(mean)
        res_str="meaning of word is {}".format(actualmean['Noun'])
        dictdb={
            'word':mean,
            'meaning':res_str
        }
        records.insert_one(dictdb)
        return res_str
    if response.intent.display_name == 'dict_translate':
        mean = str(get_meaning(dict(response.parameters)))
        means = str(get_translates(dict(response.parameters)))
        actualmean = str(dictionanry.translate("rain","hi"))
        res_str="word translation is {}".format(actualmean)
        dictdb={
            'word':mean,
            'word translate':res_str
        }
        records.insert_one(dictdb)
        return res_str
    if response.intent.display_name == 'dict_image':
        mean = get_meaning(dict(response.parameters))
        ny = wikipedia.page(mean)
        myList = ny.images
        res_str="link of image is {}".format(myList[0])
        dictdb={
            'word':mean,
            'image link':res_str
        }
        records.insert_one(dictdb)
        return res_str

    else:
        return response.fulfillment_text

