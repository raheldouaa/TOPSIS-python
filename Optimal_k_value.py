from sklearn.cluster import KMeans


import matplotlib.pyplot as plt

def optimal_k_value(data , max_k):
    means = []
    inertias = []
    for k in range(1, max_k):
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(data)
        means.append(k)
        inertias.append(kmeans.inertia_)
        
    # elbow plot
    fig = plt.plot(figsize=(10,5))
    plt.plot(means, inertias, 'o-')
    plt.xlabel('number of clusters')
    plt.ylabel('inertias')
    plt.grid(True)
    plt.show()
            
        