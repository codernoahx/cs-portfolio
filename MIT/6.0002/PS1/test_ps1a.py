from ps1a import load_cows


def test_load_cows():
    samples = {
        "ps1_cow_data.txt": {
            "Maggie": 3,
            "Herman": 7,
            "Betsy": 9,
            "Oreo": 6,
            "Moo Moo": 3,
            "Milkshake": 2,
            "Millie": 5,
            "Lola": 2,
            "Florence": 2,
            "Henrietta": 9,
        },
        "ps1_cow_data_2.txt": {
            "Miss Moo-dy": 3,
            "Milkshake": 4,
            "Lotus": 10,
            "Miss Bella": 2,
            "Horns": 9,
            "Betsy": 5,
            "Rose": 3,
            "Dottie": 6,
        },
        "ps1_cow_data_3.txt": {
            "Bessie": 8,
            "Daisy": 4,
            "Molly": 7,
            "Clover": 5,
            "Elsie": 6,
            "Joy": 2,
        },
        "ps1_cow_data_4.txt": {
            "Patches": 5,
            "Spots": 3,
        },
        "ps1_cow_data_5.txt": {
            "Buttercup": 4,
            "Rosie": 8,
            "Stella": 6,
            "Penelope": 10,
            "Clarice": 5,
            "Cinnamon": 7,
            "Tilly": 2,
            "Olive": 9,
            "Vanilla": 3,
            "Hazel": 6,
            "Ginger": 4,
            "Winnie": 5,
        },
        "ps1_cow_data_6.txt": {
            "Tiny": 1,
            "Giant": 15,
            "Slim": 2,
            "Hefty": 20,
        },
        "ps1_cow_data_7.txt": {
            "Princess": 7,
            "Duchess": 7,
            "Queen": 7,
            "Rebel": 3,
            "Scout": 3,
        },
    }

    for filename in samples:
        assert load_cows(filename) == samples[filename]
