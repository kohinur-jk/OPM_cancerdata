import os
from PIL import Image


def patch_generator(saving_path, xo, yo, xstep, ystep, H, W, patch_size, img):
    x_arr_dim, y_arr_dim = 0, 0
    if not os.path.exists(saving_path):
        os.makedirs(saving_path)
    for x in range(xo, W, xstep):
        x_arr_dim += 1
        for y in range(yo, H, ystep):
            y_arr_dim += 1
            if (x+patch_size)>W and (y+patch_size)<H:
                xi, xx = W-patch_size, W
                yi, yy = y, y+patch_size
            elif (x+patch_size)<W and (y+patch_size)>H:
                xi, xx = x, x+patch_size
                yi, yy = H-patch_size, H
            elif (x+patch_size)>W and (y+patch_size)>H:
                xi, xx = W-patch_size, W
                yi, yy = H-patch_size, H
            else:
                xi, xx = x, x+patch_size
                yi, yy = y, y+patch_size
                
            #patch = image[xi:xx, yi:yy]
            
            #if 100*(np.sum(patch==1)/(512*512))>95:
            #    Image.fromarray(img[xi:xx, yi:yy, :]).save(f'{saving_path}69987b11_normal_9_x{x}_y{y}_patch.jpg')
            
            Image.fromarray(img[xi:xx, yi:yy, :]).save(f'{saving_path}x{x}_y{y}_patch.jpg')
            
    #prob_arr_ dim is for getting the size of the aray of probability map
    prob_arr_dim = [x_arr_dim, y_arr_dim]
            
    return prob_arr_dim