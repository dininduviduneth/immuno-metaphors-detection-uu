import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_distances
from sklearn.decomposition import PCA


def main():
    context_words = [
        "invaders",
        "soldiers",
        "attack",
        "invasion",
        "kill",
        "foreign",
        "battle",
        "weapons",
        "destroy",
        "self/other",
        "sense",
        "detect",
        "signal",
        "memory",
        "transmit",
        "respond",
        "send",
        "observe",
    ]
    context = np.load(file="bert_encoded_contexts.npy")
    sentences = np.load(file="bert_encoded_sentences.npy")
    km = KMeans(n_clusters=2)
    pca = PCA(n_components=3)
    data = np.concatenate((sentences[:100], context))
    data = pca.fit_transform(data)
    pcacontext = pca.fit_transform(context)
    km.fit(data)
    centroids = km.cluster_centers_
    for idx, item in enumerate(pcacontext):
        print(
            f"Distance to centroid 1 from {context_words[idx]} was {np.linalg.norm(item - centroids[0])}"
        )
        print(
            f"Distacne to centroid 2 from {context_words[idx]} was {np.linalg.norm(item - centroids[1])}"
        )


if __name__ == "__main__":
    main()
