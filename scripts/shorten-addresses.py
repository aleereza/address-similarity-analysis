import json
import random


def load_addresses(json_path):
    """
    Load the addresses from a JSON file.

    Parameters:
    json_path (str): The path to the JSON file containing the addresses.

    Returns:
    list: A list of address dictionaries extracted from the 'addresses' key in the JSON file.
    """
    with open(json_path, 'r') as file:
        data = json.load(file)
    return data['addresses']


def find_length_threshold(addresses, percentile=0.9):
    """
    Calculate the length threshold for addresses at a given percentile.

    Parameters:
    addresses (list): A list of address dictionaries. Each dictionary must contain the key 'address1'.
    percentile (float): The percentile to calculate the threshold for. Default is 0.9 (90th percentile).

    Returns:
    int: The length threshold where the specified percentile of addresses are longer than this length.
    """
    lengths = [len(address['address1']) for address in addresses]
    lengths.sort()  # Sorts the lengths in ascending order
    threshold_index = int(len(lengths) * percentile)
    return lengths[threshold_index]


def remove_random_vowels(address_str):
    """
    Remove a random vowel from the given address string.

    Parameters:
    address_str (str): The address string from which to remove a vowel.

    Returns:
    str: The address string with a random vowel removed, if any vowels are present.
    """
    vowels = 'aeiouAEIOU'
    address_chars = list(address_str)
    vowel_indices = [i for i, char in enumerate(address_chars) if char in vowels]
    if vowel_indices:
        index_to_remove = random.choice(vowel_indices)
        address_chars.pop(index_to_remove)
    return ''.join(address_chars)


def shorten_address(address_str, threshold):
    """
    Shorten the address string by removing random vowels until its length is below a specified threshold.

    Parameters:
    address_str (str): The address string to be shortened.
    threshold (int): The maximum allowed length of the address string.

    Returns:
    str: The shortened address string with a length below the threshold.
    """
    has_vowel = True
    while len(address_str) > threshold and has_vowel:
        initial_length = len(address_str)
        address_str = remove_random_vowels(address_str)
        if len(address_str) == initial_length:
            has_vowel = False
    return address_str


def process_addresses(addresses_us_all, original_all_addresses_path, modified_all_addresses_path, changed_addresses_path, percentile=0.9):
    """
    Process the addresses from the input JSON file, shorten those exceeding the length threshold based on the percentile to keep unchanged,
    and store results in two separate JSON files.

    Parameters:
    addresses_us_all (str): Path to the input JSON file containing addresses.
    modified_all_addresses_path (str): Path to the output JSON file to store all addresses.
    changed_addresses_path (str): Path to the output JSON file to store changed addresses.
    percentile (float): The percentile to calculate the length threshold. Default is 0.9.
    """

    addresses = load_addresses(addresses_us_all)
    threshold = find_length_threshold(addresses, percentile)

    modified_all_addresses = []
    original_all_addresses = []
    changed_addresses = []

    for address in addresses:
        address_str = address['address1']

        # Add the (potentially updated) address string to modified_all_addresses
        original_all_addresses.append(address_str)

        if len(address_str) > threshold:

            shortened_address = shorten_address(address_str, threshold)

            # Store the original and shortened versions in changed_addresses
            changed_addresses.append({
                "long_address": address_str,
                "short_address": shortened_address
            })

            modified_all_addresses.append(shortened_address)

        else:
            modified_all_addresses.append(address_str)

    # Write all addresses to the specified output file
    with open(modified_all_addresses_path, 'w') as file:
        json.dump(modified_all_addresses, file, indent=4)
    with open(original_all_addresses_path, 'w') as file:
        json.dump(original_all_addresses, file, indent=4)

    # Write changed addresses to the specified output file
    with open(changed_addresses_path, 'w') as file:
        json.dump(changed_addresses, file, indent=4)


if __name__ == "__main__":
    addresses_us_all = '../data/addresses-us-all.json'  # Path to the JSON file containing all the correct addresses
    original_all_addresses_path = '../data/original_all_addresses.json'  # Path to save the JSON file with original addresses
    modified_all_addresses_path = '../data/modified_all_addresses.json'  # Path to save the JSON file with modified addresses, some of which are shortened due to length restrictions
    changed_addresses_path = '../data/changed_addresses.json'  # Path to the output JSON file to store changed addresses.
    process_addresses(addresses_us_all, original_all_addresses_path, modified_all_addresses_path, changed_addresses_path)
