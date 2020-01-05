
import os
import util
from util import videoPlayBack
from shutil import copyfile
import string

activitydict=dict()
pathToVideos=os.path.join("data","UCF-101")

def remove_non_ascii_1(text):

    return ''.join(i for i in text if ord(i)<128)

def init(pathForSplit,files):


	pathForSplit_train=os.path.join(pathForSplit,"train")
	pathForSplit_test=os.path.join(pathForSplit,"test")

	if not os.path.exists(pathForSplit):
		os.makedirs(pathForSplit)
	if not os.path.exists(pathForSplit_train):
		os.makedirs(pathForSplit_train)
	if not os.path.exists(pathForSplit_test):
		os.makedirs(pathForSplit_test)

	return files,pathForSplit_train,pathForSplit_test

def exploreFiles(files,pathForSplit_train,pathForSplit_test,mainSplit):	
	UCF101_Action_detection_splits=os.path.join("data",mainSplit)

	#files = os.listdir(UCF101_Action_detection_splits)

	#print(files)
	print("-------------------------------------------------------")

	for txtFileName in files:
		txtFileName= os.path.join(UCF101_Action_detection_splits,txtFileName)
		readTxtFile(txtFileName)

	print("-------------------------------------------------------")

	'''
	ucfTrainTestlist=os.path.join("data","ucfTrainTestlist")

	files = os.listdir(ucfTrainTestlist)
	for file in files:
		print (file)


	print("-------------------------------------------------------")

	'''


def readTxtFile(txtFileName):
	global activitydict
	f = open(txtFileName, "r")

	if ("testlist" in txtFileName):
		for x in f:
			fileName=x
			#print("in {}  file  name {}".format(txtFileName,fileName))
			pathToVideo=(os.path.join(pathToVideos,fileName)).strip()
			if not (os.path.exists(pathToVideo)):
				continue
			activity=(pathToVideo.split(os.sep))[2]

			#print("pathToVideo: {}".format(pathToVideo))
			#videoPlayBack.playVideo(pathToVideo)

			src=pathToVideo
			#print(pathForSplit_test,fileName)
			dst=(os.path.join(pathForSplit_test,fileName)).strip()
			print("[INFO] Copying from  {} to {} ".format(src, dst))
			print(os.path.exists(src))


			copyfile(src, dst)

			#print("src={}".format(src))
			#print("dst={}".format(dst))
			#input("press any key")

			if not (os.path.exists(dst)):
				exit()



	elif ("classInd.txt" in txtFileName):
		for x in f:
			tokens=x.split(" ")
			activityNumber,activityName=tokens[0],tokens[1]
			activitydict[activityNumber]=activityName.strip()
			activityName=remove_non_ascii_1(activityName)


			#print("in {}  activity number {} with activity name {}".format(txtFileName,activityNumber,activityName))


			path=os.path.join(pathForSplit_train,activityName)
			if not os.path.exists(path):
				os.makedirs(path)

			path=os.path.join(pathForSplit_test,activityName)
			if not os.path.exists(path):
				os.makedirs(path)
				print("Directory for activity {} created ".format(activityName))
	
		print(activitydict)	
    
	else:   #training

		for x in f:
			tokens=x.split(" ")
			fileName,activityNum=tokens[0],tokens[1]
			#print("in {}  file {} wirh activity number {}".format(txtFileName,fileName,activityNum))
			pathToVideo=(os.path.join(pathToVideos,fileName)).strip()
			if not (os.path.exists(pathToVideo)):
				continue
			activity=(pathToVideo.split(os.sep))[2]

			#print("pathToVideo: {}".format(pathToVideo))
			
			#videoPlayBack.playVideo(pathToVideo)

			src=pathToVideo
			#print(pathForSplit_test,fileName)
			dst=os.path.join(pathForSplit_train,fileName)
			print("[INFO] Copying from  {} to {} ".format(src, dst))
			copyfile(src, dst)
			if not (os.path.exists(dst)):
				exit()




if __name__ == "__main__":

	mainSplits=["UCF101_Action_detection_splits","ucfTrainTestlist"]
	mainSplits=["ucfTrainTestlist"]


	for mainSplit in mainSplits:
		pathForSplitOne=os.path.join("data",mainSplit,"splitOne")
		pathForSplit=pathForSplitOne
		files=["classInd.txt","trainlist01.txt" , "testlist01.txt"]
		files,pathForSplit_train,pathForSplit_test=init(pathForSplit,files)
		exploreFiles(files,pathForSplit_train,pathForSplit_test,mainSplit)

		'''


		pathForSplitTwo=os.path.join("data",mainSplit,"splitTwo")
		pathForSplit=pathForSplitTwo
		files=["classInd.txt","trainlist02.txt" , "testlist02.txt"]
		files,pathForSplit_train,pathForSplit_test=init(pathForSplit,files)
		exploreFiles(files,pathForSplit_train,pathForSplit_test,mainSplit)


		pathForSplitThree=os.path.join("data",mainSplit,"splitThree")
		pathForSplit=pathForSplitThree
		files=["classInd.txt","trainlist03.txt" , "testlist03.txt"]
		files,pathForSplit_train,pathForSplit_test=init(pathForSplit,files)
		exploreFiles(files,pathForSplit_train,pathForSplit_test,mainSplit)

		'''


