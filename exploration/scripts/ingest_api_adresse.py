#!/usr/bin/env python3
"""
API Adresse Data Ingestion Script

Geocodes addresses using the French Base Adresse Nationale (BAN) API.

Usage:
    python ingest_api_adresse.py --input INPUT.parquet --output OUTPUT.parquet

TODO: Implement after exploring API behavior in notebook
"""

import argparse


def geocode_address(address, session=None):
    """Geocode a single address using API Adresse

    TODO: Implement based on API exploration findings
    """
    pass


def batch_geocode(df, address_columns, rate_limit=50):
    """Geocode a batch of addresses from a dataframe

    Args:
        df: DataFrame with address columns
        address_columns: List of column names to construct address
        rate_limit: Requests per second (default: 50)

    TODO: Implement batch geocoding logic
    """
    pass


def main():
    parser = argparse.ArgumentParser(description="Geocode addresses with API Adresse")
    parser.add_argument("--input", type=str, required=True, help="Input parquet file")
    parser.add_argument("--output", type=str, required=True, help="Output parquet file")
    parser.add_argument("--rate-limit", type=int, default=50, help="Requests per second")
    args = parser.parse_args()

    print(f"{'=' * 60}")
    print("API Adresse Geocoding")
    print(f"{'=' * 60}\n")
    print("TODO: Implement after notebook exploration")
    print(f"\nPlanned input: {args.input}")
    print(f"Planned output: {args.output}")


if __name__ == "__main__":
    main()
