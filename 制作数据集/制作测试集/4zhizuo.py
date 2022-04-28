import os
import argparse
import cv2

#parse args
parser = argparse.ArgumentParser(description='Downsize images at 2x using bicubic interpolation')
parser.add_argument("-k", "--keepdims", help="keep original image dimensions in downsampled images", action="store_true")
parser.add_argument('--hr_img_dir', type=str, default='qietu',
                    help='path to high resolution image dir')
parser.add_argument('--lr_img_dir', type=str, default='Urban100',
                    help='path to desired output dir for downsampled images')
args = parser.parse_args()

hr_image_dir = args.hr_img_dir
lr_image_dir = args.lr_img_dir

print(args.hr_img_dir)
print(args.lr_img_dir)


#create LR image dirs
os.makedirs(lr_image_dir + "/x2", exist_ok=True)
os.makedirs(lr_image_dir + "/x3", exist_ok=True)
os.makedirs(lr_image_dir + "/x4", exist_ok=True)

supported_img_formats = (".jpg", ".png")

num=1

#Downsample HR images
for filename in os.listdir(hr_image_dir):
    # print("2")
    if not filename.endswith(supported_img_formats):
        continue

    name, ext = os.path.splitext(filename)

    #Read HR image
    hr_img = cv2.imread(os.path.join(hr_image_dir, filename))
    hr_img_dims = (hr_img.shape[1], hr_img.shape[0])

    #Blur with Gaussian kernel of width sigma = 1
    hr_img = cv2.GaussianBlur(hr_img, (0,0), 1, 1)

    number_ = str(num).zfill(3)

    #Downsample image 2x
    lr_image_2x = cv2.resize(hr_img, (0,0), fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
    if args.keepdims:
        lr_image_2x = cv2.resize(lr_image_2x, hr_img_dims, interpolation=cv2.INTER_CUBIC)

    cv2.imwrite(os.path.join(lr_image_dir + "/x2", "img_" +number_+"SRF_2_HR.png"), hr_img)
    cv2.imwrite(os.path.join(lr_image_dir + "/x2",  "img_" +number_+"SRF_2_LR.png"), lr_image_2x)

    #Downsample image 3x

    hh=hr_img.shape[0]
    ww=hr_img.shape[1]
    new_hh=int(hh/3)*3
    new_ww = int(ww/3)*3

    new_hr_img = cv2.resize(hr_img,(new_ww,new_hh))
    lr_img_3x = cv2.resize(new_hr_img, (0, 0), fx=(1/3), fy=(1 / 3),
                           interpolation=cv2.INTER_CUBIC)

    if args.keepdims:
        lr_img_3x = cv2.resize(lr_img_3x, hr_img_dims,
                               interpolation=cv2.INTER_CUBIC)
    # cv2.imwrite(os.path.join(lr_image_dir + "x3", filename.split('.')[0]+'x3'+ext), lr_img_3x)
    cv2.imwrite(os.path.join(lr_image_dir + "/x3", "img_" + number_ + "SRF_3_HR.png"), new_hr_img)
    cv2.imwrite(os.path.join(lr_image_dir + "/x3", "img_" + number_ + "SRF_3_LR.png"), lr_img_3x)

    # Downsample image 4x
    lr_img_4x = cv2.resize(hr_img, (0, 0), fx=0.25, fy=0.25,
                           interpolation=cv2.INTER_CUBIC)
    if args.keepdims:
        lr_img_4x = cv2.resize(lr_img_4x, hr_img_dims,
                               interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(os.path.join(lr_image_dir + "/x4", "img_" + number_ + "SRF_4_HR.png"), hr_img)
    cv2.imwrite(os.path.join(lr_image_dir + "/x4", "img_" + number_ + "SRF_4_LR.png"), lr_img_4x)
    num += 1