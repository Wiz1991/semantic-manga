import collections
from bson.objectid import ObjectId
import pymongo
from pymongo.collection import ReturnDocument
import manga_utils
from tqdm import tqdm
from bson import ObjectId
db_str = "mongodb://localhost:27017/dev"
dir_inout = "output/"
client = pymongo.MongoClient(db_str)
new_db = True
db = client.get_database('randomanga')
manga_collection = db.mangas
tag_collection = db.tags
manga_data = manga_utils.read_raw_manga_data_files(dir_inout)

MediaTagCollection = [
    {
        "name": "4-koma",
        "isAdult": False,
        "category": "Technical"
    },
    {
        "name": "Achromatic",
        "isAdult": False,
        "category": "Technical"
    },
    {
        "name": "Achronological Order",
        "isAdult": False,
        "category": "Setting-Time"
    },
    {
        "name": "Acting",
        "isAdult": False,
        "category": "Theme-Arts"
    },
    {
        "name": "Advertisement",
        "isAdult": False,
        "category": "Technical"
    },
    {
        "name": "Afterlife",
        "isAdult": False,
        "category": "Setting-Universe"
    },
    {
        "name": "Age Gap",
        "isAdult": False,
        "category": "Theme-Romance"
    },
    {
        "name": "Age Regression",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Agender",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Agriculture",
        "isAdult": False,
        "category": "Theme-Slice of Life"
    },
    {
        "name": "Ahegao",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Airsoft",
        "isAdult": False,
        "category": "Theme-Game-Sport"
    },
    {
        "name": "Aliens",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Alternate Universe",
        "isAdult": False,
        "category": "Setting-Universe"
    },
    {
        "name": "American Football",
        "isAdult": False,
        "category": "Theme-Game-Sport"
    },
    {
        "name": "Amnesia",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Amputation",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Anachronism",
        "isAdult": False,
        "category": "Setting-Time"
    },
    {
        "name": "Anal Sex",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Animals",
        "isAdult": False,
        "category": "Theme-Other"
    },
    {
        "name": "Anthology",
        "isAdult": False,
        "category": "Technical"
    },
    {
        "name": "Anti-Hero",
        "isAdult": False,
        "category": "Cast-Main Cast"
    },
    {
        "name": "Archery",
        "isAdult": False,
        "category": "Theme-Action"
    },
    {
        "name": "Armpits",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Artificial Intelligence",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Asexual",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Ashikoki",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Asphyxiation",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Assassins",
        "isAdult": False,
        "category": "Theme-Other-Organisations"
    },
    {
        "name": "Astronomy",
        "isAdult": False,
        "category": "Theme-Other"
    },
    {
        "name": "Athletics",
        "isAdult": False,
        "category": "Theme-Game-Sport"
    },
    {
        "name": "Augmented Reality",
        "isAdult": False,
        "category": "Setting-Universe"
    },
    {
        "name": "Autobiographical",
        "isAdult": False,
        "category": "Theme-Other"
    },
    {
        "name": "Aviation",
        "isAdult": False,
        "category": "Theme-Other-Vehicle"
    },
    {
        "name": "Badminton",
        "isAdult": False,
        "category": "Theme-Game-Sport"
    },
    {
        "name": "Band",
        "isAdult": False,
        "category": "Theme-Arts-Music"
    },
    {
        "name": "Bar",
        "isAdult": False,
        "category": "Setting-Scene"
    },
    {
        "name": "Baseball",
        "isAdult": False,
        "category": "Theme-Game-Sport"
    },
    {
        "name": "Basketball",
        "isAdult": False,
        "category": "Theme-Game-Sport"
    },
    {
        "name": "Battle Royale",
        "isAdult": False,
        "category": "Theme-Action"
    },
    {
        "name": "Biographical",
        "isAdult": False,
        "category": "Theme-Other"
    },
    {
        "name": "Bisexual",
        "isAdult": False,
        "category": "Theme-Romance"
    },
    {
        "name": "Blackmail",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Body Horror",
        "isAdult": False,
        "category": "Theme-Other"
    },
    {
        "name": "Body Swapping",
        "isAdult": False,
        "category": "Theme-Fantasy"
    },
    {
        "name": "Bondage",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Boobjob",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Boxing",
        "isAdult": False,
        "category": "Theme-Game-Sport"
    },
    {
        "name": "Boys' Love",
        "isAdult": False,
        "category": "Theme-Romance"
    },
    {
        "name": "Bullying",
        "isAdult": False,
        "category": "Theme-Drama"
    },
    {
        "name": "Butler",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Calligraphy",
        "isAdult": False,
        "category": "Theme-Arts"
    },
    {
        "name": "Cannibalism",
        "isAdult": False,
        "category": "Theme-Other"
    },
    {
        "name": "Card Battle",
        "isAdult": False,
        "category": "Theme-Game-Card & Board Game"
    },
    {
        "name": "Cars",
        "isAdult": False,
        "category": "Theme-Other-Vehicle"
    },
    {
        "name": "Centaur",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "CGI",
        "isAdult": False,
        "category": "Technical"
    },
    {
        "name": "Cheerleading",
        "isAdult": False,
        "category": "Theme-Game-Sport"
    },
    {
        "name": "Chibi",
        "isAdult": False,
        "category": "Theme-Other"
    },
    {
        "name": "Chimera",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Chuunibyou",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Circus",
        "isAdult": False,
        "category": "Setting-Scene"
    },
    {
        "name": "Classic Literature",
        "isAdult": False,
        "category": "Theme-Arts"
    },
    {
        "name": "College",
        "isAdult": False,
        "category": "Setting-Scene"
    },
    {
        "name": "Coming of Age",
        "isAdult": False,
        "category": "Theme-Drama"
    },
    {
        "name": "Conspiracy",
        "isAdult": False,
        "category": "Theme-Drama"
    },
    {
        "name": "Cosmic Horror",
        "isAdult": False,
        "category": "Theme-Other"
    },
    {
        "name": "Cosplay",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Crime",
        "isAdult": False,
        "category": "Theme-Other"
    },
    {
        "name": "Crossdressing",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Crossover",
        "isAdult": False,
        "category": "Theme-Other"
    },
    {
        "name": "Cult",
        "isAdult": False,
        "category": "Theme-Other-Organisations"
    },
    {
        "name": "Cultivation",
        "isAdult": False,
        "category": "Theme-Fantasy"
    },
    {
        "name": "Cunnilingus",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Cute Girls Doing Cute Things",
        "isAdult": False,
        "category": "Theme-Slice of Life"
    },
    {
        "name": "Cyberpunk",
        "isAdult": False,
        "category": "Theme-Sci-Fi"
    },
    {
        "name": "Cyborg",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Cycling",
        "isAdult": False,
        "category": "Theme-Game-Sport"
    },
    {
        "name": "Dancing",
        "isAdult": False,
        "category": "Theme-Arts-Music"
    },
    {
        "name": "Death Game",
        "isAdult": False,
        "category": "Theme-Other"
    },
    {
        "name": "Defloration",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Delinquents",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Demons",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Denpa",
        "isAdult": False,
        "category": "Theme-Other"
    },
    {
        "name": "Detective",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Dinosaurs",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Dissociative Identities",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Dragons",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Drawing",
        "isAdult": False,
        "category": "Theme-Arts"
    },
    {
        "name": "Drugs",
        "isAdult": False,
        "category": "Theme-Other"
    },
    {
        "name": "Dullahan",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Dungeon",
        "isAdult": False,
        "category": "Setting-Scene"
    },
    {
        "name": "Dystopian",
        "isAdult": False,
        "category": "Setting-Time"
    },
    {
        "name": "E-Sports",
        "isAdult": False,
        "category": "Theme-Game"
    },
    {
        "name": "Economics",
        "isAdult": False,
        "category": "Theme-Other"
    },
    {
        "name": "Educational",
        "isAdult": False,
        "category": "Theme-Other"
    },
    {
        "name": "Elf",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Ensemble Cast",
        "isAdult": False,
        "category": "Cast-Main Cast"
    },
    {
        "name": "Environmental",
        "isAdult": False,
        "category": "Theme-Other"
    },
    {
        "name": "Episodic",
        "isAdult": False,
        "category": "Technical"
    },
    {
        "name": "Ero Guro",
        "isAdult": False,
        "category": "Theme-Other"
    },
    {
        "name": "Espionage",
        "isAdult": False,
        "category": "Theme-Action"
    },
    {
        "name": "Exhibitionism",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Facial",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Fairy Tale",
        "isAdult": False,
        "category": "Theme-Fantasy"
    },
    {
        "name": "Family Life",
        "isAdult": False,
        "category": "Theme-Slice of Life"
    },
    {
        "name": "Fashion",
        "isAdult": False,
        "category": "Theme-Arts"
    },
    {
        "name": "Feet",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Fellatio",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Female Protagonist",
        "isAdult": False,
        "category": "Cast-Main Cast"
    },
    {
        "name": "Firefighters",
        "isAdult": False,
        "category": "Theme-Other-Organisations"
    },
    {
        "name": "Fishing",
        "isAdult": False,
        "category": "Theme-Game-Sport"
    },
    {
        "name": "Fitness",
        "isAdult": False,
        "category": "Theme-Game-Sport"
    },
    {
        "name": "Flash",
        "isAdult": False,
        "category": "Technical"
    },
    {
        "name": "Flat Chest",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Food",
        "isAdult": False,
        "category": "Theme-Arts"
    },
    {
        "name": "Football",
        "isAdult": False,
        "category": "Theme-Game-Sport"
    },
    {
        "name": "Foreign",
        "isAdult": False,
        "category": "Setting-Scene"
    },
    {
        "name": "Fugitive",
        "isAdult": False,
        "category": "Theme-Action"
    },
    {
        "name": "Full CGI",
        "isAdult": False,
        "category": "Technical"
    },
    {
        "name": "Full Color",
        "isAdult": False,
        "category": "Technical"
    },
    {
        "name": "Futanari",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Gambling",
        "isAdult": False,
        "category": "Theme-Other"
    },
    {
        "name": "Gangs",
        "isAdult": False,
        "category": "Theme-Other-Organisations"
    },
    {
        "name": "Gender Bending",
        "isAdult": False,
        "category": "Theme-Other"
    },
    {
        "name": "Ghost",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Go",
        "isAdult": False,
        "category": "Theme-Game-Card & Board Game"
    },
    {
        "name": "Goblin",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Gods",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Golf",
        "isAdult": False,
        "category": "Theme-Game-Sport"
    },
    {
        "name": "Gore",
        "isAdult": False,
        "category": "Theme-Other"
    },
    {
        "name": "Group Sex",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Guns",
        "isAdult": False,
        "category": "Theme-Action"
    },
    {
        "name": "Gyaru",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Handjob",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Harem",
        "isAdult": False,
        "category": "Theme-Romance"
    },
    {
        "name": "Henshin",
        "isAdult": False,
        "category": "Theme-Fantasy"
    },
    {
        "name": "Hikikomori",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Historical",
        "isAdult": False,
        "category": "Setting-Time"
    },
    {
        "name": "Human Pet",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Ice Skating",
        "isAdult": False,
        "category": "Theme-Game-Sport"
    },
    {
        "name": "Idol",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Incest",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Irrumatio",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Isekai",
        "isAdult": False,
        "category": "Theme-Fantasy"
    },
    {
        "name": "Iyashikei",
        "isAdult": False,
        "category": "Theme-Slice of Life"
    },
    {
        "name": "Josei",
        "isAdult": False,
        "category": "Demographic"
    },
    {
        "name": "Kaiju",
        "isAdult": False,
        "category": "Theme-Fantasy"
    },
    {
        "name": "Karuta",
        "isAdult": False,
        "category": "Theme-Game-Card & Board Game"
    },
    {
        "name": "Kemonomimi",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Kids",
        "isAdult": False,
        "category": "Demographic"
    },
    {
        "name": "Kuudere",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Lacrosse",
        "isAdult": False,
        "category": "Theme-Game-Sport"
    },
    {
        "name": "Lactation",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Language Barrier",
        "isAdult": False,
        "category": "Setting-Scene"
    },
    {
        "name": "Large Breasts",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "LGBTQ+ Themes",
        "isAdult": False,
        "category": "Theme-Other"
    },
    {
        "name": "Lost Civilization",
        "isAdult": False,
        "category": "Theme-Other"
    },
    {
        "name": "Love Triangle",
        "isAdult": False,
        "category": "Theme-Romance"
    },
    {
        "name": "Mafia",
        "isAdult": False,
        "category": "Theme-Other-Organisations"
    },
    {
        "name": "Magic",
        "isAdult": False,
        "category": "Theme-Fantasy"
    },
    {
        "name": "Mahjong",
        "isAdult": False,
        "category": "Theme-Game-Card & Board Game"
    },
    {
        "name": "Maids",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Male Protagonist",
        "isAdult": False,
        "category": "Cast-Main Cast"
    },
    {
        "name": "Martial Arts",
        "isAdult": False,
        "category": "Theme-Action"
    },
    {
        "name": "Masochism",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Masturbation",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Medicine",
        "isAdult": False,
        "category": "Theme-Other"
    },
    {
        "name": "Memory Manipulation",
        "isAdult": False,
        "category": "Theme-Other"
    },
    {
        "name": "Mermaid",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Meta",
        "isAdult": False,
        "category": "Theme-Other"
    },
    {
        "name": "MILF",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Military",
        "isAdult": False,
        "category": "Theme-Other-Organisations"
    },
    {
        "name": "Monster Girl",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Mopeds",
        "isAdult": False,
        "category": "Theme-Other-Vehicle"
    },
    {
        "name": "Motorcycles",
        "isAdult": False,
        "category": "Theme-Other-Vehicle"
    },
    {
        "name": "Musical",
        "isAdult": False,
        "category": "Theme-Arts-Music"
    },
    {
        "name": "Mythology",
        "isAdult": False,
        "category": "Theme-Fantasy"
    },
    {
        "name": "Nakadashi",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Nekomimi",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Netorare",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Netorase",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Netori",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Ninja",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "No Dialogue",
        "isAdult": False,
        "category": "Technical"
    },
    {
        "name": "Noir",
        "isAdult": False,
        "category": "Theme-Other"
    },
    {
        "name": "Nudity",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Nun",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Office Lady",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Oiran",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Ojou-sama",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Omegaverse",
        "isAdult": True,
        "category": "Setting-Universe"
    },
    {
        "name": "Otaku Culture",
        "isAdult": False,
        "category": "Theme-Other"
    },
    {
        "name": "Outdoor",
        "isAdult": False,
        "category": "Setting-Scene"
    },
    {
        "name": "Pandemic",
        "isAdult": False,
        "category": "Theme-Other"
    },
    {
        "name": "Parkour",
        "isAdult": False,
        "category": "Theme-Game-Sport"
    },
    {
        "name": "Parody",
        "isAdult": False,
        "category": "Theme-Comedy"
    },
    {
        "name": "Philosophy",
        "isAdult": False,
        "category": "Theme-Other"
    },
    {
        "name": "Photography",
        "isAdult": False,
        "category": "Theme-Arts"
    },
    {
        "name": "Pirates",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Poker",
        "isAdult": False,
        "category": "Theme-Game-Card & Board Game"
    },
    {
        "name": "Police",
        "isAdult": False,
        "category": "Theme-Other-Organisations"
    },
    {
        "name": "Politics",
        "isAdult": False,
        "category": "Theme-Other"
    },
    {
        "name": "Post-Apocalyptic",
        "isAdult": False,
        "category": "Setting-Universe"
    },
    {
        "name": "POV",
        "isAdult": False,
        "category": "Technical"
    },
    {
        "name": "Pregnant",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Primarily Adult Cast",
        "isAdult": False,
        "category": "Cast-Main Cast"
    },
    {
        "name": "Primarily Child Cast",
        "isAdult": False,
        "category": "Cast-Main Cast"
    },
    {
        "name": "Primarily Female Cast",
        "isAdult": False,
        "category": "Cast-Main Cast"
    },
    {
        "name": "Primarily Male Cast",
        "isAdult": False,
        "category": "Cast-Main Cast"
    },
    {
        "name": "Prostitution",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Public Sex",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Puppetry",
        "isAdult": False,
        "category": "Technical"
    },
    {
        "name": "Rakugo",
        "isAdult": False,
        "category": "Theme-Arts"
    },
    {
        "name": "Rape",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Real Robot",
        "isAdult": False,
        "category": "Theme-Sci-Fi-Mecha"
    },
    {
        "name": "Rehabilitation",
        "isAdult": False,
        "category": "Theme-Drama"
    },
    {
        "name": "Reincarnation",
        "isAdult": False,
        "category": "Theme-Other"
    },
    {
        "name": "Revenge",
        "isAdult": False,
        "category": "Theme-Drama"
    },
    {
        "name": "Reverse Harem",
        "isAdult": False,
        "category": "Theme-Romance"
    },
    {
        "name": "Rimjob",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Robots",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Rotoscoping",
        "isAdult": False,
        "category": "Technical"
    },
    {
        "name": "Rugby",
        "isAdult": False,
        "category": "Theme-Game-Sport"
    },
    {
        "name": "Rural",
        "isAdult": False,
        "category": "Setting-Scene"
    },
    {
        "name": "Sadism",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Samurai",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Satire",
        "isAdult": False,
        "category": "Theme-Comedy"
    },
    {
        "name": "Scat",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "School",
        "isAdult": False,
        "category": "Setting-Scene"
    },
    {
        "name": "School Club",
        "isAdult": False,
        "category": "Setting-Scene"
    },
    {
        "name": "Scuba Diving",
        "isAdult": False,
        "category": "Theme-Game-Sport"
    },
    {
        "name": "Seinen",
        "isAdult": False,
        "category": "Demographic"
    },
    {
        "name": "Sex Toys",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Shapeshifting",
        "isAdult": False,
        "category": "Theme-Fantasy"
    },
    {
        "name": "Ships",
        "isAdult": False,
        "category": "Theme-Other-Vehicle"
    },
    {
        "name": "Shogi",
        "isAdult": False,
        "category": "Theme-Game-Card & Board Game"
    },
    {
        "name": "Shoujo",
        "isAdult": False,
        "category": "Demographic"
    },
    {
        "name": "Shounen",
        "isAdult": False,
        "category": "Demographic"
    },
    {
        "name": "Shrine Maiden",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Skateboarding",
        "isAdult": False,
        "category": "Theme-Game-Sport"
    },
    {
        "name": "Skeleton",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Slapstick",
        "isAdult": False,
        "category": "Theme-Comedy"
    },
    {
        "name": "Slavery",
        "isAdult": False,
        "category": "Theme-Other"
    },
    {
        "name": "Software Development",
        "isAdult": False,
        "category": "Theme-Other"
    },
    {
        "name": "Space",
        "isAdult": False,
        "category": "Setting-Universe"
    },
    {
        "name": "Space Opera",
        "isAdult": False,
        "category": "Theme-Sci-Fi"
    },
    {
        "name": "Steampunk",
        "isAdult": False,
        "category": "Theme-Fantasy"
    },
    {
        "name": "Stop Motion",
        "isAdult": False,
        "category": "Technical"
    },
    {
        "name": "Succubus",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Sumata",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Super Power",
        "isAdult": False,
        "category": "Theme-Fantasy"
    },
    {
        "name": "Super Robot",
        "isAdult": False,
        "category": "Theme-Sci-Fi-Mecha"
    },
    {
        "name": "Superhero",
        "isAdult": False,
        "category": "Theme-Fantasy"
    },
    {
        "name": "Surfing",
        "isAdult": False,
        "category": "Theme-Game-Sport"
    },
    {
        "name": "Surreal Comedy",
        "isAdult": False,
        "category": "Theme-Comedy"
    },
    {
        "name": "Survival",
        "isAdult": False,
        "category": "Theme-Other"
    },
    {
        "name": "Sweat",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Swimming",
        "isAdult": False,
        "category": "Theme-Game-Sport"
    },
    {
        "name": "Swordplay",
        "isAdult": False,
        "category": "Theme-Action"
    },
    {
        "name": "Table Tennis",
        "isAdult": False,
        "category": "Theme-Game-Sport"
    },
    {
        "name": "Tanks",
        "isAdult": False,
        "category": "Theme-Other-Vehicle"
    },
    {
        "name": "Tanned Skin",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Teacher",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Teens' Love",
        "isAdult": False,
        "category": "Theme-Romance"
    },
    {
        "name": "Tennis",
        "isAdult": False,
        "category": "Theme-Game-Sport"
    },
    {
        "name": "Tentacles",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Terrorism",
        "isAdult": False,
        "category": "Theme-Other"
    },
    {
        "name": "Threesome",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Time Manipulation",
        "isAdult": False,
        "category": "Theme-Sci-Fi"
    },
    {
        "name": "Time Skip",
        "isAdult": False,
        "category": "Setting-Time"
    },
    {
        "name": "Tokusatsu",
        "isAdult": False,
        "category": "Theme-Sci-Fi"
    },
    {
        "name": "Tomboy",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Tragedy",
        "isAdult": False,
        "category": "Theme-Drama"
    },
    {
        "name": "Trains",
        "isAdult": False,
        "category": "Theme-Other-Vehicle"
    },
    {
        "name": "Triads",
        "isAdult": False,
        "category": "Theme-Other-Organisations"
    },
    {
        "name": "Tsundere",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Twins",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Urban",
        "isAdult": False,
        "category": "Setting-Scene"
    },
    {
        "name": "Urban Fantasy",
        "isAdult": False,
        "category": "Setting-Universe"
    },
    {
        "name": "Urination",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Vampire",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Video Games",
        "isAdult": False,
        "category": "Theme-Game"
    },
    {
        "name": "Vikings",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Villainess",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Virginity",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Virtual World",
        "isAdult": False,
        "category": "Setting-Universe"
    },
    {
        "name": "Volleyball",
        "isAdult": False,
        "category": "Theme-Game-Sport"
    },
    {
        "name": "Vore",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "Voyeur",
        "isAdult": True,
        "category": "Sexual Content"
    },
    {
        "name": "War",
        "isAdult": False,
        "category": "Theme-Other"
    },
    {
        "name": "Werewolf",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Witch",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Work",
        "isAdult": False,
        "category": "Setting-Scene"
    },
    {
        "name": "Wrestling",
        "isAdult": False,
        "category": "Theme-Game-Sport"
    },
    {
        "name": "Writing",
        "isAdult": False,
        "category": "Theme-Arts"
    },
    {
        "name": "Wuxia",
        "isAdult": False,
        "category": "Theme-Fantasy"
    },
    {
        "name": "Yakuza",
        "isAdult": False,
        "category": "Theme-Other-Organisations"
    },
    {
        "name": "Yandere",
        "isAdult": False,
        "category": "Cast-Traits"
    },
    {
        "name": "Youkai",
        "isAdult": False,
        "category": "Theme-Fantasy"
    },
    {
        "name": "Yuri",
        "isAdult": False,
        "category": "Theme-Romance"
    },
    {
        "name": "Zombie",
        "isAdult": False,
        "category": "Cast-Traits"
    }
]


