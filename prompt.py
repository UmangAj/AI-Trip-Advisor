image_detection_prompt = """You are an expert in landmark image detection. If there is any landmark in the given image then please give me just the 'landmark name' and if you find any random image or any other image then please give me '1'."""

text_checker_prompt = """
You are an expert in landmark text detection. If there is any landmark in the given text then please give me just the 'landmark name' and if you find any random text or any other text then output should only 1.
"""

landmark_details_prompt = """Write a thorough details of {landmark_name} without prefixes and suffixes and the output should a strong structure or is organized  without any  contact information. The detail should contain Location, Etymology, Inspiration, Architecture and Design, Construction, Tourism, Myths. And the font style is subsubheader and text format."""

landmark_hist_prompt = """ Act as a profession history fact writer. You have to write a well  structured history fact of the {landmark_name}. All the key points should be available and should be elaborated. And the font style is subheader and text format.
 """

landmark_trip_prompt = """Suggest some interesting things to do when visit the {landmark_name} .The response should suggest top 10 popular things of the place in bullet points, has a strong structure, and is organized. And the font style is subsubheader and text format.
Example: 
when visit the Agra : You should taste the Petha because petha is famous in agra.
when visit patan : You should checkout the patola, an traditional saree famous for its making."""

landmark_near_place_prompt = """
Suggest top most 5 near by places to visit if visit {landmark_name}. The response should be json format with place_name and description key. Description should be contain the intersting fact about place.
"""