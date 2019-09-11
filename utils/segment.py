#!/usr/bin/env python3

# прочитать файл с текстом (полностью)
with open(
    "/media/zhake/Data/Projects/kaz-parallel-corpora/akorda_kz/xml/texts/kaz_all_text_cleaned_output.split.tok.txt",
    "r",
) as f:
    text_lines = f.readlines()

# прочитать файл с окончаниями (полностью)
with open("/media/zhake/Data/Projects/kaz-parallel-corpora/utils/endings", "r") as f:
    text_endings = f.readlines()

with open("/media/zhake/Data/Projects/kaz-parallel-corpora/utils/stopwords", "r") as f:
    tmp_stoplines = f.readlines()

# убираем '\n' из окончаний
tmp_text_endings = []
for item in text_endings:
    if "\n" in item:
        item = item.replace("\n", "")
    # добавляем пробелы после окончаний чтобы позже находились только окончания в конце слов
    tmp_text_endings.append(item + " ")
text_endings = tmp_text_endings

# для того чтобы показать вторую часть массива окончании из файла
endingsnew = list()
endingsnew_probel = list()
for item in text_endings:
    a, b = item.split(" - ")
    endingsnew.append(a)
    endingsnew_probel.append(b)

tmp_text_lines = []
new_words = []
stoplines = []
for ii in tmp_stoplines:
    if "\n" in ii:
        ii = ii.replace("\n", "")
    stoplines.append(ii)
j = 0

for line in text_lines:
    tmp_words = ""
    words = line.split()
    for word in words:
        j = 0
        if word in stoplines:
            tmp_text_lines.append(word + " ")
        else:
            if len(word) > 2:
                tubir = ""
                affix = ""
                for i in range(2, len(word)):
                    tubir = word[0:i]
                    affix = word[i:]
                    if affix in endingsnew:
                        index = endingsnew.index(affix)
                        affix = endingsnew_probel[index]
                        tmp_words += tubir + "@@ " + affix
                        tmp_text_lines.append(tmp_words)
                        j += 1
                        break
                tmp_words = ""
                if j == 0:
                    tmp_text_lines.append(word + " ")
            else:
                tmp_text_lines.append(word + " ")
    tmp_text_lines.append("\n")

# сохранить результат в отдельный файл
with open("/media/zhake/Data/Projects/kaz-parallel-corpora/akorda_kz/xml/texts/kaz_all_text_cleaned_output.split.tok.segm.txt", "w") as f:
    for line in tmp_text_lines:
        f.write("%s" % line)

print("1-process is over")
