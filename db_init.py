from datetime import date, datetime
import mongoengine as db
from passwords import db_pass
from models import Post, Like, User

db_name = "postscriptum_db"
db_uri = f"mongodb+srv://mongoUser1:{db_pass}@ps-backend-cluster.8mjxg.mongodb.net/{db_name}?retryWrites=true&w=majority"
db.connect(host=db_uri)

# User(
#     user_id=1,
#     email="mk@student.pl",
#     password="student"
# ).save()

Post.objects().insert([
    Post(post_id=1, 
        author='Michał Kapała', 
        datetime='14.12.2021, 1:03',
        content='Miło by było gdyby treść posta przyzwoicie wyglądała tak jakoś ładnie\n\nO patrzcie drugi akapit wow 😮',
        likes=2,
        ad=False
    ),
    Post(post_id=2, 
        author='Michał Kapała', 
        datetime='14.12.2021, 1:09',
        content='pls pls pls pls pls',
        likes=55,
        ad=False
    ),
    Post(post_id=3, 
        author='Reklamownia', 
        datetime='14.12.2021, 1:30',
        content='To jest post z reklamą',
        likes=123,
        ad=True
    ),
    Post(post_id=4, 
        author='Michał Kapała', 
        datetime='14.12.2021, 19:32',
        content='no ok niech będzie',
        likes=12,
        ad=False
    ),
    Post(post_id=5, 
        author='Reklamownia', 
        datetime='15.12.2021, 1:36',
        content='Na osłodę życia druga reklama',
        likes=0,
        ad=True
    ),
])

# Like(like_id=1, user_id=1, post_id=1).save()
# Like(like_id=1, user_id=1, post_id=3).save()