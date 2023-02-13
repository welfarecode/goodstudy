def make_words(book_name, aort):
    for i in range(1, 46):
        f = open("D:/coding/goodstudy/단어/{}/{}/{}day.txt".format(book_name,aort,i),"w")
        f.write("{0} {1} {2} DAYS".format(book_name,aort,i))
        f.close()

    print("생성 완료")

make_words('하이퍼2000', '시험지')