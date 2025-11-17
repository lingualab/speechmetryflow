
import itertools
import numpy as np
import torch

from numpy.lib.stride_tricks import sliding_window_view
from torch.nn.functional import cosine_similarity


def compute_idea_density(tokens, window_shapes):
    """
    Compute average cosine similarities between token embeddings across
    different sliding window sizes.

    This function measures how semantically similar nearby tokens are,
    for multiple window lengths (e.g. 3, 5, 7). For each window shape,
    all pairwise cosine similarities are computed between embeddings in
    that window, and the mean similarity is recorded.

    To optimize performance, previously computed pairwise similarities
    are cached in `cosine_similarity_data` so that redundant comparisons
    across overlapping windows are not recomputed.

    Parameters
    ----------
    tokens : list
        A list of token objects, each exposing a `.vector` attribute
        (NumPy array) representing its embedding.
    window_shapes : iterable of int
        A list or sequence of integer window sizes to apply
        (e.g., [3, 10, 25, 40]).

    Returns
    -------
    dict
        A dictionary mapping each window size key
        (e.g., "idea_density_3") to the mean cosine similarity
        of all windows of that size. If a window shape is larger
        than the number of tokens, the value is `None`.
    """
    # Convert all token vectors to PyTorch tensors
    embeddings = [torch.from_numpy(token.vector) for token in tokens]
    embeddings_index = list(range(len(embeddings)))
    cosine_similarity_data = {}

    results = {}
    for window_shape in window_shapes:
        results_key = f'idea_density_{window_shape}'

        try:
            # Generate sliding windows of token indices
            windows = sliding_window_view(embeddings_index, window_shape=window_shape)
        except ValueError:
            # if window_shape is larger than embeddings
            results[results_key] = None
            continue

        similarities = []
        for window in windows:
            window_cosine_similarities = []

            # Compute all pairwise cosine similarities in the window
            # cosine similarities are stored in cosine_similarity_data cache
            # in order to avoid multiple computing
            for col1, col2 in itertools.combinations(window, 2):
                col_pairs = (col1, col2)
                if col_pairs not in cosine_similarity_data:
                    cosine_similarity_data[col_pairs] = float(
                        cosine_similarity(embeddings[col1], embeddings[col2], dim=0)
                    )
                window_cosine_similarities.append(cosine_similarity_data[col_pairs])

            # Average similarity for this window
            similarities.append(np.mean(window_cosine_similarities))

        # Mean similarity across all windows of this shape
        results[results_key] = np.mean(similarities)
    
    return results
