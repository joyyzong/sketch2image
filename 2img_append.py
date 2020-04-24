import os
from PIL import Image
#'door','duck','elephant','eyeglasses','fan','fish','flower','frog','geyser','giraffe','guitar','hamburger','hammer','harp','hat','hedgedog','helicopter','hermit_crab','door','duck','elephant','eyeglasses','fan','fish','flower','frog','geyser','giraffe','guitar','hamburger','hammer','harp','hat'
class_name_list = ['hedgehog','helicopter','hermit_crab'
                    ,'horse','hot-air_balloon','hotdog','hourglass','jack-o-lantern','jellyfish','kangaroo','knife','lion','lizard','lobster','motorcycle','mouse','mushroom','owl','parrot'
                    ,'pear','penguin','piano','pickup_truck','pig','pineapple','pistol','pizza','pretzel','rabbit','raccoon','racket','ray','rhinoceros','rifle','rocket','sailboat','saw'
                    ,'saxophone','scissors','scorpion','sea_turtle','seagull','seal','shark','sheep','skyscraper','snail','snake','songbird','spider','spoon','squirrel','starfish'
                    ,'strawberry','swan','sword','table','tank','teapot','teddy_bear','tiger','trumpet','turtle','umbrella','violin','volcano','wading_bird','wheelchair','windmill','window','zebra']
 
def pinjie(image_path,sketch_path,result_path):
    # 获取当前文件夹中所有JPG图像
    im_list = [os.path.join(image_path,fn) for fn in os.listdir(image_path) if fn.endswith('.png') or fn.endswith('.jpg') ]
    im_name_list = [fn.split('.') for fn in os.listdir(image_path) if fn.endswith('.png') or fn.endswith('.jpg') ]
    sk_list = [os.path.join(sketch_path,fn) for fn in os.listdir(sketch_path) if fn.endswith('.png') or fn.endswith('.jpg') ]
    sk_name_list = [fn.split('-') for fn in os.listdir(sketch_path) if fn.endswith('.png') or fn.endswith('.jpg') ]
    #print("image list =",im_list)
    #print("sketch list =",sk_list)
    print("image name list = ",im_name_list)
    print("sketch name list = ",sk_name_list)
     # 图片转化为相同的尺寸
    ims = []
    for i in im_list:
        new_img = Image.open(i).resize((256, 256), Image.BILINEAR)
        ims.append(new_img)
    sks = []
    for i in sk_list:
        new_img = Image.open(i).resize((256, 256), Image.BILINEAR)
        sks.append(new_img)
    print("number of image = ", len(ims))
    print("number of sketch = ", len(sks))

    # 单幅图像尺寸
    width, height = ims[0].size
    mode = ims[0].mode


    # 拼接图片,对于每一幅草图都匹配相应的图像
    for j, im in enumerate(ims):
        #print(im_name_list[i][0])
        sk_number = 0
        for i, sk in enumerate(sks):
            if im_name_list[j][0] == sk_name_list[i][0]:
                # 创建空白长图
                sk_number = sk_number+1
                result = Image.new(mode, (width * 2, height))
                result.paste(sk, box=(0,0))
                result.paste(im, box=(width,0))
                # 保存图片
                #print(str(im_name_list[j][0]))
                result_name = str(sk_name_list[j][0])+'-'+str(sk_number)+'.png'
                print(result_name)
                if not os.path.exists(result_path):
                    os.makedirs(result_path)
                result.save(os.path.join(result_path,result_name))

 
if __name__ == '__main__':
    for class_name in class_name_list:
        image_path = os.path.join('/Users/joyzong/Desktop/Sketchy/rendered_256x256/256x256/photo/tx_000000000000',class_name)
        sketch_path = os.path.join('/Users/joyzong/Desktop/Sketchy/rendered_256x256/256x256/sketch/tx_000000000000',class_name)
        result_path = os.path.join('/Users/joyzong/Desktop/sketchy_v1',class_name,'result')
        pinjie(image_path,sketch_path,result_path)
