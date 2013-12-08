import numpy as np
import pylab as pl
from sklearn.cluster import KMeans
from sklearn.metrics import euclidean_distances
from sklearn.datasets import load_sample_image
from sklearn.utils import shuffle
from time import time
import cv2
import os, fnmatch
import skimage
from skimage import io

def find_files(directory, pattern):
	for root, dirs, files in os.walk(directory):
		for basename in files:
			if fnmatch.fnmatch(basename, pattern):
#filename = os.path.join(root, basename)
				yield (root, basename)

def recreate_image(codebook, labels, w, h):
    """Recreate the (compressed) image from the code book & labels"""
    d = codebook.shape[1]
    image = np.zeros((w, h, d))
    label_idx = 0
    for i in range(w):
        for j in range(h):
            image[i][j] = codebook[labels[label_idx]]
            label_idx += 1
    return image


def run_kmeans(inFile,  n_colors):
	china = cv2.imread(inFile)
	china = np.array(china, dtype=np.float64) / 255
	w, h, d = original_shape = tuple(china.shape)
	assert d == 3
	image_array = np.reshape(china, (w * h, d))
	
	print("\tFitting model on a small sub-sample of the data")
	t0 = time()
	image_array_sample = shuffle(image_array, random_state=0)[:1000]
	kmeans = KMeans(k=n_colors, random_state=0).fit(image_array_sample)
	print("\tdone in %0.3fs." % (time() - t0))
	
	# Get labels for all points
	print("\tPredicting color indices on the full image (k-means)")
	t0 = time()
	labels = kmeans.predict(image_array)
	print("\tdone in %0.3fs." % (time() - t0))
	
	codebook_random = shuffle(image_array, random_state=0)[:n_colors + 1]
	print("\tPredicting color indices on the full image (random)")
	t0 = time()
	dist = euclidean_distances(codebook_random, image_array, squared=True)
	labels_random = dist.argmin(axis=0)
	print("\tdone in %0.3fs." % (time() - t0))

	img_kmeans = recreate_image(kmeans.cluster_centers_, labels, w, h)
	img_random = recreate_image(codebook_random, labels_random, w, h)
	return china, img_kmeans, img_random

def runAll():
	num_clusters = [2,4,8,16,64]
	for (root,basename) in find_files('/Users/amirrahimi/Desktop/temp/save/','CROP_0_NUM*.jpg'):
		filename = os.path.join(root,basename)
		print filename
		for n in num_clusters:
			orig, img_kmeans, img_random = run_kmeans(filename, n)
			name_kmeans = 'n_%d_kmeans_CROP.png' % (n)
			name_random = 'n_%d_random_CROP.png' % (n)
#	pl.clf()
#			pl.imshow( img_kmeans)
#			pl.savefig( os.path.join(root, name_kmeans))
#			pl.clf()
#			pl.imshow( img_random)
#			pl.savefig( os.path.join(root, name_random))

			skimage.io.imsave( os.path.join(root, name_kmeans), img_kmeans)
			skimage.io.imsave( os.path.join(root, name_random), img_random)

def deleteAll():
	for (root,basename) in find_files('/Users/amirrahimi/Desktop/temp/save/','n_*_CROP*.png'):
		filename = os.path.join(root,basename)
		os.remove(filename)
		

if __name__ == '__main__':
	runAll()
#	deleteAll()	
