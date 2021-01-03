from imgurpython import ImgurClient

imgur_cfg = {
    "id":'3dfd83a3f58fa10',
    "secret":'3771adc965b3c3de64a10d998a6e91d357ebfd5f',
    "access_token":'ddc490d21b94d7f937228ad6abf69433d8562bf8',
    "refresh_token":'71989a08826c693731ce687cc994292dad8e6a05'
}
imgur_client = ImgurClient(imgur_cfg["id"], imgur_cfg["secret"])
imgur_client.set_user_auth(imgur_cfg["access_token"], imgur_cfg["refresh_token"])

def upload(img_path:str):
    '''
		Upload a picture
	'''
    print("Uploading image... ")
    image = imgur_client.upload_from_path(img_path, anon=False)
    return image['link']