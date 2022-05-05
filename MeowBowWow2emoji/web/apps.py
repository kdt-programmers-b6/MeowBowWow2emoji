from django.apps import AppConfig
from .emoji_model import emoji
import os
def ARG(animal, version):
    path = os.getcwd()+'/web/emoji_model/checkpoint/'
    arg_dict = emoji.parse_args()
    
    if animal == 'Cat':
        if version == 'V1':# v1 => light버전
            path += 'UGATIT_CAT_DOWN/UGATIT_light.model-700000'
            arg_dict['light']=True
            arg_dict['ch']= 64
        else:#v2 => V1버전
            path += 'UGATIT_CAT_V1/UGATIT.model-920000'
    else:#dog
        if version == 'V1':
            path += 'UGATIT_DOG_V1/UGATIT.model-810000'
        else:#v2
            path += 'UGATIT_DOG_V2/UGATIT.model-640000'

    return path, arg_dict


class WebConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'web'
    emoji_model_cat_v1 = emoji.Emoji(ARG('Cat','V1'))
    emoji_model_cat_v2 = emoji.Emoji(ARG('Cat','V2'))
    emoji_model_dog_v1 = emoji.Emoji(ARG('Dog','V1'))
    emoji_model_dog_v2 = emoji.Emoji(ARG('Dog','V2'))




