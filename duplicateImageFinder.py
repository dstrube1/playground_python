import numpy as np
import cv2
import os
import time

# From CS6603/A4 - AI ML 2/AI_ML_II-dstrube3.ipynb

# https://pyimagesearch.com/2014/09/15/python-compare-two-images/
def mean_square_error(vals_1, vals_2):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((vals_1[0] - vals_2[0]) ** 2)
    err /= float(vals_1[1] * vals_1[2])

    # return the MSE
    # the lower the error, the more "similar" the two images are
    return err


def get_images_values(files, folder_path):
    image_values = {}

    for image_file in files:
        image = cv2.imread(folder_path + image_file)
        if image is not None:
            image_values[image_file] = [image.astype('float'), image.shape[0], image.shape[1]]
    return image_values


def get_time(seconds):
    # Copied from my CS 7641 Assignment 2
    if int(seconds / 60) == 0:
        if int(seconds) == 0:
            return str(round(seconds, 3)) + ' seconds'
        return str(int(seconds)) + ' second(s)'
    minutes = int(seconds / 60)
    seconds = int(seconds % 60)
    if int(minutes / 60) == 0:
        return str(minutes) + ' minute(s) and ' + str(seconds) + ' second(s)'
    hours = int(minutes / 60)
    minutes = int(minutes % 60)
    # Assuming this won't be called for any time span greater than 24 hours
    return str(hours) + ' hour(s), ' + str(minutes) + ' minute(s), and ' + str(seconds) + ' second(s)'


path = 'images/'
dir_list = os.listdir(path)
dir_list.sort()
#######################################
# Not in CS6603/A4, because in this context (the wild), we can't rely on all files being the same type

# cv2 doesn't like HEIC:
# https://stackoverflow.com/questions/59949966/how-do-i-read-a-heic-heif-image-into-python-opencv-for-onward-processing
# Workaround:
import pillow_heif
import sys

print('Looking for HEICs to convert. "*" = 1 HEIC file converted to png')
heic_conversion_count = 0
start = time.time()
for file in dir_list:
    if file.upper().endswith('.HEIC'):
        heif_file = pillow_heif.open_heif(path + file, convert_hdr_to_8bit=False, bgr_mode=True)
        np_array = np.asarray(heif_file)
        file_name = file[:file.rfind('.')]
        # Always make sure the file doesn't exist before creating it
        new_file = path + file_name + '.png'
        if os.path.exists(new_file):
            print('Something went wrong. Was about to create HEIC replacement ' + new_file + ', but it already exists.')
            sys.exit()
            # os.remove(new_file)
        cv2.imwrite(new_file, np_array)
        os.remove(path + file)
        print('*', end='')
        heic_conversion_count += 1
        if heic_conversion_count % 100 == 0:
            print()
if heic_conversion_count > 0:
    print('\nConverted ' + str(heic_conversion_count) + ' HEICs to pngs')
else:
    print('No HEICs found')
#######################################

dir_list = os.listdir(path)
dir_list.sort()

compare_list = os.listdir(path)
compare_list.sort()
print('Getting image values...')
images_values = get_images_values(dir_list, path)

# if len(images_values) != len(dir_list):
#     print('Something went wrong. len(images_values) (' + str(len(images_values)) + ') != len(dir_list) (' +
#           str(len(dir_list)) + ')')
#     sys.exit()

print('files count: ' + str(len(dir_list)))

duplicates = []
anomalies = []
index = 0
print('Looking for duplicates & bad file names. "." = 1 file checked. "#" = duplicate found...')

for file in dir_list:
    if file not in images_values.keys():
        # File didn't make it into images_values (like .DS_Store) - skip it
        compare_list.remove(file)
        anomalies.append(file)
        continue
    if file not in compare_list:
        # Previously detected duplicate
        continue
    compare_list.remove(file)
    for duplicate in duplicates:
        if duplicate in compare_list:
            compare_list.remove(duplicate)
    for file_other in compare_list:

        #######################################
        # Not in CS6603/A4, because in this context (the wild), we can't rely on
        # same dimensions
        f1 = images_values[file]
        f2 = images_values[file_other]
        if f1[1] != f2[1] or f1[2] != f2[2]:
            # Unequal dimensions - skip
            continue
        #######################################

        mse = mean_square_error(images_values[file], images_values[file_other])
        if mse < 188:
            # print(file + ' seems to be a duplicate of ' + file_other)
            print('#', end='')
            # duplicates.append(file)
            duplicates.append(file_other)
    print('.', end='')
    index += 1
    if index % 100 == 0:
        print()

end = time.time()
print('\nDone in ' + get_time(end - start))
print('Found ' + str(len(duplicates)) + ' duplicates.')
for duplicate in duplicates:
    print('duplicate: ' + duplicate)
    if duplicate in dir_list:
        dir_list.remove(duplicate)

for anomaly in anomalies:
    if anomaly in dir_list:
        dir_list.remove(anomaly)
