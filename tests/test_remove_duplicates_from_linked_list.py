import os
import sys

import pytest

from algosds.problems.categories.linked_lists.remove_duplicates_from_linked_list import \
    remove_duplicates_from_linked_list_single_while, \
    LinkedList

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

tests = [(
    {
        "linkedList": {
            "head": "1",
            "nodes": [
                {"id": "1", "next": "1-2", "value": 1},
                {"id": "1-2", "next": "1-3", "value": 1},
                {"id": "1-3", "next": "2", "value": 1},
                {"id": "2", "next": "3", "value": 3},
                {"id": "3", "next": "3-2", "value": 4},
                {"id": "3-2", "next": "3-3", "value": 4},
                {"id": "3-3", "next": "4", "value": 4},
                {"id": "4", "next": "5", "value": 5},
                {"id": "5", "next": "5-2", "value": 6},
                {"id": "5-2", "next": None, "value": 6}
            ]
        }
    },
    {
        "head": "1",
        "nodes": [
            {"id": "1", "next": "3", "value": 1},
            {"id": "3", "next": "4", "value": 3},
            {"id": "4", "next": "5", "value": 4},
            {"id": "5", "next": "6", "value": 5},
            {"id": "6", "next": None, "value": 6}
        ]
    }),
    (
        {
            "linkedList": {
                "head": "1",
                "nodes": [
                    {"id": "1", "next": "1-2", "value": 1},
                    {"id": "1-2", "next": "1-3", "value": 1},
                    {"id": "1-3", "next": "1-4", "value": 1},
                    {"id": "1-4", "next": "1-5", "value": 1},
                    {"id": "1-5", "next": "4", "value": 1},
                    {"id": "4", "next": "4-2", "value": 4},
                    {"id": "4-2", "next": "5", "value": 4},
                    {"id": "5", "next": "6", "value": 5},
                    {"id": "6", "next": "6-2", "value": 6},
                    {"id": "6-2", "next": None, "value": 6}
                ]
            }
        },
        {
            "head": "1",
            "nodes": [
                {"id": "1", "next": "4", "value": 1},
                {"id": "4", "next": "5", "value": 4},
                {"id": "5", "next": "6", "value": 5},
                {"id": "6", "next": None, "value": 6}
            ]
        }
    ),
    (
        {
            "linkedList": {
                "head": "1",
                "nodes": [
                    {"id": "1", "next": "1-2", "value": 1},
                    {"id": "1-2", "next": "1-3", "value": 1},
                    {"id": "1-3", "next": "1-4", "value": 1},
                    {"id": "1-4", "next": "1-5", "value": 1},
                    {"id": "1-5", "next": "1-6", "value": 1},
                    {"id": "1-6", "next": "1-7", "value": 1},
                    {"id": "1-7", "next": None, "value": 1}
                ]
            }
        },
        {
            "head": "1",
            "nodes": [
                {"id": "1", "next": None, "value": 1}
            ]
        }
    ),
    (
        {
            "linkedList": {
                "head": "1",
                "nodes": [
                    {"id": "1", "next": "9", "value": 1},
                    {"id": "9", "next": "11", "value": 9},
                    {"id": "11", "next": "15", "value": 11},
                    {"id": "15", "next": "15-2", "value": 15},
                    {"id": "15-2", "next": "16", "value": 15},
                    {"id": "16", "next": "17", "value": 16},
                    {"id": "17", "next": None, "value": 17}
                ]
            }
        },
        {
            "head": "1",
            "nodes": [
                {"id": "1", "next": "9", "value": 1},
                {"id": "9", "next": "11", "value": 9},
                {"id": "11", "next": "15", "value": 11},
                {"id": "15", "next": "16", "value": 15},
                {"id": "16", "next": "17", "value": 16},
                {"id": "17", "next": None, "value": 17}
            ]
        }
    ),
    (
        {
            "linkedList": {
                "head": "1",
                "nodes": [
                    {"id": "1", "next": None, "value": 1}
                ]
            }
        },
        {
            "head": "1",
            "nodes": [
                {"id": "1", "next": None, "value": 1}
            ]
        }
    ),
    (
        {
            "linkedList": {
                "head": "-5",
                "nodes": [
                    {"id": "-5", "next": "-1", "value": -5},
                    {"id": "-1", "next": "-1-2", "value": -1},
                    {"id": "-1-2", "next": "-1-3", "value": -1},
                    {"id": "-1-3", "next": "5", "value": -1},
                    {"id": "5", "next": "5-2", "value": 5},
                    {"id": "5-2", "next": "5-3", "value": 5},
                    {"id": "5-3", "next": "8", "value": 5},
                    {"id": "8", "next": "8-2", "value": 8},
                    {"id": "8-2", "next": "9", "value": 8},
                    {"id": "9", "next": "10", "value": 9},
                    {"id": "10", "next": "11", "value": 10},
                    {"id": "11", "next": "11-2", "value": 11},
                    {"id": "11-2", "next": None, "value": 11}
                ]
            }
        },
        {
            "head": "-5",
            "nodes": [
                {"id": "-5", "next": "-1", "value": -5},
                {"id": "-1", "next": "5", "value": -1},
                {"id": "5", "next": "8", "value": 5},
                {"id": "8", "next": "9", "value": 8},
                {"id": "9", "next": "10", "value": 9},
                {"id": "10", "next": "11", "value": 10},
                {"id": "11", "next": None, "value": 11}
            ]
        }
    ),
    (
        {
            "linkedList": {
                "head": "1",
                "nodes": [
                    {"id": "1", "next": "2", "value": 1},
                    {"id": "2", "next": "3", "value": 2},
                    {"id": "3", "next": "4", "value": 3},
                    {"id": "4", "next": "5", "value": 4},
                    {"id": "5", "next": "6", "value": 5},
                    {"id": "6", "next": "7", "value": 6},
                    {"id": "7", "next": "8", "value": 7},
                    {"id": "8", "next": "9", "value": 8},
                    {"id": "9", "next": "10", "value": 9},
                    {"id": "10", "next": "11", "value": 10},
                    {"id": "11", "next": "12", "value": 11},
                    {"id": "12", "next": "12-2", "value": 12},
                    {"id": "12-2", "next": None, "value": 12}
                ]
            }
        },
        {
            "head": "1",
            "nodes": [
                {"id": "1", "next": "2", "value": 1},
                {"id": "2", "next": "3", "value": 2},
                {"id": "3", "next": "4", "value": 3},
                {"id": "4", "next": "5", "value": 4},
                {"id": "5", "next": "6", "value": 5},
                {"id": "6", "next": "7", "value": 6},
                {"id": "7", "next": "8", "value": 7},
                {"id": "8", "next": "9", "value": 8},
                {"id": "9", "next": "10", "value": 9},
                {"id": "10", "next": "11", "value": 10},
                {"id": "11", "next": "12", "value": 11},
                {"id": "12", "next": None, "value": 12}
            ]
        }
    )
]


@pytest.mark.skip(reason="Should not be run until de deconstruct_linked_list function is created and tested")
@pytest.mark.parametrize("linked_list, answer", tests)
def test_remove_duplicates_from_linked_list_single_while(linked_list, answer):
    assert remove_duplicates_from_linked_list_single_while(create_linked_list(linked_list)) == answer


def create_linked_list(test):
    linked_list = LinkedList(0)

    current_node = linked_list
    current_node.value = test['nodes'][0]["value"]

    for node_idx in range(0, len(test['nodes']) - 1):
        current_node.next = LinkedList(test['nodes'][node_idx + 1]["value"])
        current_node = current_node.next

    return linked_list


def deconstruct_linked_list(linked_list):
    deconstructed_linked_list = {"head": 1, "nodes": []}

    while linked_list.value is not None:
        pass
