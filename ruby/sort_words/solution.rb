class WordFinder

  def initialize(sorted_results = {})
    @file = "./words.txt"
    @sorted_results = sorted_results
  end

  def run
    do_the_work(@file)
    puts "Your files have been written to this directory"
  end

  def do_the_work(file)
    File.open(file, "r") do |file|
      file.each_line do |word|
        if valid_word?(word)
          clean_word(word)
          if short(word)
            check_unique_and_insert(word, word)
          else
            long(word)
          end
        end
      end
    end
    remove_duplicates(@sorted_results)
    write_files(@sorted_results)
  end

  def write_files(uniques_and_words)
    unique_path = './uniques.txt'
    full_words_path = './fullwords.txt'
    delete_files_if_exit([unique_path, full_words_path])

    sorted_uniques_and_words = uniques_and_words.sort.to_h
    formatted_uniques = formatted_results(sorted_uniques_and_words, :keys)
    formatted_full_words = formatted_results(sorted_uniques_and_words, :values)

    File.write(unique_path, formatted_uniques)
    File.write(full_words_path, formatted_full_words)
  end

  def formatted_results(sorted_uniques_and_words, method)
    formatted_result = ""
    results = sorted_uniques_and_words.send(method)
    results.each do |r|
      formatted_result << "#{r}\n"
    end
    formatted_result
  end

  def remove_duplicates(uniques_and_words)
    uniques_and_words.delete_if{|_,v| v == 0}
  end

  def delete_files_if_exit(paths)
    paths.each do |path|
      File.delete(path) if File.file?(path)
    end
  end

  def long(word)
    i = 0; j = 3
    while j < word.length do
      word_segment = word[i..j]
      check_unique_and_insert(word, word_segment)
      i += 1; j += 1
    end
  end

  def short(word)
    word.length == 4
  end

  def valid_word?(word)
    word.strip.length >= 4 &&
    word.match(/^[[:alpha:]]+$/)
  end

  def clean_word(word)
    word.downcase!
    word.strip!
  end

  def check_unique_and_insert(word, word_segment)
    if @sorted_results[word_segment]
      @sorted_results[word_segment] = 0
    else
      @sorted_results[word_segment] = word
    end
  end

end
