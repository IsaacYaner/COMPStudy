# -*- coding: utf-8 -*-
''' Starter code for you to complete Q3 of COMP9727 22T2 Assignment 1.
    No other lines should be altered, except for the indicated area.

    You should firstly extract `q3.csv` from `a1.zip`, and put `q3.csv`
    under the same directory with this file.

    It is your responsibility to ensure that this program can be run on
    any CSE machine's default environment in order to be awarded marks;
    otherwise, you will receive zero.
'''

from typing import Any, Tuple

import os
import numpy as np
import pandas as pd

QUERY_USER = 192
QUERY_ITEM = 156

SMOOTH_COEFF = 5e-2


def load_data(fpath: str = "./q3.csv") -> np.ndarray:
    """Load the rating matrix from a specified file.

    Args:
        fpath (str, optional): file path. Defaults to "./q3.csv".

    Returns:
        np.ndarray: the rating matrix, size of 300 * 300
                    where each row indicates a user's record, and
                    each column indicates an item's record.
    """
    ratings = pd.read_csv(fpath, sep=",").to_numpy()[:, 1:]

    return ratings


def process_data(ratings: np.ndarray) -> Any:
    """As all the entries in `ratings` are `str`, you should consider converting them
       to an appropriate format (e.g., `float`), but missing entries (i.e., `?`) cannot
       be converted to numerical format.

    Args:
        ratings (np.ndarray): The original rating matrix

    Returns:
        ratings (Any): The processed rating matrix (could be in any type as you prefer)
    """

    # --- Please complete the program under this line ---
    # TODO

    # --- Your implementation should be completed within the area above ---

    return ratings


def get_cardinality(
    query_u: int,
    query_i: int,
    ratings: Any,
) -> Tuple[int, int]:
    """ Count the number of elements within a set.

        You should get the cardinality of U_i and I_u, with respect to Eqaution 10,
        within this function.

    Args:
        query_u (int): user_id for query user (note that row index starts from 0)
        query_i (int): item_id for query item (note that column index starts from 0)
        ratings (np.ndarray, [optional]): rating matrix, produced by `process_data()`
                                          Default type is `np.ndarray`, it's fine if you
                                          change it to another type.

    Returns:
        card_I_u (int): The cardinality of set I_u (items that user u has rated)
        card_U_i (int): The cardinality of set U_i (users that have rated item i)
    """
    card_I_u, card_U_i = None, None

    # --- Please complete the program under this line ---
    # TODO

    # --- Your implementation should be completed within the area above ---

    return card_I_u, card_U_i


def cf_ub(
    query_u: int,
    query_i: int,
    ratings: Any,
    alpha=SMOOTH_COEFF,
) -> Tuple[Tuple[float, float], int]:
    """ Implementation of user-based Collaborative filtering with Naive Bayes model.

        The parameters `query_u` and `query_i` specify the missing entry to be predicted

        You should follow the steps in the spec, especially Equations 4, 5, 8, 9,
        in order to produce the correct results

        You can assume that you will only work with two possible ratings: 0 and 1 when
        implementing this function.

    Args:
        query_u (int): user_id for query user (note that row index starts from 0)
        query_i (int): item_id for query item (note that column index starts from 0)
        ratings (np.ndarray, [optional]): rating matrix, produced by `process_data()`
                                          Default type is `np.ndarray`, it's fine if you
                                          change it to another type.
        alpha (float): The Laplacian smoothing coefficient. 
                                  Defaults to SMOOTH_COEFF.

    Returns:
        pred_scores (tuple): A tuple stores classification scores,
                             where pred_scores[0] indicates the score for rating 0,
                                   pred_scores[1] indicates the score for rating 1
        pred_rating (int): The predicted rating (0 or 1)

    """
    pred_scores = (None, None)
    pred_rating = None

    # --- Please complete the program under this line ---
    # TODO

    # --- Your implementation should be completed within the area above ---

    return pred_scores, pred_rating


