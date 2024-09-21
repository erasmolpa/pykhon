#!/bin/sh

poetry install

poetry run kubectl-troubleshooter --help

poetry run kubectl-troubleshooter check-cluster-info

poetry run kubectl-troubleshooter check-control-plane-nodes
