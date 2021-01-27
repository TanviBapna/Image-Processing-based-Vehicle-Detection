#import libraries
from pycocotools.coco import COCO
import requests 
import urllib

# Annotations FILE PATH
coco = COCO('coco/annotations/annotations2014/instances_val2014.json')
# Getting category ids
cats = coco.loadCats(coco.getCatIds())
nms=[cat['name'] for cat in cats]
print('COCO categories: \n{}\n'.format(' '.join(nms)))

# Getting category ids only for particular categories ( i.e., car, bus, truck, and motorcycle)
catIds = coco.getCatIds(catNms=['tree'])
# print(catIds)
# Getting the complete information of each image.
imgIds = coco.getImgIds(catIds=catIds )
images = coco.loadImgs(imgIds)
# print("imgIds: ", imgIds)
# print("images: ", images)

for im in images:
    print("im: ", im)
    # img_data = requests.get(im['coco_url']).content
    # Path for downloading the image
    str1 = "/Users/T/Downloads/IMAGES2014/Tree/" +im['file_name']
    try:
        # Downloading the image
        urllib.request.urlretrieve(im['coco_url'],str1)
    except: 
        continue


