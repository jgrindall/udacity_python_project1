"""
Extract data on neos and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the
arguments provided at the command line, and uses
the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: path to a CSV file containing data about neos.
    :return: A collection of `NearEarthObject`s.
    """

    neos = []

    with open(neo_csv_path, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for line in reader:
            neo = NearEarthObject.fromData(line)
            neos.append(neo)

    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file
    containing data about close approaches.

    :return: A collection of `CloseApproach`es.
    """

    approaches = []

    with open(cad_json_path, encoding='utf-8') as f:
        response = json.load(f)

        for data in response["data"]:
            approach = CloseApproach.fromData(data)
            approaches.append(approach)

    return approaches
