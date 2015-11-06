#imports
import copy, pprint, time, math, random, string, names

class Generator:
    #init for n iterations and the original data validated against
    #avro schema
    def __init__(self, n):
        self.n = n
        self.person_data = [{'pedigree': {'true_as_of_secs': 1234567890},
           'dataunit': {'person_property': {'id': {'person_id': 'balaji'},
                                    'property': {'website': 'http://google.com'}}},
           },
        {'pedigree': {'true_as_of_secs': 1234567890},
           'dataunit': {'person_property': {'id': {'person_id': 'balaji'},
                                    'property': {'email': 'balaji.k.vijayan@gmail.com'}}},
           },
        {'pedigree': {'true_as_of_secs': 1234567890},
           'dataunit': {'person_property': {'id': {'person_id': 'balaji'},
                                    'property': {'desc': 'Howdy'}}},
           },
        {'pedigree': {'true_as_of_secs': 1234567890},
           'dataunit': {'person_property': {'id': {'person_id': 'balaji'},
                                    'property': {'name': 'Balaji Vijayan'}}},
           },
        {'pedigree': {'true_as_of_secs': 1234567890},
           'dataunit': {'person_property': {'id': {'person_id': 'balaji'},
                                    'property': {'phone': '(555)555-5555'}}},
           }]
        self.media_data = [{'pedigree': {'true_as_of_secs': 1234567892},
           'dataunit': {'media_property': {'id': {'media_id': 1},
                                    'property': {'url': 'http://amazon.com'}}},
           },
        {'pedigree': {'true_as_of_secs': 1234567892},
           'dataunit': {'media_property': {'id': {'media_id': 1},
                                    'property': {'desc': 'So #blessed'}}},
           },
        {'pedigree': {'true_as_of_secs': 1234567892},
           'dataunit': {'media_property': {'id': {'media_id': 1},
                                    'property': {'media_type': False}}},
           }]
        self.hashtag_data = {"pedigree": {'true_as_of_secs': 1234567894},
           "dataunit": {"hashtag_property": {"id": {"hashtag_id": "#blessed"},
                                            "property": {"popularityscore": 100}}}
           }
        self.friend_data = {"pedigree": {"true_as_of_secs": 1234567893},
           "dataunit": {"friends": {"id1": {"person_id": "balaji"},
                                  "id2": {"person_id": "jones"}}},
           }
        self.search_data = {"pedigree": {'true_as_of_secs': 1234567895},
           "dataunit": {"searches": {"id1": {"person_id": "balaji"},
                                  "id2": {"hashtag_id": "#blessed"}}},
           }
        self.like_data = {"pedigree": {'true_as_of_secs': 1234567896},
           "dataunit": {"likes": {"id1": {"person_id": "jones"},
                                  "id2": {"media_id": 1}}},
           }
        self.contain_data = {"pedigree": {'true_as_of_secs': 1234567897},
           "dataunit": {"contains": {"id1": {"media_id": 1},
                                  "id2": {"hashtag_id": "#blessed"}}},
           }
    def Person(self):
        #creating random data
        person = copy.deepcopy(self.person_data)

        #person data
        name = names.get_full_name()
        person_id = name.replace(" ","")
        website = "https://"+person_id+".com"
        email = person_id+"@yahoo.com"
        person_desc = names.get_full_name()\
            +" "+names.get_full_name()
        phone = ("("+"".join([str(random.randint(0, 9)) for i in range(3)])\
            +")"+"".join([str(random.randint(0, 9)) for i in range(7)])).decode()

        person[0]['pedigree']['true_as_of_secs'] \
            = int(math.floor(time.time()))
        person[0]['dataunit']['person_property']['id']['person_id'] \
            = person_id
        person[0]['dataunit']['person_property']['property']['website']\
            = website

        person[1]['pedigree']['true_as_of_secs'] \
            = int(math.floor(time.time()))
        person[1]['dataunit']['person_property']['id']['person_id'] \
            = person_id
        person[1]['dataunit']['person_property']['property']['email']\
            = email

        person[2]['pedigree']['true_as_of_secs'] \
            = int(math.floor(time.time()))
        person[2]['dataunit']['person_property']['id']['person_id'] \
            = person_id
        person[2]['dataunit']['person_property']['property']['desc'] \
            = person_desc

        person[3]['pedigree']['true_as_of_secs'] \
            = int(math.floor(time.time()))
        person[3]['dataunit']['person_property']['id']['person_id'] \
            = person_id
        person[3]['dataunit']['person_property']['property']['name'] \
            = name

        person[4]['pedigree']['true_as_of_secs'] \
            = int(math.floor(time.time()))
        person[4]['dataunit']['person_property']['id']['person_id'] \
            = person_id
        person[4]['dataunit']['person_property']['property']['phone'] \
            = phone

        return person
            
    def Media(self):
        #creating random data
        media = copy.deepcopy(self.media_data)
        #media data
        media_id = random.randint(1,50)
        url = "https://"+"".join(random.SystemRandom().choice(
            string.lowercase) for _ in range(6))+".com"
        media_desc = "".join(random.SystemRandom().choice(
            string.lowercase) for _ in range(20))
        media_type = random.randint(0,1)

        media[0]['pedigree']['true_as_of_secs'] \
            = int(math.floor(time.time()))
        media[0]['dataunit']['media_property']['id']['media_id'] \
            = media_id
        media[0]['dataunit']['media_property']['property']['url'] \
            = url

        media[1]['pedigree']['true_as_of_secs'] \
            = int(math.floor(time.time()))
        media[1]['dataunit']['media_property']['id']['media_id'] \
            = media_id
        media[1]['dataunit']['media_property']['property']['desc'] \
            = media_desc

        media[2]['pedigree']['true_as_of_secs'] \
            = int(math.floor(time.time()))
        media[2]['dataunit']['media_property']['id']['media_id'] \
            = media_id
        media[2]['dataunit']['media_property']['property']['media_type'] \
            = media_type

        return media
    
    def Hashtag(self):
        hashtag = copy.deepcopy(self.hashtag_data)
        
        hashtaglist = ["#winning","#blessed","#squadgoals",
                     "#halloween","#data","#yourmom",
                     "#wcw","#tbt","#wine"]
        
        #hashtag data
        hashtag_id = random.choice(hashtaglist)
        popularityscore = random.randint(1,100)
        
        hashtag['pedigree']['true_as_of_secs'] \
            = int(math.floor(time.time()))
        hashtag['dataunit']['hashtag_property']['id']['hashtag_id'] \
            = hashtag_id
        hashtag['dataunit']['hashtag_property']['property']['popularityscore'] \
            = popularityscore
        
        return hashtag
    
    def Friend(self, person_id):
        friend = copy.deepcopy(self.friend_data)
        friendlist = ["BalajiVijayan","KatAquino","AlexanderBarriga",
                     "MikeMansour","AlessandroGagliardi","AndrewHuang",
                     "BrandonFetters","DonatellaTaurasi","MikeThorne"]
        person_id2 = random.choice(friendlist)
        
        friend['pedigree']['true_as_of_secs'] \
            = int(math.floor(time.time()))
        friend['dataunit']['friends']['id1']['person_id'] \
            = person_id
        friend['dataunit']['friends']['id2']['person_id'] \
            = person_id2
        
        return friend
    
    def Search(self, person_id, hashtag_id):
        search = copy.deepcopy(self.search_data)

        search['pedigree']['true_as_of_secs'] \
            = int(math.floor(time.time()))
        search['dataunit']['searches']['id1']['person_id'] \
            = person_id
        search['dataunit']['searches']['id2']['hashtag_id'] \
            = hashtag_id
        
        return search
    
    def Like(self, person_id, media_id):
        like = copy.deepcopy(self.like_data)
        
        like['pedigree']['true_as_of_secs'] \
            = int(math.floor(time.time()))
        like['dataunit']['likes']['id1']['person_id'] \
            = person_id
        like['dataunit']['likes']['id2']['media_id'] \
            = media_id
    
        return like
    
    def Contain(self, media_id, hashtag_id):
        contain = copy.deepcopy(self.contain_data)
        
        contain['pedigree']['true_as_of_secs'] \
            = int(math.floor(time.time()))
        contain['dataunit']['contains']['id1']['media_id'] \
            = media_id
        contain['dataunit']['contains']['id2']['hashtag_id'] \
            = hashtag_id

        return contain
    
    def Generate(self):
        for i in xrange(0, self.n):
            person = self.Person()
            media = self.Media()
            hashtag = self.Hashtag()
            friend = self.Friend(
                person[0]['dataunit']['person_property']['id']['person_id'])
            search = self.Search(
                person[0]['dataunit']['person_property']['id']['person_id'],
                hashtag['dataunit']['hashtag_property']['id']['hashtag_id'])
            like = self.Like(
                person[0]['dataunit']['person_property']['id']['person_id'],
                media[0]['dataunit']['media_property']['id']['media_id'])
            contain = self.Contain(
                media[0]['dataunit']['media_property']['id']['media_id'],
                hashtag['dataunit']['hashtag_property']['id']['hashtag_id'])

            value = person
            value.extend(media)
            value.append(hashtag)
            value.append(friend)
            value.append(search)
            value.append(like)
            value.append(contain)
            yield value