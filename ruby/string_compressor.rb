# A method to compress a string of alphabetical characters.
# Eg: AAAABBBGGGEEE would become A4B3G3E3
# if the compressed string will be longer than the original
# string, return the original string

def compress_string(str)
  # compressed string will be the uniqued string * 2 because of the count
  comp_length = str.chars.uniq.length * 2

  # check if compressed string will be shorter than input string
  if comp_length < str.length
    compressed_string = ""
    count = 1
    # iterate over the string
    str.each_char.with_index do |letter, index|
      # if following letter in string is same, increment the count
      #  else add letter and count to compressed_string var
      if letter == str[index+1]
        count += 1
      else
        compressed_string << letter
        compressed_string << count.to_s
        count = 1
      end
    end
    compressed_string
  else
    str
  end
end
