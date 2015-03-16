# A method to compress a string of alphabetical characters. 
# Eg: AAAABBBGGGEEE would become A4B3G3E3

def compress_string(str)
  compressed_string = ""
  count = 1
  str.each_char.with_index do |letter, index|
    if letter == str[index+1] 
      count += 1
    else 
      compressed_string << letter 
      compressed_string << count.to_s
      count = 1
    end
  end
  compressed_string
end
