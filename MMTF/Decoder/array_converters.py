import struct
from MMTF.Common import Utils

def combine_integers(small_array, big_array):
    """Combine integer arrays.  The first is an array purely of integers to be added.
	 The second contains integers in pairs. The first in the pair is to be added.
	 The second in the pair is the number of integers to read from the first array.
	 :param an array of integers
	 :param an array of integers in pairs. The first in the pair
	 is to be added to the output array. The second in the pair is the number of
	 integers to read from the first array.
	 :return the integer array output """
    tot_count = len(big_array)/2
    start = 0
    out_array = []
    
    for in_int in range(tot_count):
        out_array.append(big_array[in_int*2])
        count = big_array[in_int*2+1]
        for small_int in range(start, start+count):
            out_array.append(small_array[small_int])
        start+=count
    return out_array


def convert_bytes_to_ints(in_bytes, num):
    """Convert a byte array into an integer arrays. The number of bytes forming an integer
    is defined by num
    :param the input bytes
    :param the number of bytes per int
    :return the integer array"""
    out_arr = []
    for i in range(len(in_bytes)/num):
        out_arr.append(struct.unpack(Utils.NUM_DICT[num],in_bytes[i*num:i*num+num])[0])
    return out_arr

def decode_chain_list(in_bytes):
    """Convert a list of bytes to a list of strings. Each string is of length
    Utils.CHAIN_LEN
    :param the input bytes
    :return the decoded list of strings"""
    tot_strings = len(in_bytes)/Utils.CHAIN_LEN
    out_strings = []
    for i in range(tot_strings):
        out_s = in_bytes[i*Utils.CHAIN_LEN:i*Utils.CHAIN_LEN+Utils.CHAIN_LEN].strip(Utils.NULL_BYTE)
        out_strings.append(out_s)
    return out_strings

def convert_ints_to_floats(in_ints, divider):
    """Conver integers to floats by division.
    :param the integer array
    :param the divider
    :return the array of floats produced"""
    out_floats = []
    for in_int in in_ints:
        out_floats.append(in_int/divider)
    return out_floats

def convert_ints_to_chars(in_ints):
    """Convert integers to chars.
    :param the input integers
    :return the character array converted"""
    out_chars = []
    for in_int in in_ints:
        out_chars.append(chr(in_int))
    return out_chars


