"""
Function to translate from English to a secondary language, in this case
French and German.
"""
# Import dependencies
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator 
from pandas import json_normalize

def englishtofrench(recognized_text):
    #Define authentication components in order to use IBM Watson Language Translator
    url = 'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/55dac344-a3eb-4394-b60c-88c078032048'
    api_key = 'v0KOYgPO7z39nxPElAHvpVY-CpMXZOkagfLUoq_TPmak'
    version = '2018-05-01'

    #Creating the language translator object
    authenticator = IAMAuthenticator(api_key)
    language_translator = LanguageTranslatorV3(version=version, authenticator=authenticator)
    language_translator.set_service_url(url)

    #Create the actual translated response as a string
    translation_response = language_translator.translate(\
        text=recognized_text, model_id='en-fr')
    translation=translation_response.get_result()
    return translation['translations'][0]['translation']
