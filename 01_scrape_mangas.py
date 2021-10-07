import time
import json
import requests
import os.path
import manga_obj
import manga_utils
from tqdm import trange


def get_page_data(page, retry=99):
    query = '''  
    query($page: Int){
	    Page(page: $page,perPage: 50){
            media (type: MANGA,format_not_in: [NOVEL,ONE_SHOT]){
                isAdult
                title {
                    romaji
                    english
                    native
                }
                genres
                tags {
                    name
                    category
                    rank
                }
                description
                id
                siteUrl
                coverImage{
                    extraLarge
                    large
                    medium
                }
                bannerImage
            }       
        }
    }                 
    '''
    remaining_tries = retry
    response = {}
    while remaining_tries > 0:
        try:
            response = requests.post(
                url_main, json={'query': query, 'variables': {'page': page}})
            return response.json()['data']['Page']['media']

        except:
            time.sleep(3)
            remaining_tries -= 1
            continue
    raise Exception("Couldn't get the data")


url_main = 'https://graphql.anilist.co'
dir_inout = 'output/'
pull_from_website = True
page_count = manga_utils.get_page_count()
manga_data = manga_utils.read_raw_manga_data_files(dir_inout)


for page in trange(1, page_count, desc="Scraping"):
    # for page in range(1, page_count):
    start_time = time.time()
    page_data = get_page_data(page)

    for manga in page_data:
        data = manga_obj.MangaObj()

        data.id = manga['id']

        # already_downloaded = False
        # for ct, it in enumerate(manga_data):
        #     if data.id == it.id:
        #         already_downloaded = True
        #         break
        # if already_downloaded and not pull_from_website:
        #     continue

        data.genre = manga['genres']
        eng_title = manga['title']['english']
        jap_title = manga['title']['romaji']
        native_title = manga['title']['native']
        data.title = jap_title if jap_title is not None else eng_title if eng_title is not None else native_title
        data.url = manga['siteUrl']
        data.description = manga['description'] if manga['description'] is not None else 'no description'
        coverImage = {
            "extraLarge": manga['coverImage']['extraLarge'],
            "large": manga['coverImage']['large'],
            "medium": manga['coverImage']['medium']
        }
        data.coverImage = coverImage
        data.banner = manga['bannerImage']
        data.isAdult = manga['isAdult']

        tags = manga['tags']
        for tag in tags:
            if tag['category'] == 'Demographic':
                data.demographic.append(tag['name'])
            elif tag['rank'] >= 45:
                data.tags.append(tag['name'])

        manga_data.append(data)

    end_time = time.time()
    time_taken = round(end_time - start_time, 2)
    if time_taken < 0.7:
        time.sleep(0.7 - time_taken)

# ct_before = len(manga_data)
# t01 = time.time()
# manga_data = manga_utils.remove_dups_from_manga_list(manga_data)
# ct_after = len(manga_data)
# t11 = time.time()
# print("reduced " + str(ct_before) + " to only " + str(ct_after) +
#   " mangas (" + str(round(t11 - t01, 2)) + " seconds)")

manga_utils.write_raw_manga_data_files(dir_inout, manga_data)
print("outputted to " + dir_inout)
