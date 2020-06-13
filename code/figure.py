# Data Mining and Machine Learning 2020
# Group Number 2    ->  [Raz Malka | Shoham Yamin | Raz Itzhak Afriat]
# Research Subject  ->  One-Class SVMs for Document Classification

# This file is meant to provide implementation of graphical figures
import represent
import const

# GUI
import tkinter as tk; from tkinter import ttk

# MatplotLib and Embedding with tkinter
import matplotlib; matplotlib.use("TkAgg");
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure; import matplotlib.pyplot as plt; import matplotlib.font_manager

# TSNE and SVM
from sklearn.svm import OneClassSVM; import numpy as np
from sklearn.manifold import TSNE
from sklearn.preprocessing import normalize

from collections import Counter

figure = canvas = toolbar = None

def createFigure(rightFrame: tk.Frame, item_xpos: int, item_ypos: int, representation: str, kernel_type: str, cache_state: int, outlier_state: int):
    global figure, canvas, toolbar

    # Validity Test
    if representation not in ["Binary", "TF-IDF", "Frequency", "Hadamard"] or kernel_type not in ["Linear", "Radial"]:
        print("Unimplemented!")
        return False

    # Destroy Previous Figure
    canvas.get_tk_widget().destroy()
    canvas._tkcanvas.destroy()
    toolbar.destroy()
    figure.clf()

    # Define "classifiers" to be used
    if kernel_type == "Linear":
        classifiers = {"One-Class SVM": OneClassSVM(nu=0.01, kernel="linear")}    # OPTIMIZED AS OF BINARY
    else:
        classifiers = {"One-Class SVM": OneClassSVM(nu=0.1, kernel="rbf", gamma=0.00001)}     # NOT OPTIMIZED YET
    colors = ['m', 'g', 'b']; legend1 = {}; legend2 = {}

    precalculated_flag = cache_state  # A flag allowing use of precalculated data - Make Controller of this flag

    trainBooks = const.BookSet.HARRY_POTTER
    testBooks = [y for x in [const.books[140:174], const.books[224:250]] for y in x] # 34 HP books (GREEN), 26 GOT books (RED)

    print("--------------------------------------------------")
    if representation == "Binary":
        if precalculated_flag == 0:
            print("Calculating Binary Representation's Keywords ... ")
            keywords = represent.getTrainSetKeywords(trainBooks)
            with open('cache/binary_keywords.npy', 'wb') as f:
                np.save(f, keywords)
            print("Calculating Binary Representation of Training Set ... ")
            train = represent.r_binary(keywords, represent.getTrainSet(trainBooks))
            x_train = np.array(train)
            with open('cache/binary_x_train.npy', 'wb') as f:
                np.save(f, x_train)
            print("Calculating Binary Representation of Testing Set ... ")
            test = represent.r_binary(keywords, testBooks)
            x_test  = np.array(test)
            with open('cache/binary_x_test.npy', 'wb') as f:
                np.save(f, x_test)
            print("Downscaling Dataset Dimensions and Preparing Plot ... ")
        else:
            print("Calculating Binary Representation's Keywords ... ")
            keywords = np.load('cache/binary_keywords.npy')
            print("Calculating Binary Representation of Training Set ... ")
            x_train = np.load('cache/binary_x_train.npy')
            print("Calculating Binary Representation of Testing Set ... ")
            x_test = np.load('cache/binary_x_test.npy')
            print("Downscaling Dataset Dimensions and Preparing Plot ... ")

    if representation == "Frequency":
        if precalculated_flag == 0:
            print("Calculating Frequency Representation's Keywords ... ")
            keywords = represent.getTrainSetKeywords(trainBooks)
            with open('cache/frequency_keywords.npy', 'wb') as f:
                np.save(f, keywords)
            print("Calculating Frequency Representation of Training Set ... ")
            train = represent.r_frequency(keywords, represent.getTrainSet(trainBooks))
            x_train = np.array(train)
            with open('cache/frequency_x_train.npy', 'wb') as f:
                np.save(f, x_train)
            print("Calculating Frequency Representation of Testing Set ... ")
            test = represent.r_frequency(keywords, testBooks)
            x_test  = np.array(test)
            with open('cache/frequency_x_test.npy', 'wb') as f:
                np.save(f, x_test)
            print("Downscaling Dataset Dimensions and Preparing Plot ... ")
        else:
            print("Calculating Frequency Representation's Keywords ... ")
            keywords = np.load('cache/frequency_keywords.npy')
            print("Calculating Frequency Representation of Training Set ... ")
            x_train = np.load('cache/frequency_x_train.npy')
            print("Calculating Frequency Representation of Testing Set ... ")
            x_test = np.load('cache/frequency_x_test.npy')
            print("Downscaling Dataset Dimensions and Preparing Plot ... ")

    if representation == "TF-IDF":
        if precalculated_flag == 0:
            print("Calculating TF-IDF Representation of Training Set ... ")
            x_train  = represent.r_tfidf(represent.getTrainSet(trainBooks))
            with open('cache/tfidf_x_train.npy', 'wb') as f:
                np.save(f, x_train)
            print("Calculating TF-IDF Representation of Testing Set ... ")
            x_test   = represent.r_tfidf(testBooks)
            with open('cache/tfidf_x_test.npy', 'wb') as f:
                np.save(f, x_test)
            print("Downscaling Dataset Dimensions and Preparing Plot ... ")
        else:
            print("Calculating TF-IDF Representation of Training Set ... ")
            x_train = np.load('cache/tfidf_x_train.npy')
            print("Calculating TF-IDF Representation of Testing Set ... ")
            x_test  = np.load('cache/tfidf_x_test.npy')
            print("Downscaling Dataset Dimensions and Preparing Plot ... ")

    if representation == "Hadamard":
        if precalculated_flag == 0:
            print("Calculating Hadamard Representation's Keywords ... ")
            keywords = represent.getTrainSetKeywords(trainBooks)
            with open('cache/hadamard_keywords.npy', 'wb') as f:
                np.save(f, keywords)
            print("Calculating Hadamard Representation of Training Set ... ")
            train = represent.r_hadamard(keywords, represent.getTrainSet(trainBooks), represent.getTrainSet(trainBooks))
            x_train = np.array(train)
            with open('cache/hadamard_x_train.npy', 'wb') as f:
                np.save(f, x_train)
            print("Calculating Hadamard Representation of Testing Set ... ")
            test = represent.r_hadamard(keywords, represent.getTrainSet(trainBooks), testBooks)
            x_test  = np.array(test)
            with open('cache/hadamard_x_test.npy', 'wb') as f:
                np.save(f, x_test)
            print("Downscaling Dataset Dimensions and Preparing Plot ... ")
        else:
            print("Calculating Hadamard Representation's Keywords ... ")
            keywords = np.load('cache/hadamard_keywords.npy')
            print("Calculating Hadamard Representation of Training Set ... ")
            x_train = np.load('cache/hadamard_x_train.npy')
            print("Calculating Hadamard Representation of Testing Set ... ")
            x_test = np.load('cache/hadamard_x_test.npy')
            print("Downscaling Dataset Dimensions and Preparing Plot ... ")

    raw_train   = x_train
    raw_test    = x_test
    # TSNE is responsibly to downscale the dataset from m dimension to n dimension
    if kernel_type == "Linear":
        tsne_train = TSNE(n_components=2, perplexity=20, learning_rate=15)
        tsne_test = TSNE(n_components=2, perplexity=20, learning_rate=15)
    else:
        tsne_train = TSNE(n_components=2, perplexity=20, learning_rate=35)
        tsne_test = TSNE(n_components=2, perplexity=20, learning_rate=35)
    # Learn a frontier for outlier detection with several classifiers
    xx1, yy1 = np.meshgrid(np.linspace(-100, 100, 500), np.linspace(-100, 100, 500))
    for i, (clf_name, clf) in enumerate(classifiers.items()):
        figure = plt.figure(1)
        x_train = tsne_train.fit_transform(x_train)
        x_test  = tsne_test.fit_transform(x_test)
        y_train = clf.fit_predict(x_train)
        y_test = clf.predict(x_test)
        x_pred = np.array([xx1.ravel(), yy1.ravel()]).T #+ [np.repeat(0, xx1.ravel().size) for _ in range(3 - 2)]).T
        Z1 = clf.decision_function(x_pred)
        Z1 = Z1.reshape(xx1.shape)
        legend1[clf_name] = plt.contour(xx1, yy1, Z1, levels=0, linewidths=2, colors=colors[i])

    #x_train = x_train + TSNE(n_components=2, perplexity=25, learning_rate=10).fit_transform(raw_train) / 2
    common_train_value = Counter(y_train).most_common(1)[0][0]  # MOST COMMON VALUE IN TRAIN LABELS

    #print("TRAIN:   ", Counter(y_train).most_common(1)[0], " out of ", len(x_train))
    #print("TEST:    ", Counter(y_test).most_common(1)[0], " out of 34 / ", len(x_test))

    positive_tests = np.array([])   # INIT NUMPY NDARRAY
    negative_tests = np.array([])   # INIT NUMPY NDARRAY
    
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # SHOULD ADD RECALL AND PRECISION IN LABEL TO BE PRINTED ON SCREEN
    # ALSO CHECK WHAT THE F1 thing is about
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    for i, w in enumerate(x_test):
        if y_test[i] == common_train_value:
            positive_tests = np.append(positive_tests,w)
        else:
            negative_tests = np.append(negative_tests,w)
    # Reshape 1D ndarray into 2D ndarray
    positive_tests = np.reshape(positive_tests, (-1, 2))
    negative_tests = np.reshape(negative_tests, (-1, 2))

    legend1_values_list = list(legend1.values())
    legend1_keys_list = list(legend1.keys())

    # Plot the results (= shape of the data points cloud)
    plt.figure(1)  # two clusters
    plt.title("Document Classification using One-Class SVM on Real Books Data Set")
    
    plt.scatter(x_train[:, 0], x_train[:, 1], color='white', edgecolors="black", s=50)
    plt.scatter(x_test[0:34, 0], x_test[0:34, 1], color='yellow', edgecolors="black", s=50)                        # DATA CORRESPONDING TO DEFAULT TRAINING SET - HARRY POTTER
    plt.scatter(x_test[34:len(x_test), 0], x_test[34:len(x_test), 1], color='red', edgecolors="black", s=50)      # DATA THAT SHOULD BE DETECTED AS AN OUTLIER - GAME OF THRONES

    if outlier_state == 1:
        plt.scatter(negative_tests[:,0], negative_tests[:,1], marker='x', color='black')    # Mark Outliers
    bbox_args = dict(boxstyle="round", fc="0.8")
    arrow_args = dict(arrowstyle="->")
    
    #plt.annotate("outlying points", xy=(6, 2), xycoords="data", textcoords="data", xytext=(0, 0.4), bbox=bbox_args, arrowprops=arrow_args)
    plt.xlim((-25, 25)); plt.ylim((-25, 25))
    plt.legend(([legend1_values_list[0].collections[0]]), ([legend1_keys_list[0]]), loc="upper left", prop=matplotlib.font_manager.FontProperties(size=11))
    plt.ylabel("Training Set - WHITE : HARRY POTTER"); plt.xlabel("Testing Set - YELLOW : HARRY POTTER          RED : GAME OF THRONES")

    # Draw and Pack graphical components and controllers
    canvas = FigureCanvasTkAgg(figure, rightFrame); canvas.draw()

    toolbar = NavigationToolbar2Tk(canvas, rightFrame)
    toolbar.config(bg="white")
    toolbar.update()
    toolbar._message_label.config(bg="white")

    canvas.get_tk_widget().pack(side="bottom", fill="both", expand=True, padx=item_xpos, pady=item_ypos)
    canvas._tkcanvas.pack(side="top", fill="both", expand=True, padx=item_xpos, pady=item_ypos)

def emptyFigure(rightFrame: tk.Frame, item_xpos: int, item_ypos: int):
    global figure, canvas, toolbar

    figure = plt.figure(1)
    plt.title("Document Classification using One-Class SVM on Real Books Data Set")
    plt.xlim((-25, 25)); plt.ylim((-25, 25))
    plt.ylabel("Training Set - WHITE : HARRY POTTER"); plt.xlabel("Testing Set - YELLOW : HARRY POTTER          RED : GAME OF THRONES")
    bbox_args = dict(boxstyle="round", fc="0.8")
    arrow_args = dict(arrowstyle="->")
    canvas = FigureCanvasTkAgg(figure, rightFrame); canvas.draw()

    toolbar = NavigationToolbar2Tk(canvas, rightFrame)
    toolbar.config(bg="white")
    toolbar.update()
    toolbar._message_label.config(bg="white")

    canvas.get_tk_widget().pack(side="bottom", fill="both", expand=True, padx=item_xpos, pady=item_ypos)
    canvas._tkcanvas.pack(side="top", fill="both", expand=True, padx=item_xpos, pady=item_ypos)