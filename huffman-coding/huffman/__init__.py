from .hc import Huffman
import pickle

def get_frequencies(text):
    h = Huffman(text)
    e_text = h.encode()

    print(h.frequencies)
    print("============================")

    with open("sample.txt", 'a') as f:
        # Serialize the character frequency table and write it to the file
        # pickle.dump((h.frequencies, e_text), f)
        # Write a marker to indicate the end of the header and the start of the compressed data
        # f.write(b'\x00\x00\x00\x00\x00')  # Example marker
        f.write(e_text)

    # with open("sample.pkl", 'rb') as f:
    #     data = pickle.load(f)
    #     print(data)

    return h.frequencies