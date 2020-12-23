import ast
from instagram_private_api import Client, ClientCompatPatch
import json

user_name = input('username ')
password = input('password ')
api = Client(user_name, password,auto_patch=True)
print("connexion succes")

liste_des_id_des_media=[]
liste_des_commentaires=[]
liste_des_textes_de_publication=[]

# ---------------------------- récuperer les publication qui contiennent un tag #jackchirac --------------------------
results=api.feed_tag('jackchirac',api.generate_uuid())

with open('C:/Users/Bensammar/Desktop/toutes_les_infos_jackchirac.json', 'w') as jsonFile:
    json.dump(results, jsonFile)



# ---------------------------- récuperer les ID des média ----------------------------------------------------------
for y in range(len(results['ranked_items'])):
    for item in (results['ranked_items'][y]['caption'].items()):
        x=0;
        for it in item:
            if x==1:
                liste_des_id_des_media.append(item)
                x = 0
            if it == 'media_id':
                x=1;

for y in range(len(results['items'])):
    for item in (results['items'][y]['caption'].items()):
        x=0;
        for it in item:
            if x==1:
                liste_des_id_des_media.append(item)
                x = 0
            if it == 'media_id':
                x=1;


#----------------------------------- récuperer le texte de la publication -----------------------------------------
for i in range(len(liste_des_id_des_media)):
    results1=api.media_comments(str(liste_des_id_des_media[i][1]))
    try:
        for item in (results1['caption'].items()):
            x = 0;
            for it in item:
                if x == 1:
                    liste_des_textes_de_publication.append(it)
                    x = 0
                if it == 'text':
                    x = 1
    except:
        print("pas de texte")

pub=json.dumps(liste_des_textes_de_publication)
pub = ast.literal_eval(pub)
with open('C:/Users/Bensammar/Desktop/liste_des_textes_de_publication.json', 'w') as jsonFile:
    json.dump(pub, jsonFile)

#------------------------------------récuperer les commentaires des publications ------------------------------------
for i in range(len(liste_des_id_des_media)):
    r=api.media_comments(str(liste_des_id_des_media[i][1]))
    try:
        for i in range(len(r['comments'])):
            for item in (r['comments'][i].items()):
                x = 0;
                for it in item:
                    if x == 1:
                        liste_des_commentaires.append(it)
                        x = 0
                    if it == 'text':
                        x = 1
    except:
       print('pas de comments')

comment=json.dumps(liste_des_commentaires)
comment = ast.literal_eval(comment)
with open('C:/Users/Bensammar/Desktop/liste_des_commentaires.json', 'w') as jsonFile:
    json.dump(comment, jsonFile)