def insert_raw_data():
    for manga in tqdm(manga_data, desc="Inserting data"):

        query = {
            'al_id': manga.id,
            'title': manga.title,
            'al_url': manga.url,
            'description': manga.description,
            'demographic': manga.demographic,
            'genre': manga.genre,
            'tags': manga.tags,
            'related': [],
            'banner': manga.banner,
            'cover_image': manga.coverImage,
            'likes': [],
            'isAdult': manga.isAdult,
        }
        if new_db:
            manga_collection.insert_one(query)
        else:
            manga_collection.update_one({'al_id': manga.id}, {'$set': {
                'title': manga.title,
                'al_url': manga.url,
                'description': manga.description,
                'demographic': manga.demographic,
                'genre': manga.genre,
                'tags': manga.tags,
                'banner': manga.banner,
                'cover_image': manga.coverImage,
                'isAdult': manga.isAdult,
            }})


def insert_related():
    for manga in tqdm(manga_data, desc="Updating related"):
        result = manga_collection.find(
            {"al_id": {"$in": [int(x["id"]) for x in manga.matches]}}, {"_id": 1, "al_id": 1})
        for res in result:
            for match in manga.matches:
                if res['al_id'] == match['id']:
                    manga.related.append(res['al_id'])

        manga_collection.find_one_and_update(
            {'al_id': manga.id}, {"$set": {"related": manga.related}})


def insert_tags():
    for tag in tqdm(MediaTagCollection, desc="Inserting tags"):
        tag_collection.insert_one(tag)


#insert_raw_data()
insert_related()
#if new_db:
    #insert_tags()
