import numpy as np
# pip install numpy
import cv2
# pip install opencv-python
import os
import time


def mean_square_error(vals_1, vals_2):
    # From CS6603/A4 - AI ML 2/AI_ML_II-dstrube3.ipynb
    # https://pyimagesearch.com/2014/09/15/python-compare-two-images/

    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((vals_1[0] - vals_2[0]) ** 2)
    err /= float(vals_1[1] * vals_1[2])

    # return the MSE
    # the lower the error, the more "similar" the two images are
    return err


def get_images_values(files, folder_path):
    # Returns a dictionary
    image_values = {}
    # giv_index = 0
    # milestone = 50
    # print('* = '+str(milestone)+' images values gotten.')
    for image_file in files:
        # giv_index += 1
        # if giv_index % milestone == 0:
        #     print('*', end='')
        image = cv2.imread(folder_path + image_file)
        if image is not None:
            image_values[image_file] = [image.astype('float'), image.shape[0], image.shape[1]]
    return image_values


# Only one image at a time
def get_image_values(image_file, folder_path):
    image_values = tuple()
    image = cv2.imread(folder_path + image_file)
    if image is not None:
        image_values = (image.astype('float'), image.shape[0], image.shape[1])
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


def clean_list(dirty_list):
    if '.DS_Store' in dirty_list:
        dirty_list.remove('.DS_Store')
    dirty_list.sort()


# region fix_heics
#######################################
# Not in CS6603/A4, because in this context (the wild), we can't rely on all files being the same type

# cv2 doesn't like HEIC:
# https://stackoverflow.com/questions/59949966/how-do-i-read-a-heic-heif-image-into-python-opencv-for-onward-processing
# Workaround:
import pillow_heif
# pip install pillow_heif
import sys


def fix_heics(dir_list):
    print('Looking for HEICs to convert. "*" = 1 HEIC file converted to png')
    heic_conversion_count = 0
    for current_file in dir_list:
        if current_file.upper().endswith('.HEIC'):
            heif_file = pillow_heif.open_heif(path + current_file, convert_hdr_to_8bit=False, bgr_mode=True)
            np_array = np.asarray(heif_file)
            file_name = current_file[:current_file.rfind('.')]
            # Always make sure the file doesn't exist before creating it
            new_file = path + file_name + '.png'
            if os.path.exists(new_file):
                print(
                    'Something went wrong. Was about to create HEIC replacement ' + new_file +
                    ', but it already exists.')
                sys.exit()
                # os.remove(new_file)
            cv2.imwrite(new_file, np_array)
            os.remove(path + current_file)
            print('*', end='')
            heic_conversion_count += 1
            if heic_conversion_count % 100 == 0:
                print()
    if heic_conversion_count > 0:
        print('\nConverted ' + str(heic_conversion_count) + ' HEICs to pngs')
    else:
        print('No HEICs found')


#######################################
# endregion


def main(path):
    # path must end in directory separator ('/' in this case),
    # else Python won't be smart enough to add one,
    # and you'll get file paths like /Users/dstrube/Downloads/temp/test.DS_Store
    dir_list = os.listdir(path)
    dir_list.sort()
    start = time.time()
    fix_heics(dir_list)

    dir_list = os.listdir(path)
    clean_list(dir_list)

    compare_list = os.listdir(path)
    clean_list(compare_list)

    print('Getting image values...')
    images_values = get_images_values(dir_list, path)

    # Exit if get_images_values failed
    if len(images_values) != len(dir_list):
        print('Something went wrong. len(images_values) (' + str(len(images_values)) + ') != len(dir_list) (' +
              str(len(dir_list)) + ')')
        sys.exit()

    print('files count: ' + str(len(dir_list)))

    duplicates = []
    anomalies = []
    index = 0
    print('Looking for duplicates. "." = 1 file checked. "#" = duplicate found...')

    for file in dir_list:
        if file not in images_values.keys():
            # File didn't make it into images_values - skip it
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

        # Doing it this way may be less memory intensive, but takes twice as long with a dir of 19 images
        # (probably longer theoretically)
        # f1_image_values = get_image_values(file, path)
        # for dimensions of file
        f1 = images_values[file]

        for file_other in compare_list:

            #######################################
            # Not in CS6603/A4, because in this context (the wild), we can't rely on
            # same dimensions
            f2 = images_values[file_other]
            # f2_image_values = get_image_values(file_other, path)
            # if f1_image_values[1] != f2_image_values[1] or f1_image_values[2] != f2_image_values[2]:
            if f1[1] != f2[1] or f1[2] != f2[2]:
                # Unequal dimensions - skip
                continue
            #######################################

            # mse = mean_square_error(f1_image_values, f2_image_values)
            mse = mean_square_error(images_values[file], images_values[file_other])
            if mse < 188:
                # print(file + ' seems to be a duplicate of ' + file_other)
                print('#', end='')
                sys.stdout.flush()
                # duplicates.append(file)
                duplicates.append(file_other)
        print('.', end='')
        sys.stdout.flush()
        index += 1
        if index % 100 == 0:
            print()

    end = time.time()
    print('\nDone in ' + get_time(end - start))
    print('Found ' + str(len(duplicates)) + ' duplicates.')
    for duplicate in duplicates:
        print('duplicate: ' + duplicate)
        # if duplicate in dir_list:
        #     dir_list.remove(duplicate)

    for anomaly in anomalies:
        print('anomaly: ' + anomaly)
        # if anomaly in dir_list:
        #     dir_list.remove(anomaly)


if __name__ == "__main__":
    # path = '/Users/dstrube/Downloads/temp/imageDedupe/1/'

    # sys.argv[0] = duplicateImageFinder.py
    main_path = sys.argv[1]
    if not main_path.endswith('/'):
        main_path += '/'
    print("path = " + main_path)

    main(main_path)
"""
"""
