import os

cyclone = input("Enter Cyclone Name: ")
year = int(input("Enter Year: "))
month = input("Enter Month(eg. JAN): ")
start_date = int(input("Enter Starting Date: "))
end_date = int(input("Enter end Date: "))

def download(img_no):
    url = f"https://mosdac.gov.in/look/3D_IMG/gallery/{year}/{date:02d}{month}/3DIMG_{date:02d}{month}{year}_{img_no}_L1C_ASIA_MER_BIMG.jpg"
    path = f'/media/Programs/Hackathon/SIH/data/cyclone/{cyclone}/{date:02d}{month}{year}-{img_no}.jpg'
    # path = f'/media/Programs/Hackathon/SIH/data/cyclone/hudhud/'

    command = f'wget -O {path} {url}'
    os.system(command)

for d in range(start_date, end_date+1):
    date = d
    with open('numloop.txt', 'r') as f:
        newline_break = ""
        for loop_no in f:
            img_no = loop_no.strip()
            download(img_no)
       
print("Successful...")              