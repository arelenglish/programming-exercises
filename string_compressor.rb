str = "AAAABBBBCCAAA"

def compress_string(str)
  compressed_string = ""
  count = 1
  str.each_char.with_index do |letter, index|
    if letter == str[index+1] 
      count += 1
    else 
      result << letter 
      result << count.to_s
      count = 1
    end
  end
  compressed_string
end
