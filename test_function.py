def Create_url(i):
    for z in range(len(i)):
        i[z] = int(z)
    return f'http://127.0.0.1:5000/search?ptn={i[0]}&time={i[1]}&numm={i[2]}&numd={i[3]}&nbp={i[4]}&nbpa={i[5]}&nbe={i[6]}&racee={i[7]}&gendee={i[8]}&agee={i[9]}&maxe={i[10]}&A1Cresulte={i[11]}&metf={i[12]}&glipe={i[13]}&glybe={i[14]}&piogle={i[15]}&rosige={i[16]}&inse={i[17]}&changee={i[18]}&diabe={i[19]}'
test = Create_url([135,8,33,8,83,0,2,1.0,0.0,5.0,2.0,2.0,2.0,1.0,0.0,1.0,1.0,2.0,0.0,1.0])
print(test)
