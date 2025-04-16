import requests

def get_image(landmark_name, num_images):
    """
    Function to get image  of specified landmark name.Takes landmark name and number of image of fetching as arguments and gives the list of image urls.

    Arguments
    ---------
    landmark_name : name of landmark that we want to fetch the images.
    image_count : number of images we want

    returns
    --------
    image_url_list : A list of urls containing the images of landmark.
    """    
    PEXELS_API_KEY = "FIrEPMvUNRey3u0wbdFsR1V6PbwQpQk0sKeR3Wsc5EpPpOt9GZWBboWW"
    #url to goto the pexel website
    url = "https://api.pexels.com/v1/search"

    #authorization
    headers = {"Authorization": PEXELS_API_KEY}

    #parameters for  images
    params = {"query": landmark_name, "per_page": num_images, 'orientation':'landscape'}
    response = requests.get(url, headers=headers, params=params).json()
    
    #get the list of image urls
    image_urls_list = [photo["src"]["large"] for photo in response.get("photos", [])]

    return image_urls_list

