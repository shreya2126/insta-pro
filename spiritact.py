from instagram.client import InstagramAPI

client_id = "c1c440a28cc945228d0d70a3f4b51a9e"
client_secret = "68a904567236aa03144ac0919643c8a2"
api = InstagramAPI(client_id=client_id, client_secret=client_secret)
popular_media = api.media_popular(count=20)
for media in popular_media:
    print (media.images['standard_resolution'].url)