def cf_ib(
    query_u: int,
    query_i: int,
    ratings: Any,
    alpha=SMOOTH_COEFF,
) -> Tuple[Tuple[float, float], int]:
    """ Implementation of item-based Collaborative filtering with Naive Bayes model.

        The parameters `query_u` and `query_i` specify the missing entry to be predicted

        You should follow the steps in the spec, especially Equations 6, 7, 8, 9,
        in order to produce the correct results

        You can assume that you will only work with two possible ratings: 0 and 1 when
        implementing this function.

    Args:
        query_u (int): user_id for query user (note that row index starts from 0)
        query_i (int): item_id for query item (note that column index starts from 0)
        ratings (np.ndarray, [optional]): rating matrix, produced by `process_data()`
                                          Default type is `np.ndarray`, it's fine if you
                                          change it to another type.
        alpha (float): The Laplacian smoothing coefficient. 
                                  Defaults to SMOOTH_COEFF.

    Returns:
        pred_scores (tuple): A tuple stores classification scores,
                             where pred_scores[0] indicates the score for rating 0,
                                   pred_scores[1] indicates the score for rating 1
        pred_rating (int): The predicted rating (0 or 1)
    """
    pred_scores = (None, None)
    pred_rating = None

    # --- Please complete the program under this line ---
    # TODO

    # --- Your implementation should be completed within the area above ---

    return pred_scores, pred_rating


def cf_hybrid(
    ub_scores: Tuple[float, float],
    ib_scores: Tuple[float, float],
    card_U_i: int,
    card_I_u: int,
) -> Tuple[Tuple[float, float], int]:
    """ Implementation of hybrid Collaborative filtering with Naive Bayes model.

        The hybrid CF is implemented upon user-based CF and item-based CF, so that we use
        the outputs of `cf_ub()` and `cf_ib()`

        You should follow the steps in the spec, especially Equations 10,
        in order to produce the correct results

        You can assume that you will only work with two possible ratings: 0 and 1 when
        implementing this function.

    Args:
        ub_scores (tuple): classification scores of user-based CF
        ib_scores (tuple): classification scores of item-based CF
        card_U_i (int): cardinality of set U_i
        card_I_u (int): cardinality of set I_u

    Returns:
        pred_scores (tuple): A tuple stores classification scores,
                             where pred_scores[0] indicates the score for rating 0,
                                   pred_scores[1] indicates the score for rating 1
        pred_rating (int): The predicted rating (0 or 1). 
    """
    pred_scores = (None, None)
    pred_rating = None

    # --- Please complete the program under this line ---
    # TODO

    # --- Your implementation should be completed within the area above ---

    return pred_scores, pred_rating


def main():
    # load data
    fpath = os.path.join(".", "q3.csv")
    assert os.path.exists(fpath), "No file exists in the specified path"
    ratings = load_data(fpath=fpath)

    # process data
    # you need to find a way to process the data that meets your requirement for the
    # further steps
    ratings = process_data(ratings=ratings)

    # compute user-based collaborative filtering
    ub_scores, ub_rating = cf_ub(query_u=QUERY_USER,
                                 query_i=QUERY_ITEM,
                                 ratings=ratings,
                                 alpha=SMOOTH_COEFF)

    # compute item-based collaborative filtering
    ib_scores, ib_rating = cf_ib(query_u=QUERY_USER,
                                 query_i=QUERY_ITEM,
                                 ratings=ratings,
                                 alpha=SMOOTH_COEFF)

    # get cardinality of I_u and U_i
    card_I_u, card_U_i = get_cardinality(query_u=QUERY_USER,
                                         query_i=QUERY_ITEM,
                                         ratings=ratings)

    # compute hybrid collaborative filtering
    hybrid_scores, hybrid_rating = cf_hybrid(ub_scores=ub_scores,
                                             ib_scores=ib_scores,
                                             card_U_i=card_U_i,
                                             card_I_u=card_I_u)

    # output the results to stdout
    outputs = {
        "user-based": {
            "scores": ub_scores,  # user-based classification scores
            "rating": ub_rating,  # user-based classification prediction
        },
        "item-based": {
            "scores": ib_scores,  # item-based classification scores
            "rating": ib_rating,  # item-based classification prediction
        },
        "hybrid": {
            "scores": hybrid_scores,  # hybrid classification scores
            "rating": hybrid_rating,  # hybrid classification prediction
        },
    }

    print("==========")
    for output in outputs.keys():
        print("For {} CF,\nthe score of rating 0: {}, the score of rating 1: {}".format(
            output, outputs[output]["scores"][0], outputs[output]["scores"][1]))
        print("the predicted rating: {}".format(outputs[output]["rating"]))
        print("==========")


if __name__ == "__main__":
    main()
