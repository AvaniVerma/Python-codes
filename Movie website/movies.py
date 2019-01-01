import media
import fresh_tomatoes

Deadpool = media.Movie("Deadpool",
                           "Mercenary Wade Wilson, subjected to an experiment to heal himself of cancer, obtains healing powers, but at the cost of becoming awfully disfigured. He then adopts the alter ego of Deadpool.",
                           "https://en.wikipedia.org/wiki/Deadpool_(film)#/media/File:Deadpool_(2016_poster).png",
                           "https://www.youtube.com/watch?v=ONHBaC-pfsk")

#print(Deadpool.title)


Avatar = media.Movie("Avatar",
                     "DescriptionJake, a paraplegic marine, replaces his brother on the Na'vi inhabited Pandora for a corporate mission. He is accepted by the natives as one of their own but he must decide where his loyalties lie.",
                     "https://www.google.com/imgres?imgurl=http://www.gstatic.com/tv/thumb/v22vodart/3542039/p3542039_v_v8_ac.jpg&imgrefurl=http://google.com/search?tbm%3Disch%26q%3DAvatar&h=1440&w=960&tbnid=EjtSrMTdwp5H1M:&q=Avatar&tbnh=186&tbnw=124&usg=AI4_-kQTKJPYEj0eisuHKIHAZu-h_4h_kQ&vet=12ahUKEwi51NHdisTfAhVJvo8KHbNFAXIQ_B0wHXoECAIQBg..i&docid=UHUPOmPGfyBCqM&itg=1&sa=X&ved=2ahUKEwi51NHdisTfAhVJvo8KHbNFAXIQ_B0wHXoECAIQBg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(Avatar.show_trailer())

The_Accidental_Prime_Minister = media.Movie("The Accidental Prime Minister",
                                             "The Accidental Prime Minister is an upcoming 2019 Indian biographical political film",
                                             "https://www.google.com/imgres?imgurl=https://images.news18.com/ibnlive/uploads/221x147/jpg/2018/06/The-Accidental-Prime-Minister.jpg&imgrefurl=https://www.news18.com/newstopics/the-accidental-prime-minister.html&h=147&w=221&tbnid=Z4LF1e5PTY8AlM:&q=the+accidental+prime+minister&tbnh=147&tbnw=221&usg=AI4_-kRTG70iFIreJ2oSjawc23I1nNrQIw&vet=12ahUKEwjDm-Plj8TfAhUCNY8KHXJoBdcQ_B0wK3oECAYQEQ..i&docid=_lIi8Sq33FgrTM&itg=1&sa=X&ved=2ahUKEwjDm-Plj8TfAhUCNY8KHXJoBdcQ_B0wK3oECAYQEQ",
                                             "https://www.youtube.com/watch?v=q6a7YHDK-ik")

#print(The_Accidental_Prime_Minister.show_trailer())

movies=[Deadpool, Avatar, The_Accidental_Prime_Minister, Avatar]

#fresh_tomatoes.open_movies_page(movies)

#print("Doc : " + media.Movie.__doc__)
#print("Name : " + media.Movie.__name__)
#print("Name : " + media.Movie.__module__)
#print(media.Movie.__bases__)
#print(media.Movie.__dict__)
