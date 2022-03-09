import requests # to get image from the web
import shutil # to save it locally


year = 2014
month = 'OCT'
date = '01'
img_no = 0000

# url = f"https://mosdac.gov.in/look/3D_IMG/gallery/{year}/{date}{month}/3DIMG_{date}{month}{year}_{img_no}_L1C_ASIA_MER_BIMG.jpg"




## Set up the image URL and filename
image_url = f"https://mosdac.gov.in/look/3D_IMG/gallery/{year}/{date}{month}/3DIMG_{date}{month}{year}_{img_no}_L1C_ASIA_MER_BIMG.jpg"
filename = image_url.split("/")[-1]

# Open the url image, set stream to True, this will return the stream content.
r = requests.get(image_url, stream = True)

# Check if the image was retrieved successfully
if r.status_code == 200:
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    r.raw.decode_content = True
    
    # Open a local file with wb ( write binary ) permission.
    with open(filename,'wb') as f:
        shutil.copyfileobj(r.raw, f)
        
    print('Image successfully Downloaded: ',filename)
else:
    print('Image Couldn\'t be retrieved')