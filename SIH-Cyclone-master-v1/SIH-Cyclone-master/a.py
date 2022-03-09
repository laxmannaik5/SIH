import os
year = 2014
month = 'OCT'
start_date = 1
end_date = 1
img_no = '0000'


url = f"https://mosdac.gov.in/look/3D_IMG/gallery/{year}/{date}{month}/3DIMG_{date}{month}{year}_{img_no}_L1C_ASIA_MER_BIMG.jpg"
path = f'/media/Programs/Hackathon/SIH/data/hudhud/{date:02d}-{month}-{year}.jpg'
command = f'wget -O {path} {url}'
os.system(command)

print(url)